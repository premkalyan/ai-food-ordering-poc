"""
AI Food Ordering Mock API
FastAPI backend simulating restaurant ordering platform
"""

from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from datetime import datetime
import logging
import json

from mock_data import (
    get_restaurants_by_location,
    get_restaurant_by_id,
    get_menu_by_restaurant_id,
    create_order,
    get_order_by_id,
    update_order_status,
    process_payment,
    CUISINES,
    CITIES,
    RESTAURANTS,
    MENUS,
    get_favorite_restaurants,
    add_favorite_restaurant,
    remove_favorite_restaurant,
    get_favorite_items,
    add_favorite_item,
    remove_favorite_item
)

# Configure logging
# Note: File logging disabled for Vercel serverless environment (read-only filesystem)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler()  # Console only for Vercel
    ]
)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="AI Food Ordering API",
    description="Mock API for ChatGPT Custom GPT integration - Restaurant ordering platform",
    version="1.0.0",
    servers=[
        {"url": "http://localhost:8000", "description": "Local development server"},
        {"url": "https://ai-food-ordering-poc.vercel.app", "description": "Production server (Vercel)"}
    ]
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request logging middleware
@app.middleware("http")
async def log_requests(request: Request, call_next):
    """Log all API requests and responses"""
    request_id = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
    
    # Log request
    request_log = {
        "request_id": request_id,
        "timestamp": datetime.now().isoformat(),
        "method": request.method,
        "url": str(request.url),
        "path": request.url.path,
        "query_params": dict(request.query_params),
        "client_host": request.client.host if request.client else None,
        "user_agent": request.headers.get("user-agent", ""),
    }
    
    # Get request body if present
    if request.method in ["POST", "PUT", "PATCH"]:
        try:
            body = await request.body()
            if body:
                request_log["body"] = json.loads(body.decode())
        except:
            pass
    
    logger.info(f"REQUEST: {json.dumps(request_log, indent=2)}")
    
    # Process request
    response = await call_next(request)
    
    # Log response
    response_log = {
        "request_id": request_id,
        "timestamp": datetime.now().isoformat(),
        "status_code": response.status_code,
    }
    
    logger.info(f"RESPONSE: {json.dumps(response_log, indent=2)}")
    
    return response

# Pydantic models
class Location(BaseModel):
    address: str
    city: str
    state: str
    zip: str
    lat: Optional[float] = None
    lng: Optional[float] = None

class Restaurant(BaseModel):
    id: str
    name: str
    cuisine: str
    location: Location
    rating: float
    price_range: str
    delivery_time: str
    minimum_order: float
    delivery_fee: float
    is_open: bool
    image_url: Optional[str] = None

class MenuItem(BaseModel):
    id: str
    name: str
    description: str
    price: float
    vegetarian: Optional[bool] = False
    spicy: Optional[bool] = False
    popular: Optional[bool] = False
    image_url: Optional[str] = None

class MenuCategory(BaseModel):
    name: str
    items: List[MenuItem]

class Menu(BaseModel):
    categories: List[MenuCategory]

class OrderItem(BaseModel):
    item_id: str
    name: str
    price: float
    quantity: int = 1
    special_instructions: Optional[str] = None

class CreateOrderRequest(BaseModel):
    restaurant_id: str
    items: List[OrderItem]
    delivery_address: Location
    special_instructions: Optional[str] = None

class Order(BaseModel):
    id: str
    restaurant_id: str
    restaurant_name: Optional[str]
    items: List[OrderItem]
    subtotal: float
    delivery_fee: float
    tax: float
    total: float
    delivery_address: Location
    special_instructions: Optional[str]
    status: str
    created_at: str
    estimated_delivery: str
    payment_status: str

class PaymentMethod(BaseModel):
    type: str = Field(..., description="Payment type: credit_card, debit_card, paypal, apple_pay")
    last_four: Optional[str] = Field(None, description="Last 4 digits of card")

class PaymentRequest(BaseModel):
    payment_method: PaymentMethod

class PaymentResponse(BaseModel):
    success: bool
    transaction_id: Optional[str]
    message: str

