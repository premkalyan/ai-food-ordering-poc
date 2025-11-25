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
        "delivery_time": "25-40 min",
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
        "delivery_time": "30-45 min",
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
        "delivery_time": "25-40 min",
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
        "delivery_time": "30-45 min",
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
        "delivery_time": "30-45 min",
        "minimum_order": 25.00,
        "delivery_fee": 5.99,
        "is_open": True,
        "image_url": "https://example.com/chicago-pizza.jpg"
    },
    {
        "id": "rest_017",
        "name": "Windy City Tacos",
        "cuisine": "Mexican",
        "location": {
            "address": "123 State St, Chicago, IL 60602",
            "city": "Chicago",
            "state": "IL",
            "zip": "60602",
            "lat": 41.8819,
            "lng": -87.6278
        },
        "rating": 4.6,
        "price_range": "$$",
        "delivery_time": "15-25 min",
        "minimum_order": 12.00,
        "delivery_fee": 2.99,
        "is_open": True,
        "image_url": "https://example.com/windy-tacos.jpg"
    },
    {
        "id": "rest_018",
        "name": "Lake Shore Chinese",
        "cuisine": "Chinese",
        "location": {
            "address": "789 Wabash Ave, Chicago, IL 60605",
            "city": "Chicago",
            "state": "IL",
            "zip": "60605",
            "lat": 41.8756,
            "lng": -87.6244
        },
        "rating": 4.4,
        "price_range": "$$",
        "delivery_time": "20-30 min",
        "minimum_order": 15.00,
        "delivery_fee": 3.49,
        "is_open": True,
        "image_url": "https://example.com/lakeshore-chinese.jpg"
    },
    {
        "id": "rest_019",
        "name": "Chicago Tandoor",
        "cuisine": "Indian",
        "location": {
            "address": "456 Michigan Ave, Chicago, IL 60611",
            "city": "Chicago",
            "state": "IL",
            "zip": "60611",
            "lat": 41.8902,
            "lng": -87.6250
        },
        "rating": 4.7,
        "price_range": "$$",
        "delivery_time": "25-35 min",
        "minimum_order": 20.00,
        "delivery_fee": 3.99,
        "is_open": True,
        "image_url": "https://example.com/chicago-tandoor.jpg"
    },
    # === BANGALORE - Fill Missing Cuisines ===
    {
        "id": "rest_020",
        "name": "Bangalore Wok",
        "cuisine": "Chinese",
        "location": {
            "address": "88 MG Road, Bangalore, KA 560001",
            "city": "Bangalore",
            "state": "Karnataka",
            "zip": "560001",
            "lat": 12.9716,
            "lng": 77.5946
        },
        "rating": 4.3,
        "price_range": "$$",
        "delivery_time": "20-30 min",
        "minimum_order": 15.00,
        "delivery_fee": 2.99,
        "is_open": True,
        "image_url": "https://example.com/bangalore-wok.jpg"
    },
    {
        "id": "rest_021",
        "name": "Pasta Paradise Bangalore",
        "cuisine": "Italian",
        "location": {
            "address": "45 Indiranagar, Bangalore, KA 560038",
            "city": "Bangalore",
            "state": "Karnataka",
            "zip": "560038",
            "lat": 12.9716,
            "lng": 77.5946
        },
        "rating": 4.4,
        "price_range": "$$",
        "delivery_time": "25-35 min",
        "minimum_order": 18.00,
        "delivery_fee": 3.49,
        "is_open": True,
        "image_url": "https://example.com/pasta-paradise-blr.jpg"
    },
    {
        "id": "rest_022",
        "name": "Sakura Sushi Bangalore",
        "cuisine": "Japanese",
        "location": {
            "address": "12 Koramangala, Bangalore, KA 560034",
            "city": "Bangalore",
            "state": "Karnataka",
            "zip": "560034",
            "lat": 12.9352,
            "lng": 77.6245
        },
        "rating": 4.6,
        "price_range": "$$$",
        "delivery_time": "30-40 min",
        "minimum_order": 25.00,
        "delivery_fee": 4.99,
        "is_open": True,
        "image_url": "https://example.com/sakura-blr.jpg"
    },
    {
        "id": "rest_023",
        "name": "Seoul Kitchen Bangalore",
        "cuisine": "Korean",
        "location": {
            "address": "67 Whitefield, Bangalore, KA 560066",
            "city": "Bangalore",
            "state": "Karnataka",
            "zip": "560066",
            "lat": 12.9698,
            "lng": 77.7499
        },
        "rating": 4.5,
        "price_range": "$$",
        "delivery_time": "25-35 min",
        "minimum_order": 20.00,
        "delivery_fee": 3.99,
        "is_open": True,
        "image_url": "https://example.com/seoul-blr.jpg"
    },
    {
        "id": "rest_024",
        "name": "Mediterranean Oasis Bangalore",
        "cuisine": "Mediterranean",
        "location": {
            "address": "34 Brigade Road, Bangalore, KA 560025",
            "city": "Bangalore",
            "state": "Karnataka",
            "zip": "560025",
            "lat": 12.9716,
            "lng": 77.5946
        },
        "rating": 4.4,
        "price_range": "$$$",
        "delivery_time": "28-38 min",
        "minimum_order": 22.00,
        "delivery_fee": 4.49,
        "is_open": True,
        "image_url": "https://example.com/med-oasis-blr.jpg"
    },
    {
        "id": "rest_025",
        "name": "Bangalore Fiesta",
        "cuisine": "Mexican",
        "location": {
            "address": "56 Jayanagar, Bangalore, KA 560041",
            "city": "Bangalore",
            "state": "Karnataka",
            "zip": "560041",
            "lat": 12.9250,
            "lng": 77.5838
        },
        "rating": 4.2,
        "price_range": "$$",
        "delivery_time": "22-32 min",
        "minimum_order": 16.00,
        "delivery_fee": 3.49,
        "is_open": True,
        "image_url": "https://example.com/fiesta-blr.jpg"
    },
    {
        "id": "rest_026",
        "name": "Thai Spice Bangalore",
        "cuisine": "Thai",
        "location": {
            "address": "78 HSR Layout, Bangalore, KA 560102",
            "city": "Bangalore",
            "state": "Karnataka",
            "zip": "560102",
            "lat": 12.9121,
            "lng": 77.6446
        },
        "rating": 4.5,
        "price_range": "$$",
        "delivery_time": "24-34 min",
        "minimum_order": 18.00,
        "delivery_fee": 3.99,
        "is_open": True,
        "image_url": "https://example.com/thai-spice-blr.jpg"
    },
    # === CHICAGO - Fill Missing Cuisines ===
    {
        "id": "rest_027",
        "name": "Tokyo Express Chicago",
        "cuisine": "Japanese",
        "location": {
            "address": "789 State St, Chicago, IL 60605",
            "city": "Chicago",
            "state": "IL",
            "zip": "60605",
            "lat": 41.8781,
            "lng": -87.6298
        },
        "rating": 4.6,
        "price_range": "$$$",
        "delivery_time": "28-38 min",
        "minimum_order": 25.00,
        "delivery_fee": 4.99,
        "is_open": True,
        "image_url": "https://example.com/tokyo-chicago.jpg"
    },
    {
        "id": "rest_028",
        "name": "Seoul BBQ Chicago",
        "cuisine": "Korean",
        "location": {
            "address": "234 Wabash Ave, Chicago, IL 60604",
            "city": "Chicago",
            "state": "IL",
            "zip": "60604",
            "lat": 41.8781,
            "lng": -87.6265
        },
        "rating": 4.7,
        "price_range": "$$",
        "delivery_time": "25-35 min",
        "minimum_order": 20.00,
        "delivery_fee": 3.99,
        "is_open": True,
        "image_url": "https://example.com/seoul-chicago.jpg"
    },
    {
        "id": "rest_029",
        "name": "Greek Islands Chicago",
        "cuisine": "Mediterranean",
        "location": {
            "address": "567 N Michigan Ave, Chicago, IL 60611",
            "city": "Chicago",
            "state": "IL",
            "zip": "60611",
            "lat": 41.8902,
            "lng": -87.6250
        },
        "rating": 4.5,
        "price_range": "$$$",
        "delivery_time": "30-40 min",
        "minimum_order": 22.00,
        "delivery_fee": 4.49,
        "is_open": True,
        "image_url": "https://example.com/greek-chicago.jpg"
    },
    {
        "id": "rest_030",
        "name": "Thai Elephant Chicago",
        "cuisine": "Thai",
        "location": {
            "address": "890 W Randolph St, Chicago, IL 60607",
            "city": "Chicago",
            "state": "IL",
            "zip": "60607",
            "lat": 41.8843,
            "lng": -87.6501
        },
        "rating": 4.4,
        "price_range": "$$",
        "delivery_time": "26-36 min",
        "minimum_order": 18.00,
        "delivery_fee": 3.99,
        "is_open": True,
        "image_url": "https://example.com/thai-chicago.jpg"
    },
    # === LOS ANGELES - Fill Missing Cuisines ===
    {
        "id": "rest_031",
        "name": "Golden Dragon LA",
        "cuisine": "Chinese",
        "location": {
            "address": "345 W 3rd St, Los Angeles, CA 90013",
            "city": "Los Angeles",
            "state": "CA",
            "zip": "90013",
            "lat": 34.0522,
            "lng": -118.2437
        },
        "rating": 4.4,
        "price_range": "$$",
        "delivery_time": "22-32 min",
        "minimum_order": 15.00,
        "delivery_fee": 3.49,
        "is_open": True,
        "image_url": "https://example.com/golden-dragon-la.jpg"
    },
    {
        "id": "rest_032",
        "name": "Bollywood Bites LA",
        "cuisine": "Indian",
        "location": {
            "address": "678 S Flower St, Los Angeles, CA 90017",
            "city": "Los Angeles",
            "state": "CA",
            "zip": "90017",
            "lat": 34.0522,
            "lng": -118.2437
        },
        "rating": 4.5,
        "price_range": "$$",
        "delivery_time": "25-35 min",
        "minimum_order": 18.00,
        "delivery_fee": 3.99,
        "is_open": True,
        "image_url": "https://example.com/bollywood-la.jpg"
    },
    {
        "id": "rest_033",
        "name": "Venice Italian Kitchen",
        "cuisine": "Italian",
        "location": {
            "address": "123 Abbot Kinney Blvd, Los Angeles, CA 90291",
            "city": "Los Angeles",
            "state": "CA",
            "zip": "90291",
            "lat": 33.9925,
            "lng": -118.4695
        },
        "rating": 4.6,
        "price_range": "$$$",
        "delivery_time": "28-38 min",
        "minimum_order": 22.00,
        "delivery_fee": 4.49,
        "is_open": True,
        "image_url": "https://example.com/venice-italian.jpg"
    },
    {
        "id": "rest_034",
        "name": "Seoul Station LA",
        "cuisine": "Korean",
        "location": {
            "address": "456 S Western Ave, Los Angeles, CA 90020",
            "city": "Los Angeles",
            "state": "CA",
            "zip": "90020",
            "lat": 34.0522,
            "lng": -118.2437
        },
        "rating": 4.7,
        "price_range": "$$",
        "delivery_time": "24-34 min",
        "minimum_order": 20.00,
        "delivery_fee": 3.99,
        "is_open": True,
        "image_url": "https://example.com/seoul-la.jpg"
    },
    {
        "id": "rest_035",
        "name": "Santorini Grill LA",
        "cuisine": "Mediterranean",
        "location": {
            "address": "789 Pico Blvd, Los Angeles, CA 90015",
            "city": "Los Angeles",
            "state": "CA",
            "zip": "90015",
            "lat": 34.0407,
            "lng": -118.2595
        },
        "rating": 4.5,
        "price_range": "$$$",
        "delivery_time": "30-40 min",
        "minimum_order": 24.00,
        "delivery_fee": 4.99,
        "is_open": True,
        "image_url": "https://example.com/santorini-la.jpg"
    },
    {
        "id": "rest_036",
        "name": "Thai Town LA",
        "cuisine": "Thai",
        "location": {
            "address": "234 N Vermont Ave, Los Angeles, CA 90004",
            "city": "Los Angeles",
            "state": "CA",
            "zip": "90004",
            "lat": 34.0922,
            "lng": -118.2915
        },
        "rating": 4.6,
        "price_range": "$$",
        "delivery_time": "23-33 min",
        "minimum_order": 17.00,
        "delivery_fee": 3.49,
        "is_open": True,
        "image_url": "https://example.com/thai-town-la.jpg"
    },
    # === NEW YORK - Fill Missing Cuisines ===
    {
        "id": "rest_037",
        "name": "Chinatown Express NYC",
        "cuisine": "Chinese",
        "location": {
            "address": "567 Canal St, New York, NY 10013",
            "city": "New York",
            "state": "NY",
            "zip": "10013",
            "lat": 40.7128,
            "lng": -74.0060
        },
        "rating": 4.3,
        "price_range": "$$",
        "delivery_time": "20-30 min",
        "minimum_order": 15.00,
        "delivery_fee": 2.99,
        "is_open": True,
        "image_url": "https://example.com/chinatown-nyc.jpg"
    },
    {
        "id": "rest_038",
        "name": "Tokyo Sushi NYC",
        "cuisine": "Japanese",
        "location": {
            "address": "890 Madison Ave, New York, NY 10021",
            "city": "New York",
            "state": "NY",
            "zip": "10021",
            "lat": 40.7731,
            "lng": -73.9630
        },
        "rating": 4.7,
        "price_range": "$$$",
        "delivery_time": "28-38 min",
        "minimum_order": 25.00,
        "delivery_fee": 4.99,
        "is_open": True,
        "image_url": "https://example.com/tokyo-nyc.jpg"
    },
    {
        "id": "rest_039",
        "name": "K-Town BBQ NYC",
        "cuisine": "Korean",
        "location": {
            "address": "123 W 32nd St, New York, NY 10001",
            "city": "New York",
            "state": "NY",
            "zip": "10001",
            "lat": 40.7488,
            "lng": -73.9890
        },
        "rating": 4.6,
        "price_range": "$$",
        "delivery_time": "25-35 min",
        "minimum_order": 20.00,
        "delivery_fee": 3.99,
        "is_open": True,
        "image_url": "https://example.com/ktown-nyc.jpg"
    },
    {
        "id": "rest_040",
        "name": "Mediterranean Breeze NYC",
        "cuisine": "Mediterranean",
        "location": {
            "address": "456 Park Ave, New York, NY 10022",
            "city": "New York",
            "state": "NY",
            "zip": "10022",
            "lat": 40.7614,
            "lng": -73.9776
        },
        "rating": 4.5,
        "price_range": "$$$",
        "delivery_time": "30-40 min",
        "minimum_order": 24.00,
        "delivery_fee": 4.99,
        "is_open": True,
        "image_url": "https://example.com/med-breeze-nyc.jpg"
    },
    {
        "id": "rest_041",
        "name": "Cancun Cantina NYC",
        "cuisine": "Mexican",
        "location": {
            "address": "789 Broadway, New York, NY 10003",
            "city": "New York",
            "state": "NY",
            "zip": "10003",
            "lat": 40.7282,
            "lng": -73.9942
        },
        "rating": 4.4,
        "price_range": "$$",
        "delivery_time": "22-32 min",
        "minimum_order": 16.00,
        "delivery_fee": 3.49,
        "is_open": True,
        "image_url": "https://example.com/cancun-nyc.jpg"
    },
    {
        "id": "rest_042",
        "name": "Bangkok Street NYC",
        "cuisine": "Thai",
        "location": {
            "address": "234 E 53rd St, New York, NY 10022",
            "city": "New York",
            "state": "NY",
            "zip": "10022",
            "lat": 40.7573,
            "lng": -73.9714
        },
        "rating": 4.6,
        "price_range": "$$",
        "delivery_time": "24-34 min",
        "minimum_order": 18.00,
        "delivery_fee": 3.99,
        "is_open": True,
        "image_url": "https://example.com/bangkok-nyc.jpg"
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
    },
    "rest_009": {  # Spice Garden Indian Kitchen (Bangalore)
        "categories": [
            {
                "name": "Appetizers",
                "items": [
                    {
                        "id": "item_901",
                        "name": "Vegetable Samosa (2 pcs)",
                        "description": "Crispy pastry with spiced potato filling",
                        "price": 80.00,
                        "vegetarian": True,
                        "spicy": True
                    },
                    {
                        "id": "item_902",
                        "name": "Paneer Tikka",
                        "description": "Grilled cottage cheese with spices",
                        "price": 220.00,
                        "vegetarian": True,
                        "spicy": True,
                        "popular": True
                    }
                ]
            },
            {
                "name": "Main Course",
                "items": [
                    {
                        "id": "item_903",
                        "name": "Butter Chicken",
                        "description": "Tender chicken in creamy tomato sauce",
                        "price": 350.00,
                        "vegetarian": False,
                        "spicy": False,
                        "popular": True
                    },
                    {
                        "id": "item_904",
                        "name": "Paneer Butter Masala",
                        "description": "Cottage cheese in rich tomato gravy",
                        "price": 280.00,
                        "vegetarian": True,
                        "spicy": False,
                        "popular": True
                    },
                    {
                        "id": "item_905",
                        "name": "Dal Makhani",
                        "description": "Black lentils cooked overnight with cream",
                        "price": 220.00,
                        "vegetarian": True,
                        "spicy": False
                    }
                ]
            },
            {
                "name": "Breads",
                "items": [
                    {
                        "id": "item_906",
                        "name": "Butter Naan",
                        "description": "Soft leavened bread with butter",
                        "price": 50.00,
                        "vegetarian": True,
                        "spicy": False
                    },
                    {
                        "id": "item_907",
                        "name": "Garlic Naan",
                        "description": "Naan topped with garlic and herbs",
                        "price": 60.00,
                        "vegetarian": True,
                        "spicy": False
                    }
                ]
            }
        ]
    },
    "rest_010": {  # Bangalore Biryani House
        "categories": [
            {
                "name": "Biryani",
                "items": [
                    {
                        "id": "item_1001",
                        "name": "Hyderabadi Chicken Biryani",
                        "description": "Aromatic basmati rice with tender chicken",
                        "price": 280.00,
                        "vegetarian": False,
                        "spicy": True,
                        "popular": True
                    },
                    {
                        "id": "item_1002",
                        "name": "Mutton Biryani",
                        "description": "Flavorful rice with succulent mutton",
                        "price": 350.00,
                        "vegetarian": False,
                        "spicy": True,
                        "popular": True
                    },
                    {
                        "id": "item_1003",
                        "name": "Vegetable Biryani",
                        "description": "Mixed vegetables with fragrant rice",
                        "price": 220.00,
                        "vegetarian": True,
                        "spicy": True
                    }
                ]
            },
            {
                "name": "Sides",
                "items": [
                    {
                        "id": "item_1004",
                        "name": "Raita",
                        "description": "Yogurt with cucumber and spices",
                        "price": 60.00,
                        "vegetarian": True,
                        "spicy": False
                    },
                    {
                        "id": "item_1005",
                        "name": "Gulab Jamun (2 pcs)",
                        "description": "Sweet milk dumplings in sugar syrup",
                        "price": 80.00,
                        "vegetarian": True,
                        "spicy": False
                    }
                ]
            }
        ]
    },
    "rest_011": {  # Dosa Corner (Bangalore)
        "categories": [
            {
                "name": "Dosas",
                "items": [
                    {
                        "id": "item_1101",
                        "name": "Masala Dosa",
                        "description": "Crispy crepe with potato filling",
                        "price": 120.00,
                        "vegetarian": True,
                        "spicy": True,
                        "popular": True
                    },
                    {
                        "id": "item_1102",
                        "name": "Mysore Masala Dosa",
                        "description": "Spicy red chutney dosa with potato",
                        "price": 140.00,
                        "vegetarian": True,
                        "spicy": True,
                        "popular": True
                    },
                    {
                        "id": "item_1103",
                        "name": "Onion Rava Dosa",
                        "description": "Crispy semolina crepe with onions",
                        "price": 150.00,
                        "vegetarian": True,
                        "spicy": True
                    }
                ]
            },
            {
                "name": "Idli & Vada",
                "items": [
                    {
                        "id": "item_1104",
                        "name": "Idli (3 pcs)",
                        "description": "Steamed rice cakes with chutney",
                        "price": 80.00,
                        "vegetarian": True,
                        "spicy": False
                    },
                    {
                        "id": "item_1105",
                        "name": "Medu Vada (2 pcs)",
                        "description": "Crispy lentil donuts",
                        "price": 90.00,
                        "vegetarian": True,
                        "spicy": True
                    }
                ]
            }
        ]
    },
    "rest_012": {  # Manhattan Tandoor (New York)
        "categories": [
            {
                "name": "Appetizers",
                "items": [
                    {
                        "id": "item_1201",
                        "name": "Samosa (2 pieces)",
                        "description": "Crispy pastry filled with spiced potatoes",
                        "price": 6.99,
                        "vegetarian": True,
                        "spicy": True
                    },
                    {
                        "id": "item_1202",
                        "name": "Chicken Tikka",
                        "description": "Marinated chicken grilled in tandoor",
                        "price": 10.99,
                        "vegetarian": False,
                        "spicy": True
                    }
                ]
            },
            {
                "name": "Main Course",
                "items": [
                    {
                        "id": "item_1203",
                        "name": "Chicken Tikka Masala",
                        "description": "Grilled chicken in creamy tomato sauce",
                        "price": 17.99,
                        "vegetarian": False,
                        "spicy": True,
                        "popular": True
                    },
                    {
                        "id": "item_1204",
                        "name": "Butter Chicken",
                        "description": "Tender chicken in rich butter sauce",
                        "price": 17.99,
                        "vegetarian": False,
                        "spicy": False,
                        "popular": True
                    },
                    {
                        "id": "item_1205",
                        "name": "Lamb Vindaloo",
                        "description": "Spicy lamb curry with potatoes",
                        "price": 19.99,
                        "vegetarian": False,
                        "spicy": True
                    },
                    {
                        "id": "item_1206",
                        "name": "Paneer Tikka Masala",
                        "description": "Cottage cheese in creamy tomato sauce",
                        "price": 15.99,
                        "vegetarian": True,
                        "spicy": False
                    }
                ]
            },
            {
                "name": "Breads",
                "items": [
                    {
                        "id": "item_1207",
                        "name": "Garlic Naan",
                        "description": "Tandoor-baked bread with garlic",
                        "price": 3.99,
                        "vegetarian": True,
                        "spicy": False
                    },
                    {
                        "id": "item_1208",
                        "name": "Butter Naan",
                        "description": "Classic tandoor-baked flatbread",
                        "price": 2.99,
                        "vegetarian": True,
                        "spicy": False
                    }
                ]
            }
        ]
    },
    "rest_016": {  # Chicago Deep Dish Co
        "categories": [
            {
                "name": "Deep Dish Pizza",
                "items": [
                    {
                        "id": "item_501",
                        "name": "Classic Chicago Deep Dish",
                        "description": "Traditional deep dish with mozzarella, sausage, and chunky tomato sauce",
                        "price": 24.99,
                        "vegetarian": False,
                        "popular": True,
                        "image_url": "https://example.com/classic-deep-dish.jpg"
                    },
                    {
                        "id": "item_502",
                        "name": "Vegetarian Deep Dish",
                        "description": "Spinach, mushrooms, peppers, and mozzarella",
                        "price": 22.99,
                        "vegetarian": True,
                        "image_url": "https://example.com/veggie-deep-dish.jpg"
                    }
                ]
            }
        ]
    },
    "rest_017": {  # Windy City Tacos
        "categories": [
            {
                "name": "Tacos",
                "items": [
                    {
                        "id": "item_601",
                        "name": "Carne Asada Tacos",
                        "description": "Grilled steak with onions, cilantro, and lime",
                        "price": 12.99,
                        "vegetarian": False,
                        "spicy": True,
                        "popular": True
                    },
                    {
                        "id": "item_602",
                        "name": "Chicken Tacos",
                        "description": "Seasoned chicken with lettuce, cheese, and salsa",
                        "price": 10.99,
                        "vegetarian": False,
                        "spicy": True
                    },
                    {
                        "id": "item_603",
                        "name": "Veggie Tacos",
                        "description": "Black beans, corn, peppers, and avocado",
                        "price": 9.99,
                        "vegetarian": True
                    }
                ]
            },
            {
                "name": "Burritos",
                "items": [
                    {
                        "id": "item_604",
                        "name": "California Burrito",
                        "description": "Carne asada, fries, cheese, sour cream, and guacamole",
                        "price": 14.99,
                        "vegetarian": False,
                        "popular": True
                    }
                ]
            }
        ]
    },
    "rest_018": {  # Lake Shore Chinese
        "categories": [
            {
                "name": "Popular Dishes",
                "items": [
                    {
                        "id": "item_701",
                        "name": "General Tso's Chicken",
                        "description": "Crispy chicken in sweet and spicy sauce",
                        "price": 13.99,
                        "vegetarian": False,
                        "spicy": True,
                        "popular": True
                    },
                    {
                        "id": "item_702",
                        "name": "Beef and Broccoli",
                        "description": "Tender beef with fresh broccoli in brown sauce",
                        "price": 14.99,
                        "vegetarian": False
                    },
                    {
                        "id": "item_703",
                        "name": "Vegetable Fried Rice",
                        "description": "Wok-fried rice with mixed vegetables",
                        "price": 9.99,
                        "vegetarian": True
                    },
                    {
                        "id": "item_704",
                        "name": "Kung Pao Chicken",
                        "description": "Spicy chicken with peanuts and vegetables",
                        "price": 13.99,
                        "vegetarian": False,
                        "spicy": True
                    }
                ]
            }
        ]
    },
    "rest_019": {  # Chicago Tandoor
        "categories": [
            {
                "name": "Appetizers",
                "items": [
                    {
                        "id": "item_801",
                        "name": "Samosa (2 pieces)",
                        "description": "Crispy pastry filled with spiced potatoes and peas",
                        "price": 5.99,
                        "vegetarian": True,
                        "spicy": True
                    },
                    {
                        "id": "item_802",
                        "name": "Chicken Tikka",
                        "description": "Marinated chicken pieces grilled in tandoor",
                        "price": 9.99,
                        "vegetarian": False,
                        "spicy": True
                    }
                ]
            },
            {
                "name": "Main Course",
                "items": [
                    {
                        "id": "item_803",
                        "name": "Chicken Tikka Masala",
                        "description": "Grilled chicken in creamy tomato sauce",
                        "price": 15.99,
                        "vegetarian": False,
                        "spicy": True,
                        "popular": True
                    },
                    {
                        "id": "item_804",
                        "name": "Paneer Butter Masala",
                        "description": "Cottage cheese in rich tomato cream sauce",
                        "price": 14.99,
                        "vegetarian": True,
                        "spicy": False
                    },
                    {
                        "id": "item_805",
                        "name": "Chicken Biryani",
                        "description": "Fragrant basmati rice with spiced chicken",
                        "price": 16.99,
                        "vegetarian": False,
                        "spicy": True,
                        "popular": True
                    },
                    {
                        "id": "item_806",
                        "name": "Lamb Rogan Josh",
                        "description": "Tender lamb in aromatic curry sauce",
                        "price": 18.99,
                        "vegetarian": False,
                        "spicy": True
                    }
                ]
            },
            {
                "name": "Breads",
                "items": [
                    {
                        "id": "item_807",
                        "name": "Garlic Naan",
                        "description": "Tandoor-baked flatbread with garlic",
                        "price": 3.99,
                        "vegetarian": True,
                        "spicy": False
                    },
                    {
                        "id": "item_808",
                        "name": "Butter Naan",
                        "description": "Classic tandoor-baked flatbread with butter",
                        "price": 2.99,
                        "vegetarian": True,
                        "spicy": False
                    }
                ]
            }
        ]
    },
    "rest_020": {  # Placeholder for future expansion
        "categories": []
    },
    "rest_021": {  # Placeholder for future expansion
        "categories": []
    },
    "rest_022": {  # Placeholder for future expansion
        "categories": []
    },
    "rest_023": {  # Placeholder for future expansion
        "categories": []
    },
    "rest_024": {  # Placeholder for future expansion
        "categories": []
    },
    "rest_025": {  # Placeholder for future expansion
        "categories": []
    },
    "rest_026": {  # Placeholder for future expansion
        "categories": []
    },
    "rest_027": {  # Placeholder for future expansion
        "categories": []
    },
    "rest_028": {  # Placeholder for future expansion
        "categories": []
    },
    "rest_029": {  # Placeholder for future expansion
        "categories": []
    },
    "rest_030": {  # Placeholder for future expansion
        "categories": []
    },
    "rest_031": {  # Placeholder for future expansion
        "categories": []
    },
    "rest_032": {  # Placeholder for future expansion
        "categories": []
    },
    "rest_033": {  # Placeholder for future expansion
        "categories": []
    },
    "rest_034": {  # Placeholder for future expansion
        "categories": []
    },
    "rest_035": {  # Placeholder for future expansion
        "categories": []
    },
    "rest_036": {  # Placeholder for future expansion
        "categories": []
    },
    "rest_037": {  # Placeholder for future expansion
        "categories": []
    },
    "rest_038": {  # Placeholder for future expansion
        "categories": []
    },
    "rest_039": {  # Placeholder for future expansion
        "categories": []
    },
    "rest_040": {  # Placeholder for future expansion
        "categories": []
    },
    "rest_041": {  # Placeholder for future expansion
        "categories": []
    },
    "rest_042": {  # Placeholder for future expansion
        "categories": []
    },
    "rest_043": {  # Placeholder for future expansion
        "categories": []
    },
    "rest_044": {  # Placeholder for future expansion
        "categories": []
    },
    # === BANGALORE - New Restaurant Menus ===
    "rest_020": {  # Bangalore Wok (Chinese)
        "categories": [
            {
                "name": "Appetizers",
                "items": [
                    {"id": "item_2001", "name": "Spring Rolls (4 pcs)", "description": "Crispy vegetable spring rolls", "price": 6.99, "vegetarian": True, "spicy": False},
                    {"id": "item_2002", "name": "Chicken Dumplings (6 pcs)", "description": "Steamed chicken dumplings", "price": 8.99, "vegetarian": False, "spicy": False}
                ]
            },
            {
                "name": "Main Course",
                "items": [
                    {"id": "item_2003", "name": "Kung Pao Chicken", "description": "Spicy chicken with peanuts and vegetables", "price": 14.99, "vegetarian": False, "spicy": True, "popular": True},
                    {"id": "item_2004", "name": "Vegetable Fried Rice", "description": "Mixed vegetables with fried rice", "price": 11.99, "vegetarian": True, "spicy": False},
                    {"id": "item_2005", "name": "Beef with Broccoli", "description": "Tender beef in brown sauce", "price": 16.99, "vegetarian": False, "spicy": False}
                ]
            }
        ]
    },
    "rest_021": {  # Pasta Paradise Bangalore (Italian)
        "categories": [
            {
                "name": "Pasta",
                "items": [
                    {"id": "item_2101", "name": "Spaghetti Carbonara", "description": "Creamy pasta with bacon and eggs", "price": 15.99, "vegetarian": False, "spicy": False, "popular": True},
                    {"id": "item_2102", "name": "Penne Arrabbiata", "description": "Spicy tomato sauce pasta", "price": 13.99, "vegetarian": True, "spicy": True},
                    {"id": "item_2103", "name": "Lasagna", "description": "Layered pasta with meat sauce", "price": 17.99, "vegetarian": False, "spicy": False}
                ]
            },
            {
                "name": "Pizza",
                "items": [
                    {"id": "item_2104", "name": "Margherita Pizza", "description": "Classic tomato and mozzarella", "price": 14.99, "vegetarian": True, "spicy": False, "popular": True}
                ]
            }
        ]
    },
    "rest_022": {  # Sakura Sushi Bangalore (Japanese)
        "categories": [
            {
                "name": "Sushi Rolls",
                "items": [
                    {"id": "item_2201", "name": "California Roll", "description": "Crab, avocado, cucumber", "price": 12.99, "vegetarian": False, "spicy": False, "popular": True},
                    {"id": "item_2202", "name": "Spicy Tuna Roll", "description": "Tuna with spicy mayo", "price": 14.99, "vegetarian": False, "spicy": True},
                    {"id": "item_2203", "name": "Vegetable Roll", "description": "Assorted fresh vegetables", "price": 10.99, "vegetarian": True, "spicy": False}
                ]
            },
            {
                "name": "Main Dishes",
                "items": [
                    {"id": "item_2204", "name": "Chicken Teriyaki", "description": "Grilled chicken with teriyaki sauce", "price": 16.99, "vegetarian": False, "spicy": False}
                ]
            }
        ]
    },
    "rest_023": {  # Seoul Kitchen Bangalore (Korean)
        "categories": [
            {
                "name": "Main Dishes",
                "items": [
                    {"id": "item_2301", "name": "Bibimbap", "description": "Mixed rice bowl with vegetables and egg", "price": 15.99, "vegetarian": False, "spicy": True, "popular": True},
                    {"id": "item_2302", "name": "Korean BBQ Beef", "description": "Marinated beef bulgogi", "price": 19.99, "vegetarian": False, "spicy": True},
                    {"id": "item_2303", "name": "Kimchi Fried Rice", "description": "Spicy fermented cabbage rice", "price": 13.99, "vegetarian": True, "spicy": True}
                ]
            }
        ]
    },
    "rest_024": {  # Mediterranean Oasis Bangalore
        "categories": [
            {
                "name": "Main Dishes",
                "items": [
                    {"id": "item_2401", "name": "Falafel Wrap", "description": "Crispy chickpea balls in warm pita", "price": 12.99, "vegetarian": True, "spicy": False, "popular": True},
                    {"id": "item_2402", "name": "Lamb Gyro", "description": "Grilled lamb in pita bread", "price": 16.99, "vegetarian": False, "spicy": False},
                    {"id": "item_2403", "name": "Greek Salad", "description": "Fresh vegetables with feta cheese", "price": 10.99, "vegetarian": True, "spicy": False}
                ]
            }
        ]
    },
    "rest_025": {  # Bangalore Fiesta (Mexican)
        "categories": [
            {
                "name": "Main Dishes",
                "items": [
                    {"id": "item_2501", "name": "Chicken Burrito", "description": "Rice, beans, chicken, cheese wrapped in tortilla", "price": 12.99, "vegetarian": False, "spicy": True, "popular": True},
                    {"id": "item_2502", "name": "Beef Tacos (3 pcs)", "description": "Soft shell tacos with seasoned beef", "price": 11.99, "vegetarian": False, "spicy": True},
                    {"id": "item_2503", "name": "Vegetarian Quesadilla", "description": "Cheese and vegetables in grilled tortilla", "price": 10.99, "vegetarian": True, "spicy": False}
                ]
            }
        ]
    },
    "rest_026": {  # Thai Spice Bangalore
        "categories": [
            {
                "name": "Main Dishes",
                "items": [
                    {"id": "item_2601", "name": "Pad Thai", "description": "Stir-fried noodles with shrimp and peanuts", "price": 14.99, "vegetarian": False, "spicy": True, "popular": True},
                    {"id": "item_2602", "name": "Green Curry", "description": "Thai green curry with chicken", "price": 15.99, "vegetarian": False, "spicy": True},
                    {"id": "item_2603", "name": "Vegetable Spring Rolls (4 pcs)", "description": "Fresh vegetables in rice paper", "price": 8.99, "vegetarian": True, "spicy": False}
                ]
            }
        ]
    },
    # === CHICAGO - New Restaurant Menus ===
    "rest_027": {  # Tokyo Express Chicago (Japanese)
        "categories": [
            {
                "name": "Sushi",
                "items": [
                    {"id": "item_2701", "name": "Rainbow Roll", "description": "Assorted fish on California roll", "price": 18.99, "vegetarian": False, "spicy": False, "popular": True},
                    {"id": "item_2702", "name": "Dragon Roll", "description": "Eel and avocado", "price": 16.99, "vegetarian": False, "spicy": False}
                ]
            },
            {
                "name": "Main Dishes",
                "items": [
                    {"id": "item_2703", "name": "Beef Teriyaki", "description": "Grilled beef with teriyaki glaze", "price": 19.99, "vegetarian": False, "spicy": False}
                ]
            }
        ]
    },
    "rest_028": {  # Seoul BBQ Chicago (Korean)
        "categories": [
            {
                "name": "Main Dishes",
                "items": [
                    {"id": "item_2801", "name": "Korean BBQ Platter", "description": "Assorted grilled meats with sides", "price": 24.99, "vegetarian": False, "spicy": True, "popular": True},
                    {"id": "item_2802", "name": "Japchae", "description": "Stir-fried glass noodles with vegetables", "price": 14.99, "vegetarian": True, "spicy": False},
                    {"id": "item_2803", "name": "Spicy Pork Bulgogi", "description": "Marinated spicy pork", "price": 17.99, "vegetarian": False, "spicy": True}
                ]
            }
        ]
    },
    "rest_029": {  # Greek Islands Chicago (Mediterranean)
        "categories": [
            {
                "name": "Main Dishes",
                "items": [
                    {"id": "item_2901", "name": "Souvlaki Platter", "description": "Grilled meat skewers with rice and salad", "price": 18.99, "vegetarian": False, "spicy": False, "popular": True},
                    {"id": "item_2902", "name": "Moussaka", "description": "Layered eggplant and meat casserole", "price": 17.99, "vegetarian": False, "spicy": False},
                    {"id": "item_2903", "name": "Hummus Platter", "description": "Hummus with pita and vegetables", "price": 11.99, "vegetarian": True, "spicy": False}
                ]
            }
        ]
    },
    "rest_030": {  # Thai Elephant Chicago
        "categories": [
            {
                "name": "Main Dishes",
                "items": [
                    {"id": "item_3001", "name": "Massaman Curry", "description": "Rich curry with potatoes and peanuts", "price": 16.99, "vegetarian": False, "spicy": True, "popular": True},
                    {"id": "item_3002", "name": "Tom Yum Soup", "description": "Spicy and sour Thai soup", "price": 12.99, "vegetarian": False, "spicy": True},
                    {"id": "item_3003", "name": "Basil Fried Rice", "description": "Thai basil fried rice", "price": 13.99, "vegetarian": True, "spicy": True}
                ]
            }
        ]
    },
    # === LOS ANGELES - New Restaurant Menus ===
    "rest_031": {  # Golden Dragon LA (Chinese)
        "categories": [
            {
                "name": "Main Course",
                "items": [
                    {"id": "item_3101", "name": "General Tso's Chicken", "description": "Sweet and spicy fried chicken", "price": 15.99, "vegetarian": False, "spicy": True, "popular": True},
                    {"id": "item_3102", "name": "Mongolian Beef", "description": "Beef with scallions in brown sauce", "price": 17.99, "vegetarian": False, "spicy": False},
                    {"id": "item_3103", "name": "Mapo Tofu", "description": "Spicy tofu with ground pork", "price": 13.99, "vegetarian": False, "spicy": True}
                ]
            }
        ]
    },
    "rest_032": {  # Bollywood Bites LA (Indian)
        "categories": [
            {
                "name": "Main Course",
                "items": [
                    {"id": "item_3201", "name": "Chicken Tikka Masala", "description": "Grilled chicken in creamy tomato sauce", "price": 17.99, "vegetarian": False, "spicy": True, "popular": True},
                    {"id": "item_3202", "name": "Lamb Rogan Josh", "description": "Tender lamb in aromatic curry", "price": 19.99, "vegetarian": False, "spicy": True},
                    {"id": "item_3203", "name": "Palak Paneer", "description": "Spinach curry with cottage cheese", "price": 14.99, "vegetarian": True, "spicy": False}
                ]
            }
        ]
    },
    "rest_033": {  # Venice Italian Kitchen
        "categories": [
            {
                "name": "Pasta & Pizza",
                "items": [
                    {"id": "item_3301", "name": "Fettuccine Alfredo", "description": "Creamy parmesan pasta", "price": 16.99, "vegetarian": True, "spicy": False, "popular": True},
                    {"id": "item_3302", "name": "Pepperoni Pizza", "description": "Classic pepperoni pizza", "price": 15.99, "vegetarian": False, "spicy": False},
                    {"id": "item_3303", "name": "Seafood Linguine", "description": "Pasta with mixed seafood", "price": 21.99, "vegetarian": False, "spicy": False}
                ]
            }
        ]
    },
    "rest_034": {  # Seoul Station LA (Korean)
        "categories": [
            {
                "name": "Main Dishes",
                "items": [
                    {"id": "item_3401", "name": "Korean Fried Chicken", "description": "Crispy fried chicken with gochujang sauce", "price": 16.99, "vegetarian": False, "spicy": True, "popular": True},
                    {"id": "item_3402", "name": "Bibimbap Bowl", "description": "Rice bowl with vegetables and beef", "price": 15.99, "vegetarian": False, "spicy": True},
                    {"id": "item_3403", "name": "Tofu Stew", "description": "Spicy soft tofu soup", "price": 13.99, "vegetarian": True, "spicy": True}
                ]
            }
        ]
    },
    "rest_035": {  # Santorini Grill LA (Mediterranean)
        "categories": [
            {
                "name": "Main Dishes",
                "items": [
                    {"id": "item_3501", "name": "Shawarma Platter", "description": "Chicken shawarma with rice and salad", "price": 17.99, "vegetarian": False, "spicy": False, "popular": True},
                    {"id": "item_3502", "name": "Grilled Halloumi", "description": "Grilled cheese with vegetables", "price": 14.99, "vegetarian": True, "spicy": False},
                    {"id": "item_3503", "name": "Lamb Kebab", "description": "Grilled lamb skewers", "price": 20.99, "vegetarian": False, "spicy": False}
                ]
            }
        ]
    },
    "rest_036": {  # Thai Town LA
        "categories": [
            {
                "name": "Main Dishes",
                "items": [
                    {"id": "item_3601", "name": "Pad See Ew", "description": "Stir-fried wide noodles", "price": 14.99, "vegetarian": False, "spicy": False, "popular": True},
                    {"id": "item_3602", "name": "Red Curry", "description": "Spicy red curry with chicken", "price": 15.99, "vegetarian": False, "spicy": True},
                    {"id": "item_3603", "name": "Mango Sticky Rice", "description": "Sweet mango with coconut rice", "price": 8.99, "vegetarian": True, "spicy": False}
                ]
            }
        ]
    },
    # === NEW YORK - New Restaurant Menus ===
    "rest_037": {  # Chinatown Express NYC (Chinese)
        "categories": [
            {
                "name": "Main Course",
                "items": [
                    {"id": "item_3701", "name": "Sweet and Sour Pork", "description": "Crispy pork in sweet and sour sauce", "price": 14.99, "vegetarian": False, "spicy": False, "popular": True},
                    {"id": "item_3702", "name": "Szechuan Beef", "description": "Spicy beef with chili peppers", "price": 16.99, "vegetarian": False, "spicy": True},
                    {"id": "item_3703", "name": "Buddha's Delight", "description": "Mixed vegetables in garlic sauce", "price": 12.99, "vegetarian": True, "spicy": False}
                ]
            }
        ]
    },
    "rest_038": {  # Tokyo Sushi NYC (Japanese)
        "categories": [
            {
                "name": "Premium Sushi",
                "items": [
                    {"id": "item_3801", "name": "Omakase Roll", "description": "Chef's special selection", "price": 24.99, "vegetarian": False, "spicy": False, "popular": True},
                    {"id": "item_3802", "name": "Volcano Roll", "description": "Spicy tuna with baked topping", "price": 18.99, "vegetarian": False, "spicy": True},
                    {"id": "item_3803", "name": "Salmon Sashimi", "description": "Fresh raw salmon slices", "price": 19.99, "vegetarian": False, "spicy": False}
                ]
            }
        ]
    },
    "rest_039": {  # K-Town BBQ NYC (Korean)
        "categories": [
            {
                "name": "Main Dishes",
                "items": [
                    {"id": "item_3901", "name": "Korean BBQ Combo", "description": "Mixed meats with banchan", "price": 26.99, "vegetarian": False, "spicy": True, "popular": True},
                    {"id": "item_3902", "name": "Seafood Pancake", "description": "Crispy pancake with seafood", "price": 14.99, "vegetarian": False, "spicy": False},
                    {"id": "item_3903", "name": "Spicy Tofu Soup", "description": "Soft tofu in spicy broth", "price": 13.99, "vegetarian": True, "spicy": True}
                ]
            }
        ]
    },
    "rest_040": {  # Mediterranean Breeze NYC
        "categories": [
            {
                "name": "Main Dishes",
                "items": [
                    {"id": "item_4001", "name": "Mixed Grill Platter", "description": "Assorted grilled meats", "price": 22.99, "vegetarian": False, "spicy": False, "popular": True},
                    {"id": "item_4002", "name": "Falafel Bowl", "description": "Falafel with hummus and salad", "price": 14.99, "vegetarian": True, "spicy": False},
                    {"id": "item_4003", "name": "Grilled Octopus", "description": "Tender grilled octopus", "price": 23.99, "vegetarian": False, "spicy": False}
                ]
            }
        ]
    },
    "rest_041": {  # Cancun Cantina NYC (Mexican)
        "categories": [
            {
                "name": "Main Dishes",
                "items": [
                    {"id": "item_4101", "name": "Carnitas Bowl", "description": "Slow-cooked pork with rice and beans", "price": 14.99, "vegetarian": False, "spicy": True, "popular": True},
                    {"id": "item_4102", "name": "Chicken Enchiladas", "description": "Rolled tortillas with chicken and sauce", "price": 13.99, "vegetarian": False, "spicy": True},
                    {"id": "item_4103", "name": "Veggie Fajitas", "description": "Sizzling vegetables with tortillas", "price": 12.99, "vegetarian": True, "spicy": False}
                ]
            }
        ]
    },
    "rest_042": {  # Bangkok Street NYC (Thai)
        "categories": [
            {
                "name": "Main Dishes",
                "items": [
                    {"id": "item_4201", "name": "Drunken Noodles", "description": "Spicy stir-fried noodles with basil", "price": 15.99, "vegetarian": False, "spicy": True, "popular": True},
                    {"id": "item_4202", "name": "Panang Curry", "description": "Rich peanut curry with chicken", "price": 16.99, "vegetarian": False, "spicy": True},
                    {"id": "item_4203", "name": "Thai Iced Tea", "description": "Sweet Thai tea with milk", "price": 4.99, "vegetarian": True, "spicy": False}
                ]
            }
        ]
    },
    "rest_045": {  # Placeholder for future expansion
        "categories": []
    },
    "rest_046": {  # Placeholder for future expansion
        "categories": []
    },
    "rest_047": {  # Placeholder for future expansion
        "categories": []
    },
    "rest_048": {  # Placeholder for future expansion
        "categories": []
    },
    "rest_049": {  # Placeholder for future expansion
        "categories": []
    },
    "rest_050": {  # Placeholder for future expansion
        "categories": []
    }
}

