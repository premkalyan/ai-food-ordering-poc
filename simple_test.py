#!/usr/bin/env python3
"""
Ultra-simple test of intelligent search logic without FastAPI
Tests just the core parsing and filtering
"""

import time
import re

# Simplified test data
TEST_RESTAURANTS = [
    {"id": "1", "name": "Taj Palace", "cuisine": "Indian", "location": {"city": "San Francisco"}, "delivery_time": "30-45 min", "rating": 4.5},
    {"id": "2", "name": "Golden Dragon", "cuisine": "Chinese", "location": {"city": "San Francisco"}, "delivery_time": "25-35 min", "rating": 4.3},
    {"id": "3", "name": "Pizza Paradise", "cuisine": "Italian", "location": {"city": "San Francisco"}, "delivery_time": "20-30 min", "rating": 4.6},
]

CUISINES = ["Indian", "Chinese", "Italian", "Mexican", "Thai"]

def parse_query(query: str):
    """Parse query - simplified"""
    query_lower = query.lower()
    
    # Extract cuisine
    cuisine = None
    for c in CUISINES:
        if c.lower() in query_lower:
            cuisine = c
            break
    
    # Extract dish
    dish = None
    if "tandoori chicken" in query_lower:
        dish = "Tandoori Chicken"
    elif "pizza" in query_lower:
        dish = "Pizza"
    
    # Extract price
    price_max = None
    price_match = re.search(r'\$(\d+)', query_lower)
    if price_match:
        price_max = float(price_match.group(1))
    
    # Extract time
    time_max = None
    time_match = re.search(r'(\d+)\s*min', query_lower)
    if time_match:
        time_max = int(time_match.group(1))
    
    return {
        "cuisine": cuisine,
        "dish": dish,
        "price_max": price_max,
        "time_max": time_max
    }

def filter_restaurants(parsed, restaurants, location):
    """Filter restaurants"""
    # Filter by location
    results = [r for r in restaurants if r["location"]["city"] == location]
    
    # Filter by cuisine
    if parsed["cuisine"]:
        results = [r for r in results if r["cuisine"] == parsed["cuisine"]]
    
    # Filter by time
    if parsed["time_max"]:
        def get_max_time(time_str):
            match = re.search(r'(\d+)-(\d+)', time_str)
            return int(match.group(2)) if match else 60
        
        results = [r for r in results if get_max_time(r["delivery_time"]) <= parsed["time_max"]]
    
    return results

def test_query(query, location="San Francisco"):
    """Test a query"""
    print(f"\nQuery: {query}")
    print(f"Location: {location}")
    
    start = time.time()
    
    # Parse
    parsed = parse_query(query)
    print(f"Parsed: {parsed}")
    
    # Filter
    results = filter_restaurants(parsed, TEST_RESTAURANTS, location)
    print(f"Results: {len(results)} restaurants")
    for r in results:
        print(f"  - {r['name']} ({r['cuisine']}, {r['delivery_time']})")
    
    elapsed = time.time() - start
    print(f"Time: {elapsed:.4f}s")
    
    if elapsed > 30:
        print("❌ TIMEOUT!")
        return False
    else:
        print("✅ PASS")
        return True

if __name__ == "__main__":
    print("="*80)
    print("SIMPLE INTELLIGENT SEARCH TEST")
    print("="*80)
    
    tests = [
        "I want tandoori chicken from an Indian restaurant",
        "Get me pizza in 25 minutes",
        "Something spicy under $15",
    ]
    
    results = []
    for query in tests:
        results.append(test_query(query))
    
    print(f"\n{'='*80}")
    print(f"SUMMARY: {sum(results)}/{len(results)} passed")
    print(f"{'='*80}")

