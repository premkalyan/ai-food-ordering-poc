"""
Test script for the Food Ordering API
Run this to verify all endpoints are working correctly
"""

import requests
import json
from typing import Dict, Any

BASE_URL = "http://localhost:8000"

def print_response(title: str, response: requests.Response):
    """Pretty print API response"""
    print(f"\n{'='*60}")
    print(f"TEST: {title}")
    print(f"{'='*60}")
    print(f"Status Code: {response.status_code}")
    print(f"Response:")
    print(json.dumps(response.json(), indent=2))

def test_health_check():
    """Test health check endpoint"""
    response = requests.get(f"{BASE_URL}/health")
    print_response("Health Check", response)
    return response.status_code == 200

def test_get_cuisines():
    """Test get cuisines endpoint"""
    response = requests.get(f"{BASE_URL}/api/v1/cuisines")
    print_response("Get Available Cuisines", response)
    return response.status_code == 200

def test_search_restaurants():
    """Test restaurant search"""
    # Test 1: Search by cuisine
    response = requests.get(
        f"{BASE_URL}/api/v1/restaurants/search",
        params={"cuisine": "Indian"}
    )
    print_response("Search Restaurants - Indian Cuisine", response)
    
    # Test 2: Search by city
    response = requests.get(
        f"{BASE_URL}/api/v1/restaurants/search",
        params={"city": "San Francisco"}
    )
    print_response("Search Restaurants - San Francisco", response)
    
    return response.status_code == 200

def test_get_restaurant():
    """Test get restaurant details"""
    restaurant_id = "rest_001"
    response = requests.get(f"{BASE_URL}/api/v1/restaurants/{restaurant_id}")
    print_response(f"Get Restaurant Details - {restaurant_id}", response)
    return response.status_code == 200

def test_get_menu():
    """Test get restaurant menu"""
    restaurant_id = "rest_001"
    response = requests.get(f"{BASE_URL}/api/v1/restaurants/{restaurant_id}/menu")
    print_response(f"Get Menu - {restaurant_id}", response)
    return response.status_code == 200

def test_create_order():
    """Test order creation"""
    order_data = {
        "restaurant_id": "rest_001",
        "items": [
            {
                "item_id": "item_003",
                "name": "Paneer Butter Masala",
                "price": 14.99,
                "quantity": 1,
                "special_instructions": "Extra spicy"
            },
            {
                "item_id": "item_006",
                "name": "Garlic Naan",
                "price": 3.99,
                "quantity": 2
            }
        ],
        "delivery_address": {
            "address": "123 Main St, Apt 4B",
            "city": "San Francisco",
            "state": "CA",
            "zip": "94102"
        },
        "special_instructions": "Please ring doorbell"
    }
    
    response = requests.post(
        f"{BASE_URL}/api/v1/orders/create",
        json=order_data
    )
    print_response("Create Order", response)
    
    if response.status_code == 200:
        return response.json()["id"]
    return None

def test_get_order(order_id: str):
    """Test get order status"""
    response = requests.get(f"{BASE_URL}/api/v1/orders/{order_id}")
    print_response(f"Get Order Status - {order_id}", response)
    return response.status_code == 200

def test_process_payment(order_id: str):
    """Test payment processing"""
    payment_data = {
        "payment_method": {
            "type": "credit_card",
            "last_four": "4242"
        }
    }
    
    response = requests.post(
        f"{BASE_URL}/api/v1/orders/{order_id}/payment",
        json=payment_data
    )
    print_response(f"Process Payment - {order_id}", response)
    return response.status_code == 200