# Mock orders storage
MOCK_ORDERS = {}

# User favorites storage
USER_FAVORITES = {
    "restaurants": set(),
    "items": []
}

def add_favorite_restaurant(restaurant_id: str):
    """Add a restaurant to user favorites"""
    USER_FAVORITES["restaurants"].add(restaurant_id)

def get_favorite_restaurants():
    """Get list of favorite restaurants"""
    return list(USER_FAVORITES["restaurants"])

def remove_favorite_restaurant(restaurant_id: str):
    """Remove a restaurant from favorites"""
    USER_FAVORITES["restaurants"].discard(restaurant_id)

def add_favorite_item(restaurant_id: str, item_id: str, item_name: str):
    """Add a menu item to favorites"""
    favorite = {
        "restaurant_id": restaurant_id,
        "item_id": item_id,
        "item_name": item_name
    }
    # Remove if already exists
    USER_FAVORITES["items"] = [f for f in USER_FAVORITES["items"] 
                                if not (f["restaurant_id"] == restaurant_id and f["item_id"] == item_id)]
    USER_FAVORITES["items"].append(favorite)

def get_favorite_items():
    """Get list of favorite items"""
    return USER_FAVORITES["items"]

def remove_favorite_item(restaurant_id: str, item_id: str):
    """Remove an item from favorites"""
    USER_FAVORITES["items"] = [f for f in USER_FAVORITES["items"] 
                                if not (f["restaurant_id"] == restaurant_id and f["item_id"] == item_id)]

# Mock Orders Storage (in-memory)
MOCK_ORDERS = {}

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
    order_id = f"order_{len(MOCK_ORDERS) + 1:04d}"
    
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
    
    MOCK_ORDERS[order_id] = order
    return order

def get_order_by_id(order_id: str):
    """Get order by ID"""
    return MOCK_ORDERS.get(order_id)

def update_order_status(order_id: str, status: str):
    """Update order status"""
    if order_id in MOCK_ORDERS:
        MOCK_ORDERS[order_id]["status"] = status
        MOCK_ORDERS[order_id]["updated_at"] = datetime.now().isoformat()
        return MOCK_ORDERS[order_id]
    return None

def process_payment(order_id: str, payment_method: dict):
    """Process payment for an order"""
    if order_id in MOCK_ORDERS:
        MOCK_ORDERS[order_id]["payment_status"] = "completed"
        MOCK_ORDERS[order_id]["payment_method"] = payment_method
        MOCK_ORDERS[order_id]["status"] = "confirmed"
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

