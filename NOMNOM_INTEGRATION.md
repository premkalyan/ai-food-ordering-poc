# Nomnom API Integration Guide

## Overview
This document outlines the integration path from our mock API to the real Nomnom platform.

## Current Architecture (Mock)

```
ChatGPT Custom GPT
      ↓
Our Mock API (FastAPI)
      ↓
Static Mock Data (Python dicts)
```

## Target Architecture (Production)

```
ChatGPT Custom GPT
      ↓
Our Middleware API (FastAPI)
      ↓
Nomnom Platform API
      ↓
Restaurant POS Systems
```

## Integration Strategy

### Phase 1: API Discovery (Week 1)
**Goal**: Understand Nomnom's API capabilities

**Tasks**:
1. Get Nomnom API documentation from Stanley/Vijay
2. Obtain API credentials (sandbox environment)
3. Map Nomnom endpoints to our mock endpoints
4. Identify gaps and differences
5. Document authentication mechanism

**Questions to Answer**:
- What authentication does Nomnom use? (API key, OAuth, JWT?)
- What's the rate limit?
- Is there a sandbox/test environment?
- What's the data format? (JSON, XML?)
- Are there webhooks for order status updates?
- How is real-time inventory handled?

### Phase 2: Data Mapping (Week 1-2)
**Goal**: Create adapters between our API and Nomnom

**Create Mapping Layer**:

```python
# nomnom_adapter.py

class NomNomAdapter:
    """Adapter to translate between our API and Nomnom"""
    
    def __init__(self, api_key: str, base_url: str):
        self.api_key = api_key
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        })
    
    def search_restaurants(self, city=None, cuisine=None, lat=None, lng=None):
        """
        Translate our search format to Nomnom's format
        """
        # Map our parameters to Nomnom's expected format
        nomnom_params = self._map_search_params(city, cuisine, lat, lng)
        
        # Call Nomnom API
        response = self.session.get(
            f"{self.base_url}/restaurants/search",
            params=nomnom_params
        )
        
        # Transform Nomnom response to our format
        nomnom_restaurants = response.json()
        return self._transform_restaurants(nomnom_restaurants)
    
    def _map_search_params(self, city, cuisine, lat, lng):
        """Map our params to Nomnom's expected format"""
        # Example - adjust based on actual Nomnom API
        params = {}
        if city:
            params["location"] = city
        if cuisine:
            params["cuisine_type"] = cuisine
        if lat and lng:
            params["coordinates"] = f"{lat},{lng}"
        return params
    
    def _transform_restaurants(self, nomnom_data):
        """Transform Nomnom restaurant data to our format"""
        # Example transformation
        return [
            {
                "id": r["restaurant_id"],
                "name": r["name"],
                "cuisine": r["cuisine_type"],
                "location": {
                    "address": r["address"]["street"],
                    "city": r["address"]["city"],
                    "state": r["address"]["state"],
                    "zip": r["address"]["postal_code"],
                    "lat": r["coordinates"]["latitude"],
                    "lng": r["coordinates"]["longitude"]
                },
                "rating": r["rating"],
                "price_range": self._map_price_range(r["price_level"]),
                "delivery_time": r["estimated_delivery_time"],
                "minimum_order": r["minimum_order_amount"],
                "delivery_fee": r["delivery_fee"],
                "is_open": r["is_currently_open"],
                "image_url": r["logo_url"]
            }
            for r in nomnom_data.get("restaurants", [])
        ]
    
    # Similar methods for menu, orders, etc.
```

### Phase 3: Gradual Migration (Week 2-3)
**Goal**: Replace mock data with real Nomnom calls

**Strategy**: Feature flags for gradual rollout

