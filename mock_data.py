"""
Mock data for restaurant ordering API
Realistic restaurants, menus, and pricing across multiple cuisines and locations
"""

from typing import List, Dict
import random
from datetime import datetime, timedelta

# Mock Restaurants
RESTAURANTS = [
    {
        "id": "rest_001",
        "name": "Taj Palace Indian Cuisine",
        "cuisine": "Indian",
        "location": {
            "address": "123 Market St, San Francisco, CA 94103",
            "city": "San Francisco",
            "state": "CA",
            "zip": "94103",
            "lat": 37.7749,
            "lng": -122.4194
        },
        "rating": 4.5,
        "price_range": "$$",
        "delivery_time": "30-45 min",
        "minimum_order": 15.00,
        "delivery_fee": 3.99,
        "is_open": True,
        "image_url": "https://example.com/taj-palace.jpg"
    },
    {
        "id": "rest_002",
        "name": "Golden Dragon Chinese",
        "cuisine": "Chinese",
        "location": {
            "address": "456 Mission St, San Francisco, CA 94105",
            "city": "San Francisco",
            "state": "CA",
            "zip": "94105",
            "lat": 37.7899,
            "lng": -122.3965
        },
        "rating": 4.3,
        "price_range": "$$",
        "delivery_time": "25-35 min",
        "minimum_order": 20.00,
        "delivery_fee": 2.99,
        "is_open": True,
        "image_url": "https://example.com/golden-dragon.jpg"
    },
    {
        "id": "rest_003",
        "name": "Mama Mia Italian Kitchen",
        "cuisine": "Italian",
        "location": {
            "address": "789 Columbus Ave, San Francisco, CA 94133",
            "city": "San Francisco",
            "state": "CA",
            "zip": "94133",
            "lat": 37.8024,
            "lng": -122.4058
        },
        "rating": 4.7,
        "price_range": "$$$",
        "delivery_time": "35-50 min",
        "minimum_order": 25.00,
        "delivery_fee": 4.99,
        "is_open": True,
        "image_url": "https://example.com/mama-mia.jpg"
    },
    {
        "id": "rest_004",
        "name": "Tokyo Sushi Bar",
        "cuisine": "Japanese",
        "location": {
            "address": "321 Geary St, San Francisco, CA 94102",
            "city": "San Francisco",
            "state": "CA",
            "zip": "94102",
            "lat": 37.7871,
            "lng": -122.4108
        },
        "rating": 4.6,
        "price_range": "$$$",
        "delivery_time": "40-55 min",
        "minimum_order": 30.00,
        "delivery_fee": 5.99,
        "is_open": True,
        "image_url": "https://example.com/tokyo-sushi.jpg"
    },
    {
        "id": "rest_005",
        "name": "El Mariachi Mexican Grill",
        "cuisine": "Mexican",
        "location": {
            "address": "555 Valencia St, San Francisco, CA 94110",
            "city": "San Francisco",
            "state": "CA",
            "zip": "94110",
            "lat": 37.7625,
            "lng": -122.4216
        },
        "rating": 4.4,
        "price_range": "$$",
        "delivery_time": "20-30 min",
        "minimum_order": 15.00,
        "delivery_fee": 2.99,
        "is_open": True,
        "image_url": "https://example.com/el-mariachi.jpg"
    },
    {
        "id": "rest_006",
        "name": "Mediterranean Delight",
        "cuisine": "Mediterranean",
        "location": {
            "address": "888 Polk St, San Francisco, CA 94109",
            "city": "San Francisco",
            "state": "CA",
            "zip": "94109",
            "lat": 37.7858,
            "lng": -122.4193
        },
        "rating": 4.5,
        "price_range": "$$",
        "delivery_time": "30-40 min",
        "minimum_order": 18.00,
        "delivery_fee": 3.99,
        "is_open": True,
        "image_url": "https://example.com/mediterranean.jpg"
    },
    {
        "id": "rest_007",
        "name": "Thai Basil House",
        "cuisine": "Thai",
        "location": {
            "address": "234 Clement St, San Francisco, CA 94118",
            "city": "San Francisco",
            "state": "CA",
            "zip": "94118",
            "lat": 37.7833,
            "lng": -122.4633
        },
        "rating": 4.6,
        "price_range": "$$",
        "delivery_time": "25-35 min",
        "minimum_order": 20.00,
        "delivery_fee": 3.49,
        "is_open": True,
        "image_url": "https://example.com/thai-basil.jpg"
    },
    {
        "id": "rest_008",
        "name": "Seoul Kitchen",
        "cuisine": "Korean",
        "location": {
            "address": "567 Irving St, San Francisco, CA 94122",
            "city": "San Francisco",
            "state": "CA",
            "zip": "94122",
            "lat": 37.7636,
            "lng": -122.4686
        },
        "rating": 4.4,
        "price_range": "$$",
        "delivery_time": "30-45 min",
        "minimum_order": 22.00,
        "delivery_fee": 3.99,
        "is_open": True,
        "image_url": "https://example.com/seoul-kitchen.jpg"
    },
    # Bangalore Restaurants
    {
        "id": "rest_009",
        "name": "Spice Garden Indian Kitchen",
        "cuisine": "Indian",
        "location": {
            "address": "MG Road, Bangalore, KA 560001",
            "city": "Bangalore",
            "state": "KA",
            "zip": "560001",
            "lat": 12.9716,
            "lng": 77.5946
        },
        "rating": 4.6,
        "price_range": "$$",
        "delivery_time": "25-40 min",
        "minimum_order": 200.00,
        "delivery_fee": 40.00,
        "is_open": True,
        "image_url": "https://example.com/spice-garden.jpg"
    },
    {
        "id": "rest_010",
        "name": "Bangalore Biryani House",
        "cuisine": "Indian",
        "location": {
            "address": "Indiranagar, Bangalore, KA 560038",
            "city": "Bangalore",
            "state": "KA",
            "zip": "560038",
            "lat": 12.9716,
            "lng": 77.6412
        },
        "rating": 4.7,
        "price_range": "$$",
        "delivery_time": "30-45 min",
        "minimum_order": 250.00,
        "delivery_fee": 50.00,
        "is_open": True,
        "image_url": "https://example.com/biryani-house.jpg"
    },
    {
        "id": "rest_011",
        "name": "Dosa Corner",
        "cuisine": "Indian",
        "location": {
            "address": "Koramangala, Bangalore, KA 560034",
            "city": "Bangalore",
            "state": "KA",
            "zip": "560034",
            "lat": 12.9352,
            "lng": 77.6245
        },
        "rating": 4.5,
        "price_range": "$",
        "delivery_time": "20-30 min",
        "minimum_order": 150.00,
        "delivery_fee": 30.00,
        "is_open": True,
        "image_url": "https://example.com/dosa-corner.jpg"
    },
    # New York Restaurants
    {
        "id": "rest_012",
        "name": "Manhattan Tandoor",
        "cuisine": "Indian",
        "location": {
            "address": "123 Lexington Ave, New York, NY 10016",
            "city": "New York",
            "state": "NY",
            "zip": "10016",
            "lat": 40.7128,
            "lng": -74.0060
        },
        "rating": 4.5,
        "price_range": "$$$",
        "delivery_time": "35-50 min",
        "minimum_order": 25.00,
        "delivery_fee": 5.99,
        "is_open": True,
        "image_url": "https://example.com/manhattan-tandoor.jpg"
    },
    {
        "id": "rest_013",
        "name": "Brooklyn Pizza Palace",
        "cuisine": "Italian",
        "location": {
            "address": "456 Bedford Ave, Brooklyn, NY 11211",
            "city": "New York",
            "state": "NY",
            "zip": "11211",
            "lat": 40.7081,
            "lng": -73.9571
        },
        "rating": 4.6,
        "price_range": "$$",
        "delivery_time": "25-35 min",
        "minimum_order": 20.00,
        "delivery_fee": 4.99,
        "is_open": True,
        "image_url": "https://example.com/brooklyn-pizza.jpg"
    },
    # Los Angeles Restaurants
    {
        "id": "rest_014",
        "name": "LA Sushi Bar",
        "cuisine": "Japanese",
        "location": {
            "address": "789 Santa Monica Blvd, Los Angeles, CA 90046",
            "city": "Los Angeles",
            "state": "CA",
            "zip": "90046",
            "lat": 34.0522,
            "lng": -118.2437
        },
        "rating": 4.7,
        "price_range": "$$$",
        "delivery_time": "40-55 min",
        "minimum_order": 30.00,
        "delivery_fee": 6.99,
        "is_open": True,
        "image_url": "https://example.com/la-sushi.jpg"
    },
    {
        "id": "rest_015",
        "name": "Hollywood Tacos",
        "cuisine": "Mexican",
        "location": {
            "address": "321 Hollywood Blvd, Los Angeles, CA 90028",
            "city": "Los Angeles",
            "state": "CA",
            "zip": "90028",
            "lat": 34.0928,
            "lng": -118.3287
        },
        "rating": 4.4,
        "price_range": "$$",
        "delivery_time": "20-30 min",
        "minimum_order": 15.00,
        "delivery_fee": 3.99,
        "is_open": True,
        "image_url": "https://example.com/hollywood-tacos.jpg"
    },
    # Chicago Restaurants
    {
        "id": "rest_016",
        "name": "Chicago Deep Dish Co",
        "cuisine": "Italian",
        "location": {
            "address": "555 Michigan Ave, Chicago, IL 60611",
            "city": "Chicago",
            "state": "IL",
            "zip": "60611",
            "lat": 41.8781,
            "lng": -87.6298
        },
        "rating": 4.8,
        "price_range": "$$$",
        "delivery_time": "45-60 min",
        "minimum_order": 25.00,
        "delivery_fee": 5.99,
        "is_open": True,
        "image_url": "https://example.com/chicago-pizza.jpg"
    }
]

