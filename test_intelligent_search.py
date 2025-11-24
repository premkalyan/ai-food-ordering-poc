#!/usr/bin/env python3
"""
Quick test script for intelligent search logic
Tests the parsing and filtering without running the full server
"""

import time
from mock_data import RESTAURANTS, MENUS, CUISINES

# Simple ParsedQuery class
class ParsedQuery:
    def __init__(self):
        self.cuisine = None
        self.dish = None
        self.price_max = None
        self.delivery_time_max = None
        self.preferences = []
        self.is_favorite = False
        self.is_urgent = False

def parse_query(query: str, location: str):
    """Parse natural language query"""
    query_lower = query.lower()
    parsed = ParsedQuery()
    
    # Extract Cuisine
    for c in CUISINES:
        if c.lower() in query_lower:
            parsed.cuisine = c
            break
    
    # Extract Dish (simplified)
    dishes = {
        "tandoori chicken": "Tandoori Chicken",
        "butter chicken": "Butter Chicken",
        "pizza": "Pizza",
        "sushi": "Sushi",
        "tacos": "Tacos",
        "pasta": "Pasta"
    }
    for dish_key, dish_name in dishes.items():
        if dish_key in query_lower:
            parsed.dish = dish_name
            break
    
    # Extract Price
    import re
    price_match = re.search(r'(?:under|below|\$)\s*(\d+)', query_lower)
    if price_match:
        parsed.price_max = float(price_match.group(1))
    
    # Extract Delivery Time
    time_match = re.search(r'(\d+)\s*min(?:utes)?', query_lower)
    if time_match:
        parsed.delivery_time_max = int(time_match.group(1))
    elif any(word in query_lower for word in ["fast", "quick", "asap", "urgent"]):
        parsed.is_urgent = True
        parsed.delivery_time_max = 20
    
    # Extract Preferences
    if "spicy" in query_lower:
        parsed.preferences.append("spicy")
    if "vegetarian" in query_lower:
        parsed.preferences.append("vegetarian")
    
    # Check for favorites
    if any(word in query_lower for word in ["favorite", "usual", "regular"]):
        parsed.is_favorite = True
    
    return parsed

def filter_restaurants(parsed: ParsedQuery, location: str):
    """Filter restaurants based on parsed query"""
    # Get restaurants in location
    filtered = [r for r in RESTAURANTS if r["city"] == location]
    
    # Filter by cuisine
    if parsed.cuisine:
        filtered = [r for r in filtered if r["cuisine"].lower() == parsed.cuisine.lower()]
    
    # Filter by delivery time
    if parsed.delivery_time_max:
        result = []
        for r in filtered:
            try:
                min_time = int(r["delivery_time"].split('-')[0].strip())
                if min_time <= parsed.delivery_time_max:
                    result.append(r)
            except:
                pass
        filtered = result
    
    return filtered

def test_query(query: str, location: str = "San Francisco"):
    """Test a single query"""
    print(f"\n{'='*80}")
    print(f"QUERY: {query}")
    print(f"LOCATION: {location}")
    print(f"{'='*80}")
    
    start = time.time()
    
    # Parse
    parsed = parse_query(query, location)
    print(f"\nPARSED:")
    print(f"  Cuisine: {parsed.cuisine}")
    print(f"  Dish: {parsed.dish}")
    print(f"  Price Max: ${parsed.price_max}" if parsed.price_max else "  Price Max: None")
    print(f"  Delivery Time Max: {parsed.delivery_time_max} min" if parsed.delivery_time_max else "  Delivery Time Max: None")
    print(f"  Preferences: {', '.join(parsed.preferences)}" if parsed.preferences else "  Preferences: None")
    print(f"  Is Favorite: {parsed.is_favorite}")
    print(f"  Is Urgent: {parsed.is_urgent}")
    
    # Filter
    filtered = filter_restaurants(parsed, location)
    print(f"\nRESULTS: {len(filtered)} restaurants found")
    
    for i, r in enumerate(filtered[:3], 1):
        print(f"\n  {i}. {r['name']}")
        print(f"     Cuisine: {r['cuisine']}")
        print(f"     Delivery: {r['delivery_time']}")
        print(f"     Rating: {r['rating']}")
    
    elapsed = time.time() - start
    print(f"\nTIME: {elapsed:.3f}s")
    
    if elapsed > 30:
        print("❌ FAILED: Took more than 30 seconds!")
        return False
    else:
        print("✅ PASSED: Response time acceptable")
        return True

if __name__ == "__main__":
    print("Testing Intelligent Search Logic")
    print("Target: <30 seconds response time\n")
    
    # Test cases
    tests = [
        ("I want tandoori chicken from an Indian restaurant", "San Francisco"),
        ("Get me something spicy under $15", "San Francisco"),
        ("I am hungry, get me something that can reach me in 15 minutes", "San Francisco"),
        ("I want to eat Italian food in $20", "New York"),
        ("Order pizza from my favorite restaurant", "San Francisco"),
    ]
    
    results = []
    for query, location in tests:
        results.append(test_query(query, location))
    
    print(f"\n{'='*80}")
    print(f"SUMMARY: {sum(results)}/{len(results)} tests passed")
    print(f"{'='*80}")