```python
# config.py
USE_NOMNOM = os.getenv("USE_NOMNOM", "false").lower() == "true"
NOMNOM_API_KEY = os.getenv("NOMNOM_API_KEY")
NOMNOM_BASE_URL = os.getenv("NOMNOM_BASE_URL")

# main.py
from nomnom_adapter import NomNomAdapter
from mock_data import get_restaurants_by_location as mock_get_restaurants

if USE_NOMNOM:
    nomnom = NomNomAdapter(NOMNOM_API_KEY, NOMNOM_BASE_URL)

@app.get("/api/v1/restaurants/search")
async def search_restaurants(city=None, cuisine=None, lat=None, lng=None):
    if USE_NOMNOM:
        # Use real Nomnom API
        return nomnom.search_restaurants(city, cuisine, lat, lng)
    else:
        # Use mock data
        return mock_get_restaurants(city, cuisine, lat, lng)
```

### Phase 4: Testing & Validation (Week 3-4)
**Goal**: Ensure Nomnom integration works correctly

**Test Cases**:
1. Restaurant search with various filters
2. Menu retrieval with real-time pricing
3. Order creation and submission
4. Payment processing
5. Order status tracking
6. Error handling (restaurant closed, item unavailable, etc.)

**Validation Checklist**:
- [ ] All mock API endpoints have Nomnom equivalents
- [ ] Data transformations are accurate
- [ ] Error handling covers Nomnom-specific errors
- [ ] Performance is acceptable (<2s response time)
- [ ] Real-time inventory updates work
- [ ] Payment processing is secure
- [ ] Order tracking is accurate

## Expected Nomnom API Endpoints

Based on typical food ordering platforms, we expect:

### Restaurant Discovery
```
GET /api/v1/restaurants
  ?location=<city>
  &cuisine=<type>
  &lat=<latitude>
  &lng=<longitude>
  &radius=<miles>

Response:
{
  "restaurants": [
    {
      "restaurant_id": "string",
      "name": "string",
      "cuisine_type": "string",
      "address": {...},
      "coordinates": {...},
      "rating": 4.5,
      "is_currently_open": true,
      ...
    }
  ]
}
```

### Menu Retrieval
```
GET /api/v1/restaurants/{restaurant_id}/menu

Response:
{
  "menu": {
    "categories": [
      {
        "category_id": "string",
        "name": "string",
        "items": [
          {
            "item_id": "string",
            "name": "string",
            "description": "string",
            "price": 14.99,
            "available": true,
            ...
          }
        ]
      }
    ]
  }
}
```

### Order Creation
```
POST /api/v1/orders

Request:
{
  "restaurant_id": "string",
  "items": [
    {
      "item_id": "string",
      "quantity": 1,
      "modifications": []
    }
  ],
  "delivery_address": {...},
  "payment_method": {...}
}

Response:
{
  "order_id": "string",
  "status": "pending",
  "total": 25.99,
  "estimated_delivery": "2024-01-15T19:30:00Z"
}
```

### Order Tracking
```
GET /api/v1/orders/{order_id}

Response:
{
  "order_id": "string",
  "status": "preparing",
  "restaurant": {...},
  "items": [...],
  "delivery_address": {...},
  "estimated_delivery": "2024-01-15T19:30:00Z",
  "driver": {...}
}
```

## Data Transformation Examples

### Restaurant Data
```python
# Nomnom Format → Our Format

def transform_restaurant(nomnom_restaurant):
    return {
        "id": nomnom_restaurant["restaurant_id"],
        "name": nomnom_restaurant["name"],
        "cuisine": nomnom_restaurant["cuisine_type"],
        "rating": nomnom_restaurant["rating"],
        "price_range": map_price_range(nomnom_restaurant["price_level"]),
        "delivery_time": nomnom_restaurant["estimated_delivery_time"],
        "minimum_order": nomnom_restaurant["minimum_order_amount"],
        "delivery_fee": nomnom_restaurant["delivery_fee"],
        "is_open": nomnom_restaurant["is_currently_open"],
        "location": {
            "address": nomnom_restaurant["address"]["street"],
            "city": nomnom_restaurant["address"]["city"],
            "state": nomnom_restaurant["address"]["state"],
            "zip": nomnom_restaurant["address"]["postal_code"],
            "lat": nomnom_restaurant["coordinates"]["latitude"],
            "lng": nomnom_restaurant["coordinates"]["longitude"]
        }
    }

def map_price_range(price_level):
    """Map Nomnom price level (1-4) to our format ($-$$$$)"""
    mapping = {1: "$", 2: "$$", 3: "$$$", 4: "$$$$"}
    return mapping.get(price_level, "$$")
```