# Mock Menus by Restaurant
MENUS = {
    "rest_001": {  # Taj Palace Indian
        "categories": [
            {
                "name": "Appetizers",
                "items": [
                    {
                        "id": "item_001",
                        "name": "Samosa (2 pieces)",
                        "description": "Crispy pastry filled with spiced potatoes and peas",
                        "price": 5.99,
                        "vegetarian": True,
                        "spicy": True,
                        "image_url": "https://example.com/samosa.jpg"
                    },
                    {
                        "id": "item_002",
                        "name": "Chicken Tikka",
                        "description": "Marinated chicken pieces grilled in tandoor",
                        "price": 9.99,
                        "vegetarian": False,
                        "spicy": True,
                        "image_url": "https://example.com/chicken-tikka.jpg"
                    }
                ]
            },
            {
                "name": "Main Course",
                "items": [
                    {
                        "id": "item_003",
                        "name": "Paneer Butter Masala",
                        "description": "Cottage cheese in rich tomato cream sauce",
                        "price": 14.99,
                        "vegetarian": True,
                        "spicy": False,
                        "popular": True,
                        "image_url": "https://example.com/paneer-butter-masala.jpg"
                    },
                    {
                        "id": "item_004",
                        "name": "Chicken Tikka Masala",
                        "description": "Grilled chicken in creamy tomato sauce",
                        "price": 16.99,
                        "vegetarian": False,
                        "spicy": True,
                        "popular": True,
                        "image_url": "https://example.com/chicken-tikka-masala.jpg"
                    },
                    {
                        "id": "item_005",
                        "name": "Lamb Rogan Josh",
                        "description": "Tender lamb in aromatic curry sauce",
                        "price": 18.99,
                        "vegetarian": False,
                        "spicy": True,
                        "image_url": "https://example.com/lamb-rogan-josh.jpg"
                    }
                ]
            },
            {
                "name": "Breads",
                "items": [
                    {
                        "id": "item_006",
                        "name": "Garlic Naan",
                        "description": "Leavened bread with garlic and butter",
                        "price": 3.99,
                        "vegetarian": True,
                        "spicy": False,
                        "popular": True,
                        "image_url": "https://example.com/garlic-naan.jpg"
                    },
                    {
                        "id": "item_007",
                        "name": "Butter Naan",
                        "description": "Classic leavened bread with butter",
                        "price": 2.99,
                        "vegetarian": True,
                        "spicy": False,
                        "image_url": "https://example.com/butter-naan.jpg"
                    }
                ]
            },
            {
                "name": "Rice & Biryani",
                "items": [
                    {
                        "id": "item_008",
                        "name": "Vegetable Biryani",
                        "description": "Aromatic basmati rice with mixed vegetables",
                        "price": 13.99,
                        "vegetarian": True,
                        "spicy": True,
                        "image_url": "https://example.com/veg-biryani.jpg"
                    },
                    {
                        "id": "item_009",
                        "name": "Chicken Biryani",
                        "description": "Fragrant rice with tender chicken pieces",
                        "price": 15.99,
                        "vegetarian": False,
                        "spicy": True,
                        "popular": True,
                        "image_url": "https://example.com/chicken-biryani.jpg"
                    }
                ]
            }
        ]
    },
    "rest_002": {  # Golden Dragon Chinese
        "categories": [
            {
                "name": "Appetizers",
                "items": [
                    {
                        "id": "item_101",
                        "name": "Spring Rolls (4 pieces)",
                        "description": "Crispy vegetable spring rolls",
                        "price": 6.99,
                        "vegetarian": True,
                        "image_url": "https://example.com/spring-rolls.jpg"
                    },
                    {
                        "id": "item_102",
                        "name": "Chicken Dumplings (6 pieces)",
                        "description": "Steamed chicken dumplings",
                        "price": 8.99,
                        "vegetarian": False,
                        "popular": True,
                        "image_url": "https://example.com/dumplings.jpg"
                    }
                ]
            },
            {
                "name": "Main Dishes",
                "items": [
                    {
                        "id": "item_103",
                        "name": "Kung Pao Chicken",
                        "description": "Spicy stir-fried chicken with peanuts",
                        "price": 14.99,
                        "vegetarian": False,
                        "spicy": True,
                        "popular": True,
                        "image_url": "https://example.com/kung-pao.jpg"
                    },
                    {
                        "id": "item_104",
                        "name": "Sweet and Sour Pork",
                        "description": "Crispy pork in tangy sweet sauce",
                        "price": 15.99,
                        "vegetarian": False,
                        "image_url": "https://example.com/sweet-sour-pork.jpg"
                    },
                    {
                        "id": "item_105",
                        "name": "Vegetable Lo Mein",
                        "description": "Stir-fried noodles with mixed vegetables",
                        "price": 12.99,
                        "vegetarian": True,
                        "image_url": "https://example.com/lo-mein.jpg"
                    }
                ]
            },
            {
                "name": "Fried Rice",
                "items": [
                    {
                        "id": "item_106",
                        "name": "Chicken Fried Rice",
                        "description": "Classic fried rice with chicken and vegetables",
                        "price": 11.99,
                        "vegetarian": False,
                        "popular": True,
                        "image_url": "https://example.com/chicken-fried-rice.jpg"
                    },
                    {
                        "id": "item_107",
                        "name": "Shrimp Fried Rice",
                        "description": "Fried rice with shrimp and egg",
                        "price": 13.99,
                        "vegetarian": False,
                        "image_url": "https://example.com/shrimp-fried-rice.jpg"
                    }
                ]
            }
        ]
    },
    "rest_003": {  # Mama Mia Italian
        "categories": [
            {
                "name": "Appetizers",
                "items": [
                    {
                        "id": "item_201",
                        "name": "Bruschetta",
                        "description": "Toasted bread with tomatoes, garlic, and basil",
                        "price": 8.99,
                        "vegetarian": True,
                        "image_url": "https://example.com/bruschetta.jpg"
                    },
                    {
                        "id": "item_202",
                        "name": "Calamari Fritti",
                        "description": "Crispy fried calamari with marinara sauce",
                        "price": 12.99,
                        "vegetarian": False,
                        "image_url": "https://example.com/calamari.jpg"
                    }
                ]
            },
            {
                "name": "Pasta",
                "items": [
                    {
                        "id": "item_203",
                        "name": "Spaghetti Carbonara",
                        "description": "Pasta with bacon, egg, and parmesan",
                        "price": 16.99,
                        "vegetarian": False,
                        "popular": True,
                        "image_url": "https://example.com/carbonara.jpg"
                    },
                    {
                        "id": "item_204",
                        "name": "Fettuccine Alfredo",
                        "description": "Creamy parmesan pasta",
                        "price": 15.99,
                        "vegetarian": True,
                        "popular": True,
                        "image_url": "https://example.com/alfredo.jpg"
                    },
                    {
                        "id": "item_205",
                        "name": "Penne Arrabbiata",
                        "description": "Spicy tomato sauce with garlic",
                        "price": 14.99,
                        "vegetarian": True,
                        "spicy": True,
                        "image_url": "https://example.com/arrabbiata.jpg"
                    }
                ]
            },
            {
                "name": "Pizza",
                "items": [
                    {
                        "id": "item_206",
                        "name": "Margherita Pizza",
                        "description": "Classic tomato, mozzarella, and basil",
                        "price": 13.99,
                        "vegetarian": True,
                        "popular": True,
                        "image_url": "https://example.com/margherita.jpg"
                    },
                    {
                        "id": "item_207",
                        "name": "Pepperoni Pizza",
                        "description": "Tomato sauce, mozzarella, and pepperoni",
                        "price": 15.99,
                        "vegetarian": False,
                        "popular": True,
                        "image_url": "https://example.com/pepperoni.jpg"
                    }
                ]
            }
        ]
    },
    "rest_004": {  # Tokyo Sushi Bar
        "categories": [
            {
                "name": "Appetizers",
                "items": [
                    {
                        "id": "item_301",
                        "name": "Edamame",
                        "description": "Steamed soybeans with sea salt",
                        "price": 5.99,
                        "vegetarian": True,
                        "image_url": "https://example.com/edamame.jpg"
                    },
                    {
                        "id": "item_302",
                        "name": "Gyoza (6 pieces)",
                        "description": "Pan-fried pork dumplings",
                        "price": 7.99,
                        "vegetarian": False,
                        "image_url": "https://example.com/gyoza.jpg"
                    }
                ]
            },
            {
                "name": "Sushi Rolls",
                "items": [
                    {
                        "id": "item_303",
                        "name": "California Roll",
                        "description": "Crab, avocado, and cucumber",
                        "price": 8.99,
                        "vegetarian": False,
                        "popular": True,
                        "image_url": "https://example.com/california-roll.jpg"
                    },
                    {
                        "id": "item_304",
                        "name": "Spicy Tuna Roll",
                        "description": "Tuna with spicy mayo",
                        "price": 10.99,
                        "vegetarian": False,
                        "spicy": True,
                        "popular": True,
                        "image_url": "https://example.com/spicy-tuna.jpg"
                    },
                    {
                        "id": "item_305",
                        "name": "Dragon Roll",
                        "description": "Eel, cucumber, avocado on top",
                        "price": 14.99,
                        "vegetarian": False,
                        "image_url": "https://example.com/dragon-roll.jpg"
                    }
                ]
            },
            {
                "name": "Entrees",
                "items": [
                    {
                        "id": "item_306",
                        "name": "Chicken Teriyaki",
                        "description": "Grilled chicken with teriyaki sauce",
                        "price": 15.99,
                        "vegetarian": False,
                        "popular": True,
                        "image_url": "https://example.com/chicken-teriyaki.jpg"
                    },
                    {
                        "id": "item_307",
                        "name": "Salmon Teriyaki",
                        "description": "Grilled salmon with teriyaki sauce",
                        "price": 18.99,
                        "vegetarian": False,
                        "image_url": "https://example.com/salmon-teriyaki.jpg"
                    }
                ]
            }
        ]
    },
    "rest_005": {  # El Mariachi Mexican
        "categories": [
            {
                "name": "Appetizers",
                "items": [
                    {
                        "id": "item_401",
                        "name": "Guacamole & Chips",
                        "description": "Fresh guacamole with tortilla chips",
                        "price": 7.99,
                        "vegetarian": True,
                        "popular": True,
                        "image_url": "https://example.com/guacamole.jpg"
                    },
                    {
                        "id": "item_402",
                        "name": "Queso Fundido",
                        "description": "Melted cheese with chorizo",
                        "price": 9.99,
                        "vegetarian": False,
                        "image_url": "https://example.com/queso-fundido.jpg"
                    }
                ]
            },
            {
                "name": "Tacos",
                "items": [
                    {
                        "id": "item_403",
                        "name": "Carne Asada Tacos (3)",
                        "description": "Grilled steak tacos with cilantro and onions",
                        "price": 12.99,
                        "vegetarian": False,
                        "popular": True,
                        "image_url": "https://example.com/carne-asada-tacos.jpg"
                    },
                    {
                        "id": "item_404",
                        "name": "Fish Tacos (3)",
                        "description": "Battered fish with cabbage slaw",
                        "price": 13.99,
                        "vegetarian": False,
                        "image_url": "https://example.com/fish-tacos.jpg"
                    }
                ]
            },
            {
                "name": "Burritos",
                "items": [
                    {
                        "id": "item_405",
                        "name": "Chicken Burrito",
                        "description": "Grilled chicken, rice, beans, cheese",
                        "price": 11.99,
                        "vegetarian": False,
                        "popular": True,
                        "image_url": "https://example.com/chicken-burrito.jpg"
                    },
                    {
                        "id": "item_406",
                        "name": "Vegetarian Burrito",
                        "description": "Black beans, rice, vegetables, cheese",
                        "price": 10.99,
                        "vegetarian": True,
                        "image_url": "https://example.com/veg-burrito.jpg"
                    }
                ]
            }
        ]
    }
}