def test_complete_order_flow():
    """Test complete order flow from search to payment"""
    print("\n" + "="*60)
    print("COMPLETE ORDER FLOW TEST")
    print("="*60)
    
    # 1. Search restaurants
    print("\n1. Searching for Indian restaurants...")
    response = requests.get(
        f"{BASE_URL}/api/v1/restaurants/search",
        params={"cuisine": "Indian"}
    )
    restaurants = response.json()
    print(f"   Found {len(restaurants)} restaurants")
    
    if not restaurants:
        print("   ❌ No restaurants found")
        return False
    
    restaurant = restaurants[0]
    print(f"   ✓ Selected: {restaurant['name']}")
    
    # 2. Get menu
    print(f"\n2. Getting menu for {restaurant['name']}...")
    response = requests.get(f"{BASE_URL}/api/v1/restaurants/{restaurant['id']}/menu")
    menu = response.json()
    total_items = sum(len(cat['items']) for cat in menu['categories'])
    print(f"   ✓ Menu loaded: {len(menu['categories'])} categories, {total_items} items")
    
    # 3. Create order
    print("\n3. Creating order...")
    order_data = {
        "restaurant_id": restaurant['id'],
        "items": [
            {
                "item_id": "item_003",
                "name": "Paneer Butter Masala",
                "price": 14.99,
                "quantity": 1
            },
            {
                "item_id": "item_006",
                "name": "Garlic Naan",
                "price": 3.99,
                "quantity": 2
            }
        ],
        "delivery_address": {
            "address": "123 Main St",
            "city": "San Francisco",
            "state": "CA",
            "zip": "94102"
        }
    }
    
    response = requests.post(f"{BASE_URL}/api/v1/orders/create", json=order_data)
    order = response.json()
    print(f"   ✓ Order created: {order['id']}")
    print(f"   ✓ Total: ${order['total']}")
    
    # 4. Process payment
    print("\n4. Processing payment...")
    payment_data = {
        "payment_method": {
            "type": "credit_card",
            "last_four": "4242"
        }
    }
    
    response = requests.post(
        f"{BASE_URL}/api/v1/orders/{order['id']}/payment",
        json=payment_data
    )
    payment_result = response.json()
    print(f"   ✓ Payment successful: {payment_result['transaction_id']}")
    
    # 5. Check order status
    print("\n5. Checking order status...")
    response = requests.get(f"{BASE_URL}/api/v1/orders/{order['id']}")
    updated_order = response.json()
    print(f"   ✓ Order status: {updated_order['status']}")
    print(f"   ✓ Payment status: {updated_order['payment_status']}")
    print(f"   ✓ Estimated delivery: {updated_order['estimated_delivery']}")
    
    print("\n" + "="*60)
    print("✓ COMPLETE ORDER FLOW TEST PASSED")
    print("="*60)
    
    return True

def run_all_tests():
    """Run all API tests"""
    print("\n" + "="*60)
    print("FOOD ORDERING API - TEST SUITE")
    print("="*60)
    
    tests = [
        ("Health Check", test_health_check),
        ("Get Cuisines", test_get_cuisines),
        ("Search Restaurants", test_search_restaurants),
        ("Get Restaurant Details", test_get_restaurant),
        ("Get Menu", test_get_menu),
    ]
    
    results = []
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"\n❌ {test_name} failed with error: {str(e)}")
            results.append((test_name, False))
    
    # Test order flow
    try:
        order_id = test_create_order()
        if order_id:
            test_get_order(order_id)
            test_process_payment(order_id)
            results.append(("Order Flow", True))
        else:
            results.append(("Order Flow", False))
    except Exception as e:
        print(f"\n❌ Order flow failed with error: {str(e)}")
        results.append(("Order Flow", False))
    
    # Test complete flow
    try:
        complete_flow_result = test_complete_order_flow()
        results.append(("Complete Flow", complete_flow_result))
    except Exception as e:
        print(f"\n❌ Complete flow failed with error: {str(e)}")
        results.append(("Complete Flow", False))
    
    # Print summary
    print("\n" + "="*60)
    print("TEST SUMMARY")
    print("="*60)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for test_name, result in results:
        status = "✓ PASS" if result else "❌ FAIL"
        print(f"{status} - {test_name}")
    
    print(f"\n{passed}/{total} tests passed")
    
    if passed == total:
        print("\n🎉 All tests passed! API is ready for ChatGPT integration.")
    else:
        print("\n⚠️  Some tests failed. Please check the errors above.")
    
    return passed == total

if __name__ == "__main__":
    try:
        run_all_tests()
    except requests.exceptions.ConnectionError:
        print("\n❌ ERROR: Cannot connect to API")
        print("Make sure the API is running:")
        print("  python main.py")
        print(f"\nExpected API at: {BASE_URL}")