### Menu Data
```python
def transform_menu(nomnom_menu):
    return {
        "categories": [
            {
                "name": category["name"],
                "items": [
                    {
                        "id": item["item_id"],
                        "name": item["name"],
                        "description": item["description"],
                        "price": item["price"],
                        "vegetarian": "vegetarian" in item.get("dietary_tags", []),
                        "spicy": item.get("spice_level", 0) > 0,
                        "popular": item.get("is_popular", False),
                        "image_url": item.get("image_url")
                    }
                    for item in category["items"]
                    if item.get("available", True)  # Filter unavailable items
                ]
            }
            for category in nomnom_menu["categories"]
        ]
    }
```

### Order Data
```python
def transform_order_request(our_order):
    """Transform our order format to Nomnom format"""
    return {
        "restaurant_id": our_order["restaurant_id"],
        "items": [
            {
                "item_id": item["item_id"],
                "quantity": item["quantity"],
                "special_instructions": item.get("special_instructions", ""),
                "modifications": []
            }
            for item in our_order["items"]
        ],
        "delivery_address": {
            "street": our_order["delivery_address"]["address"],
            "city": our_order["delivery_address"]["city"],
            "state": our_order["delivery_address"]["state"],
            "postal_code": our_order["delivery_address"]["zip"]
        },
        "special_instructions": our_order.get("special_instructions", "")
    }

def transform_order_response(nomnom_order):
    """Transform Nomnom order to our format"""
    return {
        "id": nomnom_order["order_id"],
        "restaurant_id": nomnom_order["restaurant"]["restaurant_id"],
        "restaurant_name": nomnom_order["restaurant"]["name"],
        "items": [
            {
                "item_id": item["item_id"],
                "name": item["name"],
                "price": item["price"],
                "quantity": item["quantity"]
            }
            for item in nomnom_order["items"]
        ],
        "subtotal": nomnom_order["pricing"]["subtotal"],
        "delivery_fee": nomnom_order["pricing"]["delivery_fee"],
        "tax": nomnom_order["pricing"]["tax"],
        "total": nomnom_order["pricing"]["total"],
        "status": nomnom_order["status"],
        "created_at": nomnom_order["created_at"],
        "estimated_delivery": nomnom_order["estimated_delivery_time"],
        "payment_status": nomnom_order["payment"]["status"]
    }
```

## Error Handling

### Nomnom-Specific Errors
```python
class NomNomError(Exception):
    """Base exception for Nomnom API errors"""
    pass

class RestaurantClosedError(NomNomError):
    """Restaurant is currently closed"""
    pass

class ItemUnavailableError(NomNomError):
    """Menu item is not available"""
    pass

class DeliveryUnavailableError(NomNomError):
    """Delivery not available to this address"""
    pass

def handle_nomnom_error(response):
    """Handle Nomnom API errors"""
    if response.status_code == 400:
        error_data = response.json()
        error_code = error_data.get("error_code")
        
        if error_code == "RESTAURANT_CLOSED":
            raise RestaurantClosedError(error_data.get("message"))
        elif error_code == "ITEM_UNAVAILABLE":
            raise ItemUnavailableError(error_data.get("message"))
        elif error_code == "DELIVERY_UNAVAILABLE":
            raise DeliveryUnavailableError(error_data.get("message"))
    
    response.raise_for_status()
```

## Performance Considerations

### Caching Strategy
```python
from functools import lru_cache
from datetime import datetime, timedelta

# Cache restaurant data for 5 minutes
@lru_cache(maxsize=100)
def get_restaurant_cached(restaurant_id, cache_time):
    return nomnom.get_restaurant(restaurant_id)

# Menu data - cache for 15 minutes
@lru_cache(maxsize=50)
def get_menu_cached(restaurant_id, cache_time):
    return nomnom.get_menu(restaurant_id)

# Helper to get current cache key
def get_cache_key(minutes=5):
    now = datetime.now()
    return now.replace(second=0, microsecond=0) // timedelta(minutes=minutes)
```