# Mock Orders Storage (in-memory)
ORDERS = {}

# Order Status Flow
ORDER_STATUSES = ["pending", "confirmed", "preparing", "ready_for_pickup", "out_for_delivery", "delivered"]

def get_restaurants_by_location(city: str = None, cuisine: str = None, lat: float = None, lng: float = None):
    """Filter restaurants by location and/or cuisine"""
    filtered = RESTAURANTS.copy()
    
    if city:
        filtered = [r for r in filtered if r["location"]["city"].lower() == city.lower()]
    
    if cuisine:
        filtered = [r for r in filtered if r["cuisine"].lower() == cuisine.lower()]
    
    # If lat/lng provided, sort by distance (simplified)
    if lat and lng:
        for r in filtered:
            # Simple distance calculation (not accurate, just for demo)
            r["distance"] = abs(r["location"]["lat"] - lat) + abs(r["location"]["lng"] - lng)
        filtered.sort(key=lambda x: x.get("distance", 999))
    
    return filtered

def get_restaurant_by_id(restaurant_id: str):
    """Get restaurant by ID"""
    for restaurant in RESTAURANTS:
        if restaurant["id"] == restaurant_id:
            return restaurant
    return None

def get_menu_by_restaurant_id(restaurant_id: str):
    """Get menu for a restaurant"""
    return MENUS.get(restaurant_id, {"categories": []})