class IntelligentSearchRequest(BaseModel):
    query: str = Field(..., description="Natural language query (e.g., 'spicy food in 15 minutes under $10')")
    user_id: Optional[str] = Field(None, description="User ID for personalization")
    location: Optional[str] = Field(None, description="User location/city")

class ParsedQuery(BaseModel):
    intent: str
    cuisine: Optional[List[str]] = None
    dish: Optional[str] = None
    price_max: Optional[float] = None
    time_max: Optional[int] = None
    preferences: List[str] = []
    location: Optional[str] = None
    use_favorites: bool = False
    urgency: Optional[str] = None

class IntelligentSearchResponse(BaseModel):
    parsed_query: ParsedQuery
    restaurants: List[Restaurant]
    suggested_items: List[Dict[str, Any]]
    message: str
    alternatives: Optional[List[str]] = None

# API Endpoints

@app.get("/")
async def root():
    """Root endpoint with API information"""
    return {
        "name": "AI Food Ordering API",
        "version": "1.0.0",
        "description": "Mock API for ChatGPT Custom GPT integration",
        "docs_url": "/docs",
        "openapi_production": "/openapi-production.json",
        "endpoints": {
            "restaurants": "/api/v1/restaurants/search",
            "menu": "/api/v1/restaurants/{id}/menu",
            "orders": "/api/v1/orders",
        }
    }

@app.get("/openapi-production.json")
async def get_production_openapi():
    """Serve production-only OpenAPI spec (no localhost)"""
    import os
    import json
    
    # Read the openapi-production.json file
    file_path = os.path.join(os.path.dirname(__file__), "openapi-production.json")
    with open(file_path, 'r') as f:
        return json.load(f)

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat()
    }

# Restaurant Endpoints

@app.get(
    "/api/v1/restaurants/search",
    response_model=List[Restaurant],
    summary="Search restaurants",
    description="Search for restaurants by location, cuisine, or coordinates. Returns list of available restaurants."
)
async def search_restaurants(
    city: Optional[str] = None,
    cuisine: Optional[str] = None,
    lat: Optional[float] = None,
    lng: Optional[float] = None
):
    """
    Search for restaurants based on various criteria.
    
    - **city**: Filter by city name (e.g., "San Francisco")
    - **cuisine**: Filter by cuisine type (e.g., "Indian", "Chinese", "Italian")
    - **lat**: Latitude for location-based search
    - **lng**: Longitude for location-based search
    """
    logger.info(f"Searching restaurants: city={city}, cuisine={cuisine}, lat={lat}, lng={lng}")
    
    restaurants = get_restaurants_by_location(city=city, cuisine=cuisine, lat=lat, lng=lng)
    
    logger.info(f"Found {len(restaurants)} restaurants")
    return restaurants

@app.get(
    "/api/v1/restaurants/{restaurant_id}",
    response_model=Restaurant,
    summary="Get restaurant details",
    description="Get detailed information about a specific restaurant"
)
async def get_restaurant(restaurant_id: str):
    """
    Get detailed information about a specific restaurant.
    
    - **restaurant_id**: Unique restaurant identifier
    """
    logger.info(f"Getting restaurant details: {restaurant_id}")
    
    restaurant = get_restaurant_by_id(restaurant_id)
    if not restaurant:
        raise HTTPException(status_code=404, detail="Restaurant not found")
    
    return restaurant

@app.get(
    "/api/v1/restaurants/{restaurant_id}/menu",
    response_model=Menu,
    summary="Get restaurant menu",
    description="Get the complete menu for a specific restaurant with all items and prices"
)
async def get_menu(restaurant_id: str):
    """
    Get the complete menu for a restaurant.
    
    - **restaurant_id**: Unique restaurant identifier
    """
    logger.info(f"Getting menu for restaurant: {restaurant_id}")
    
    # Verify restaurant exists
    restaurant = get_restaurant_by_id(restaurant_id)
    if not restaurant:
        raise HTTPException(status_code=404, detail="Restaurant not found")
    
    menu = get_menu_by_restaurant_id(restaurant_id)
    return menu

# Order Endpoints