### Rate Limiting
```python
from slowapi import Limiter
from slowapi.util import get_remote_address

limiter = Limiter(key_func=get_remote_address)

@app.get("/api/v1/restaurants/search")
@limiter.limit("30/minute")  # 30 requests per minute
async def search_restaurants(...):
    ...
```

## Monitoring & Logging

### Track Nomnom API Calls
```python
import time

def log_nomnom_call(endpoint, params, response_time, status_code):
    logger.info(f"NOMNOM_API_CALL", extra={
        "endpoint": endpoint,
        "params": params,
        "response_time_ms": response_time * 1000,
        "status_code": status_code,
        "timestamp": datetime.now().isoformat()
    })

def call_nomnom_api(endpoint, **kwargs):
    start_time = time.time()
    response = nomnom.session.get(endpoint, **kwargs)
    response_time = time.time() - start_time
    
    log_nomnom_call(endpoint, kwargs, response_time, response.status_code)
    
    return response
```

## Testing Strategy

### Unit Tests
```python
# test_nomnom_adapter.py

def test_transform_restaurant():
    nomnom_data = {
        "restaurant_id": "nom123",
        "name": "Test Restaurant",
        "cuisine_type": "Italian",
        # ... more fields
    }
    
    result = transform_restaurant(nomnom_data)
    
    assert result["id"] == "nom123"
    assert result["name"] == "Test Restaurant"
    assert result["cuisine"] == "Italian"
```

### Integration Tests
```python
# test_nomnom_integration.py

def test_search_restaurants_integration():
    """Test actual Nomnom API call"""
    adapter = NomNomAdapter(TEST_API_KEY, TEST_BASE_URL)
    
    restaurants = adapter.search_restaurants(city="San Francisco")
    
    assert len(restaurants) > 0
    assert all("id" in r for r in restaurants)
    assert all("name" in r for r in restaurants)
```

### Mock Nomnom Responses
```python
# For testing without hitting real API
import responses

@responses.activate
def test_search_with_mocked_nomnom():
    responses.add(
        responses.GET,
        "https://api.nomnom.com/restaurants/search",
        json={"restaurants": [...]},
        status=200
    )
    
    adapter = NomNomAdapter(API_KEY, BASE_URL)
    result = adapter.search_restaurants(city="SF")
    
    assert len(result) > 0
```

## Rollout Plan

### Week 1: Setup & Discovery
- [ ] Get Nomnom API access
- [ ] Review documentation
- [ ] Test authentication
- [ ] Map all endpoints
- [ ] Create adapter skeleton

### Week 2: Implementation
- [ ] Implement restaurant search adapter
- [ ] Implement menu retrieval adapter
- [ ] Implement order creation adapter
- [ ] Add error handling
- [ ] Add logging

### Week 3: Testing
- [ ] Unit tests for all adapters
- [ ] Integration tests with Nomnom sandbox
- [ ] Performance testing
- [ ] Error scenario testing
- [ ] Load testing

### Week 4: Gradual Rollout
- [ ] Deploy with feature flag (USE_NOMNOM=false)
- [ ] Enable for internal testing (10% traffic)
- [ ] Monitor for errors
- [ ] Increase to 50% traffic
- [ ] Full rollout (100% traffic)
- [ ] Remove mock data code

## Success Metrics

- **Uptime**: >99.9% API availability
- **Response Time**: <2s for restaurant search, <1s for menu
- **Error Rate**: <1% of requests
- **Order Success Rate**: >95% of orders complete successfully
- **Data Accuracy**: 100% match between Nomnom and our API

## Contingency Plan

If Nomnom integration fails:
1. Revert to mock data immediately (feature flag)
2. Investigate root cause
3. Fix and test in sandbox
4. Gradual re-rollout

## Next Steps

1. **Contact Stanley/Vijay** for Nomnom API documentation
2. **Schedule meeting** with Nomnom technical team
3. **Get sandbox credentials** for testing
4. **Start adapter implementation** once API docs received
5. **Parallel track**: Continue refining ChatGPT integration with mock data