def create_order(order_data: dict) -> dict:
    """Create a new order"""
    order_id = f"order_{len(ORDERS) + 1:04d}"
    
    order = {
        "id": order_id,
        "restaurant_id": order_data.get("restaurant_id"),
        "restaurant_name": None,
        "items": order_data.get("items", []),
        "subtotal": 0.0,
        "delivery_fee": 0.0,
        "tax": 0.0,
        "total": 0.0,
        "delivery_address": order_data.get("delivery_address"),
        "special_instructions": order_data.get("special_instructions", ""),
        "status": "pending",
        "created_at": datetime.now().isoformat(),
        "estimated_delivery": (datetime.now() + timedelta(minutes=random.randint(30, 60))).isoformat(),
        "payment_status": "pending"
    }
    
    # Get restaurant details
    restaurant = get_restaurant_by_id(order["restaurant_id"])
    if restaurant:
        order["restaurant_name"] = restaurant["name"]
        order["delivery_fee"] = restaurant["delivery_fee"]
    
    # Calculate totals
    subtotal = sum(item.get("price", 0) * item.get("quantity", 1) for item in order["items"])
    order["subtotal"] = round(subtotal, 2)
    order["tax"] = round(subtotal * 0.0875, 2)  # 8.75% tax
    order["total"] = round(order["subtotal"] + order["delivery_fee"] + order["tax"], 2)
    
    ORDERS[order_id] = order
    return order

