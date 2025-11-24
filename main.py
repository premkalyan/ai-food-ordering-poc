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