@app.post(
    "/api/v1/orders/create",
    response_model=Order,
    summary="Create new order",
    description="Create a new food order with items, delivery address, and special instructions"
)
async def create_new_order(order_request: CreateOrderRequest):
    """
    Create a new order.
    
    - **restaurant_id**: Restaurant to order from
    - **items**: List of menu items with quantities
    - **delivery_address**: Delivery location
    - **special_instructions**: Optional special requests
    """
    logger.info(f"Creating order: restaurant={order_request.restaurant_id}, items={len(order_request.items)}")
    
    # Verify restaurant exists
    restaurant = get_restaurant_by_id(order_request.restaurant_id)
    if not restaurant:
        raise HTTPException(status_code=404, detail="Restaurant not found")
    
    # Create order
    order = create_order(order_request.dict())
    
    logger.info(f"Order created: {order['id']}, total=${order['total']}")
    return order

@app.get(
    "/api/v1/orders/{order_id}",
    response_model=Order,
    summary="Get order status",
    description="Get current status and details of an order"
)
async def get_order(order_id: str):
    """
    Get order details and current status.
    
    - **order_id**: Unique order identifier
    """
    logger.info(f"Getting order: {order_id}")
    
    order = get_order_by_id(order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    
    return order

@app.post(
    "/api/v1/orders/{order_id}/payment",
    response_model=PaymentResponse,
    summary="Process payment",
    description="Process payment for an order"
)
async def process_order_payment(order_id: str, payment_request: PaymentRequest):
    """
    Process payment for an order.
    
    - **order_id**: Unique order identifier
    - **payment_method**: Payment method details
    """
    logger.info(f"Processing payment for order: {order_id}, method={payment_request.payment_method.type}")
    
    # Verify order exists
    order = get_order_by_id(order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    
    # Process payment
    result = process_payment(order_id, payment_request.payment_method.dict())
    
    logger.info(f"Payment result: {result}")
    return result

@app.get(
    "/api/v1/orders/{order_id}/track",
    summary="Track order",
    description="Get real-time order tracking information with automatic status progression"
)
async def track_order(order_id: str):
    """
    Track order with automatic status updates based on time elapsed.
    
    - **order_id**: Unique order identifier
    
    Status progression (automatic):
    - 0-2 mins: pending
    - 2-5 mins: confirmed
    - 5-20 mins: preparing
    - 20-30 mins: ready_for_pickup
    - 30-45 mins: out_for_delivery
    - 45+ mins: delivered
    """
    logger.info(f"Tracking order: {order_id}")
    
    order = get_order_by_id(order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    
    # Calculate time elapsed since order creation
    from datetime import datetime, timedelta
    created_at = datetime.fromisoformat(order.get("created_at", datetime.now().isoformat()))
    elapsed_minutes = (datetime.now() - created_at).total_seconds() / 60
    
    # Auto-update status based on elapsed time (DEMO MODE: 12 mins total)
    # 6 stages × 2 minutes each for quick demo
    if elapsed_minutes < 2:
        current_status = "pending"
        status_message = "Order received! Waiting for restaurant confirmation."
        eta_minutes = 12
    elif elapsed_minutes < 4:
        current_status = "confirmed"
        status_message = "Restaurant confirmed your order!"
        eta_minutes = 10
    elif elapsed_minutes < 6:
        current_status = "preparing"
        status_message = "Your food is being prepared! 🍳"
        eta_minutes = 8
    elif elapsed_minutes < 8:
        current_status = "ready_for_pickup"
        status_message = "Order is ready! Waiting for delivery driver."
        eta_minutes = 6
    elif elapsed_minutes < 10:
        current_status = "out_for_delivery"
        status_message = "On the way to you! 🚚"
        eta_minutes = 4
    elif elapsed_minutes < 12:
        current_status = "out_for_delivery"
        status_message = "Almost there! Driver is nearby! 🚚"
        eta_minutes = 2
    else:
        current_status = "delivered"
        status_message = "Delivered! Enjoy your meal! 🍽️"
        eta_minutes = 0
    
    # Update order status in storage
    order["status"] = current_status
    
    # Calculate ETA
    eta_time = (datetime.now() + timedelta(minutes=eta_minutes)).strftime("%I:%M %p")
    
    return {
        "order_id": order_id,
        "status": current_status,
        "status_message": status_message,
        "estimated_delivery": eta_time if eta_minutes > 0 else "Delivered",
        "minutes_remaining": eta_minutes,
        "restaurant": order.get("restaurant_name", "Restaurant"),
        "total": order.get("total", 0),
        "items_count": len(order.get("items", [])),
        "delivery_address": order.get("delivery_address", {}).get("address", ""),
        "created_at": order.get("created_at"),
        "elapsed_minutes": int(elapsed_minutes)
    }

@app.patch(
    "/api/v1/orders/{order_id}/status",
    response_model=Order,
    summary="Update order status",
    description="Update the status of an order (for testing/simulation)"
)
async def update_order(order_id: str, status: str):
    """
    Update order status (for simulation purposes).
    
    - **order_id**: Unique order identifier
    - **status**: New status (pending, confirmed, preparing, ready_for_pickup, out_for_delivery, delivered)
    """
    logger.info(f"Updating order status: {order_id} -> {status}")
    
    order = update_order_status(order_id, status)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    
    return order

# Utility Endpoints

@app.get(
    "/api/v1/cuisines",
    summary="Get available cuisines",
    description="Get list of all available cuisine types in a structured format"
)
async def get_cuisines():
    """Get list of available cuisines"""
    logger.info("Getting available cuisines")
    cuisines = sorted(CUISINES)
    return {
        "cuisines": cuisines,
        "count": len(cuisines),
        "message": "Available cuisine types",
        "prompt": "Which cuisine are you in the mood for? Choose one from the list above."
    }

@app.get(
    "/api/v1/cities",
    summary="Get available cities",
    description="Get list of all cities with restaurants in a structured format for better UX"
)
async def get_cities():
    """Get list of cities with restaurants"""
    logger.info("Getting available cities")
    cities = sorted(CITIES)
    return {
        "cities": cities,
        "count": len(cities),
        "message": "Available cities for food delivery",
        "prompt": "Which city are you in? Just type or click one of the options above."
    }

# User preference endpoints (for future enhancement)

@app.get(
    "/api/v1/user/location",
    summary="Get user location",
    description="Get user's current location (simulated based on IP/context)"
)
async def get_user_location(city: Optional[str] = None):
    """
    Get user's current location (simulated).
    In production, this would use IP geolocation or user profile.
    For demo, returns San Francisco by default or specified city.
    """
    logger.info(f"Getting user location: {city if city else 'default'}")
    
    # If city specified, try to find a restaurant in that city
    if city:
        restaurants = get_restaurants_by_location(city=city)
        if restaurants:
            location = restaurants[0]["location"]
            return {
                "city": location["city"],
                "state": location["state"],
                "lat": location["lat"],
                "lng": location["lng"],
                "available": True
            }
    
    # Default to San Francisco (where we have restaurants)
    return {
        "city": "San Francisco",
        "state": "CA",
        "lat": 37.7749,
        "lng": -122.4194,
        "available": True,
        "note": "Demo location - in production, would use actual geolocation"
    }

# Intelligent Search Endpoint

def parse_natural_language_query(query: str, location: Optional[str] = None) -> ParsedQuery:
    """
    Parse natural language query into structured data
    """
    query_lower = query.lower()
    
    # Extract cuisine
    cuisines_found = []
    for cuisine in CUISINES:
        if cuisine.lower() in query_lower:
            cuisines_found.append(cuisine)
    
    # Extract dish names (common dishes)
    dish = None
    common_dishes = [
        "tandoori chicken", "butter chicken", "biryani", "naan",
        "pizza", "pasta", "margherita", "pepperoni",
        "sushi", "ramen", "tempura",
        "tacos", "burrito", "quesadilla",
        "pad thai", "curry", "fried rice", "noodles"
    ]
    for dish_name in common_dishes:
        if dish_name in query_lower:
            dish = dish_name.title()
            break
    
    # Extract price constraint
    price_max = None
    import re
    price_match = re.search(r'\$(\d+)', query_lower)
    if price_match:
        price_max = float(price_match.group(1))
    elif "under" in query_lower or "below" in query_lower:
        # Look for numbers after "under" or "below"
        under_match = re.search(r'(?:under|below)\s+\$?(\d+)', query_lower)
        if under_match:
            price_max = float(under_match.group(1))
    
    # Extract time constraint
    time_max = None
    time_match = re.search(r'(\d+)\s*(?:min|minute)', query_lower)
    if time_match:
        time_max = int(time_match.group(1))
    elif "quick" in query_lower or "fast" in query_lower or "asap" in query_lower:
        time_max = 20  # Assume quick means 20 minutes or less
    
    # Extract preferences
    preferences = []
    if "spicy" in query_lower or "hot" in query_lower:
        preferences.append("spicy")
    if "vegetarian" in query_lower or "veg" in query_lower:
        preferences.append("vegetarian")
    if "vegan" in query_lower:
        preferences.append("vegan")
    if "healthy" in query_lower:
        preferences.append("healthy")
    
    # Detect favorites intent
    use_favorites = "favorite" in query_lower or "usual" in query_lower or "regular" in query_lower
    
    # Detect urgency
    urgency = None
    if "hungry" in query_lower or "starving" in query_lower:
        urgency = "high"
    
    # Determine intent
    if use_favorites:
        intent = "favorites"
    elif dish or cuisines_found:
        intent = "search"
    elif urgency:
        intent = "urgent"
    else:
        intent = "browse"
    
    return ParsedQuery(
        intent=intent,
        cuisine=cuisines_found if cuisines_found else None,
        dish=dish,
        price_max=price_max,
        time_max=time_max,
        preferences=preferences,
        location=location,
        use_favorites=use_favorites,
        urgency=urgency
    )

def filter_restaurants_by_query(parsed: ParsedQuery, restaurants: List[Dict]) -> List[Dict]:
    """
    Filter restaurants based on parsed query
    """
    results = restaurants.copy()
    
    # Filter by cuisine
    if parsed.cuisine:
        results = [r for r in results if r["cuisine"] in parsed.cuisine]
    
    # Filter by delivery time
    if parsed.time_max:
        results = [r for r in results if extract_max_delivery_time(r["delivery_time"]) <= parsed.time_max]
    
    # Sort by relevance
    if parsed.urgency == "high":
        # Sort by fastest delivery
        results.sort(key=lambda r: extract_max_delivery_time(r["delivery_time"]))
    else:
        # Sort by rating
        results.sort(key=lambda r: r["rating"], reverse=True)
    
    return results

def extract_max_delivery_time(delivery_time_str: str) -> int:
    """
    Extract maximum delivery time from string like '30-45 min'
    """
    import re
    match = re.search(r'(\d+)-(\d+)', delivery_time_str)
    if match:
        return int(match.group(2))
    return 60  # Default to 60 if can't parse

def filter_menu_items_by_query(parsed: ParsedQuery, menu: Dict) -> List[Dict]:
    """
    Filter menu items based on parsed query - SIMPLIFIED for performance
    """
    all_items = []
    
    # Flatten menu items from all categories - limit to first 20 items for speed
    for category in menu.get("categories", [])[:5]:  # Only first 5 categories
        for item in category.get("items", [])[:10]:  # Only first 10 items per category
            try:
                item_dict = item.copy() if isinstance(item, dict) else item.dict()
                item_dict["category"] = category.get("name", "")
                all_items.append(item_dict)
            except:
                continue
    
    results = all_items
    
    # Quick filters only
    if parsed.dish and results:
        dish_lower = parsed.dish.lower()
        results = [item for item in results if dish_lower in item.get("name", "").lower()][:5]
    
    if parsed.price_max and results:
        results = [item for item in results if item.get("price", 0) <= parsed.price_max][:5]
    
    if "spicy" in parsed.preferences and results:
        results = [item for item in results if item.get("spicy", False)][:5]
    
    if "vegetarian" in parsed.preferences and results:
        results = [item for item in results if item.get("vegetarian", False)][:5]
    
    return results[:5]  # Return max 5 items

@app.post(
    "/api/v1/search/intelligent",
    response_model=IntelligentSearchResponse,
    summary="Intelligent search with natural language",
    description="Search restaurants using complex natural language queries with multiple constraints"
)
async def intelligent_search(request: IntelligentSearchRequest):
    """
    Handle complex natural language queries like:
    - "I would like to try Tandoori Chicken from an Indian restaurant"
    - "I'm hungry, get me something spicy in 15 minutes"
    - "Something Italian under $5 in 10 minutes"
    """
    logger.info(f"[INTELLIGENT_SEARCH] ========== REQUEST RECEIVED ==========")
    logger.info(f"[INTELLIGENT_SEARCH] Query: '{request.query}'")
    logger.info(f"[INTELLIGENT_SEARCH] Location: '{request.location}'")
    
    try:
        logger.info(f"[INTELLIGENT_SEARCH] Step 1: Parsing query...")
        
        # Parse the query
        parsed = parse_natural_language_query(request.query, request.location)
        logger.info(f"[INTELLIGENT_SEARCH] Step 1 DONE - Parsed: {parsed.dict()}")
    except Exception as e:
        logger.error(f"[INTELLIGENT_SEARCH] Parse error: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Query parsing failed: {str(e)}")
    
    try:
        logger.info(f"[INTELLIGENT_SEARCH] Step 2: Getting restaurants...")
        # Get all restaurants (or filter by location if provided)
        if request.location or parsed.location:
            city = request.location or parsed.location
            all_restaurants = get_restaurants_by_location(city=city)
        else:
            all_restaurants = RESTAURANTS
        
        logger.info(f"[INTELLIGENT_SEARCH] Step 2 DONE - Found {len(all_restaurants)} restaurants")
        
        logger.info(f"[INTELLIGENT_SEARCH] Step 3: Filtering restaurants...")
        # Filter restaurants by parsed query
        filtered_restaurants = filter_restaurants_by_query(parsed, all_restaurants)
        logger.info(f"[INTELLIGENT_SEARCH] Step 3 DONE - Filtered to {len(filtered_restaurants)} restaurants")
    except Exception as e:
        logger.error(f"[INTELLIGENT_SEARCH] Filter error: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Restaurant filtering failed: {str(e)}")
    
    try:
        logger.info(f"[INTELLIGENT_SEARCH] Step 4: Getting menu items...")
        # Get suggested menu items - SIMPLIFIED for performance
        suggested_items = []
        
        # Only process menu items if we have specific dish or price constraints
        if parsed.dish or parsed.price_max or parsed.preferences:
            logger.info(f"[INTELLIGENT_SEARCH] Step 4a: Processing menus for top {min(2, len(filtered_restaurants))} restaurants")
            for restaurant in filtered_restaurants[:2]:  # Only top 2 restaurants
                menu = MENUS.get(restaurant["id"], {"categories": []})
                items = filter_menu_items_by_query(parsed, menu)
                for item in items[:1]:  # Only top 1 item per restaurant
                    suggested_items.append({
                        "restaurant_id": restaurant["id"],
                        "restaurant_name": restaurant["name"],
                        "item_id": item.get("id", ""),
                        "item_name": item.get("name", ""),
                        "price": item.get("price", 0),
                        "category": item.get("category", ""),
                        "spicy": item.get("spicy", False),
                        "vegetarian": item.get("vegetarian", False)
                    })
        else:
            logger.info(f"[INTELLIGENT_SEARCH] Step 4a: Skipping menu items (no dish/price/preference constraints)")
        
        logger.info(f"[INTELLIGENT_SEARCH] Step 4 DONE - Found {len(suggested_items)} suggested items")
    except Exception as e:
        logger.error(f"[INTELLIGENT_SEARCH] Menu items error: {str(e)}")
        suggested_items = []  # Continue without suggested items
    
    logger.info(f"[INTELLIGENT_SEARCH] Step 5: Building response...")
    
    # Build response message
    if not filtered_restaurants:
        message = "No restaurants match your criteria."
        alternatives = []
        
        if parsed.price_max:
            alternatives.append(f"Try increasing your budget above ${parsed.price_max}")
        if parsed.time_max:
            alternatives.append(f"Allow more than {parsed.time_max} minutes for delivery")
        if parsed.cuisine:
            alternatives.append(f"Try a different cuisine")
        
        logger.info(f"[INTELLIGENT_SEARCH] Step 5 DONE - No results, returning alternatives")
        return IntelligentSearchResponse(
            parsed_query=parsed,
            restaurants=[],
            suggested_items=[],
            message=message,
            alternatives=alternatives if alternatives else None
        )
    
    # Success message
    if parsed.dish:
        message = f"Found {len(filtered_restaurants)} restaurants with {parsed.dish}"
    elif parsed.cuisine:
        cuisine_str = ", ".join(parsed.cuisine)
        message = f"Found {len(filtered_restaurants)} {cuisine_str} restaurants"
    elif parsed.urgency == "high":
        fastest = filtered_restaurants[0]
        message = f"Found {len(filtered_restaurants)} restaurants, fastest delivery in {fastest['delivery_time']}"
    else:
        message = f"Found {len(filtered_restaurants)} restaurants matching your criteria"
    
    if parsed.time_max:
        message += f" (delivery within {parsed.time_max} minutes)"
    if parsed.price_max:
        message += f" (items under ${parsed.price_max})"
    
    logger.info(f"[INTELLIGENT_SEARCH] Step 5 DONE - Returning {len(filtered_restaurants[:5])} restaurants")
    logger.info(f"[INTELLIGENT_SEARCH] ========== REQUEST COMPLETE ==========")
    
    return IntelligentSearchResponse(
        parsed_query=parsed,
        restaurants=filtered_restaurants[:5],  # Return top 5
        suggested_items=suggested_items,
        message=message,
        alternatives=None
    )

# Favorites Endpoints

@app.get(
    "/api/v1/favorites/restaurants",
    response_model=List[Restaurant],
    summary="Get favorite restaurants",
    description="Get user's saved favorite restaurants"
)
async def get_favorites():
    """Get user's favorite restaurants"""
    logger.info("Getting favorite restaurants")
    favorites = get_favorite_restaurants()
    return favorites

@app.post(
    "/api/v1/favorites/restaurants/{restaurant_id}",
    summary="Add restaurant to favorites",
    description="Save a restaurant to user's favorites"
)
async def add_restaurant_to_favorites(restaurant_id: str):
    """Add restaurant to favorites"""
    logger.info(f"Adding restaurant to favorites: {restaurant_id}")
    result = add_favorite_restaurant(restaurant_id)
    if not result["success"]:
        raise HTTPException(status_code=400, detail=result["message"])
    return result

@app.delete(
    "/api/v1/favorites/restaurants/{restaurant_id}",
    summary="Remove restaurant from favorites",
    description="Remove a restaurant from user's favorites"
)
async def remove_restaurant_from_favorites(restaurant_id: str):
    """Remove restaurant from favorites"""
    logger.info(f"Removing restaurant from favorites: {restaurant_id}")
    result = remove_favorite_restaurant(restaurant_id)
    return result

@app.get(
    "/api/v1/favorites/items",
    summary="Get favorite menu items",
    description="Get user's saved favorite menu items across all restaurants"
)
async def get_favorite_menu_items():
    """Get user's favorite menu items"""
    logger.info("Getting favorite menu items")
    favorites = get_favorite_items()
    return {"favorites": favorites}

@app.post(
    "/api/v1/favorites/items",
    summary="Add menu item to favorites",
    description="Save a menu item to user's favorites"
)
async def add_menu_item_to_favorites(
    restaurant_id: str,
    item_id: str,
    item_name: str
):
    """Add menu item to favorites"""
    logger.info(f"Adding item to favorites: {item_name} from {restaurant_id}")
    result = add_favorite_item(restaurant_id, item_id, item_name)
    if not result["success"]:
        raise HTTPException(status_code=400, detail=result["message"])
    return result

@app.delete(
    "/api/v1/favorites/items",
    summary="Remove menu item from favorites",
    description="Remove a menu item from user's favorites"
)
async def remove_menu_item_from_favorites(
    restaurant_id: str,
    item_id: str
):
    """Remove menu item from favorites"""
    logger.info(f"Removing item from favorites: {item_id} from {restaurant_id}")
    result = remove_favorite_item(restaurant_id, item_id)
    return result

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