def get_order_by_id(order_id: str):
    """Get order by ID"""
    return ORDERS.get(order_id)

def update_order_status(order_id: str, status: str):
    """Update order status"""
    if order_id in ORDERS:
        ORDERS[order_id]["status"] = status
        ORDERS[order_id]["updated_at"] = datetime.now().isoformat()
        return ORDERS[order_id]
    return None

def process_payment(order_id: str, payment_method: dict):
    """Process payment for an order"""
    if order_id in ORDERS:
        ORDERS[order_id]["payment_status"] = "completed"
        ORDERS[order_id]["payment_method"] = payment_method
        ORDERS[order_id]["status"] = "confirmed"
        return {
            "success": True,
            "transaction_id": f"txn_{random.randint(100000, 999999)}",
            "message": "Payment processed successfully"
        }
    return {
        "success": False,
        "message": "Order not found"
    }

# Available cuisines
CUISINES = list(set(r["cuisine"] for r in RESTAURANTS))

# Available cities
CITIES = list(set(r["location"]["city"] for r in RESTAURANTS))

# User Favorites (in-memory storage)
USER_FAVORITES = {
    "restaurants": [],  # List of restaurant IDs
    "items": []  # List of {restaurant_id, item_id, item_name}
}

def get_favorite_restaurants():
    """Get user's favorite restaurants"""
    favorite_ids = USER_FAVORITES["restaurants"]
    return [r for r in RESTAURANTS if r["id"] in favorite_ids]

def add_favorite_restaurant(restaurant_id: str):
    """Add restaurant to favorites"""
    if restaurant_id not in USER_FAVORITES["restaurants"]:
        # Verify restaurant exists
        restaurant = get_restaurant_by_id(restaurant_id)
        if restaurant:
            USER_FAVORITES["restaurants"].append(restaurant_id)
            return {"success": True, "message": f"Added {restaurant['name']} to favorites"}
    return {"success": False, "message": "Restaurant already in favorites or not found"}

def remove_favorite_restaurant(restaurant_id: str):
    """Remove restaurant from favorites"""
    if restaurant_id in USER_FAVORITES["restaurants"]:
        USER_FAVORITES["restaurants"].remove(restaurant_id)
        return {"success": True, "message": "Removed from favorites"}
    return {"success": False, "message": "Restaurant not in favorites"}

def get_favorite_items():
    """Get user's favorite menu items"""
    return USER_FAVORITES["items"]

def add_favorite_item(restaurant_id: str, item_id: str, item_name: str):
    """Add menu item to favorites"""
    favorite_item = {
        "restaurant_id": restaurant_id,
        "item_id": item_id,
        "item_name": item_name
    }
    
    # Check if already in favorites
    existing = [f for f in USER_FAVORITES["items"] 
                if f["restaurant_id"] == restaurant_id and f["item_id"] == item_id]
    
    if not existing:
        USER_FAVORITES["items"].append(favorite_item)
        return {"success": True, "message": f"Added {item_name} to favorites"}
    return {"success": False, "message": "Item already in favorites"}

def remove_favorite_item(restaurant_id: str, item_id: str):
    """Remove menu item from favorites"""
    USER_FAVORITES["items"] = [
        f for f in USER_FAVORITES["items"]
        if not (f["restaurant_id"] == restaurant_id and f["item_id"] == item_id)
    ]
    return {"success": True, "message": "Removed from favorites"}

