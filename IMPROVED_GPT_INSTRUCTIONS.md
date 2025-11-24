# Improved ChatGPT Custom GPT Instructions

## Copy this into your Custom GPT "Instructions" field:

```
You are a helpful food ordering assistant that helps users discover restaurants and place orders through natural conversation.

WORKFLOW:
1. DETECT LOCATION FIRST
   - Call getUserLocation API to get user's city automatically
   - If location detected, say: "I see you're in [City]. Let me find restaurants for you!"
   - If user mentions a different city, search that city instead

2. SHOW AVAILABLE OPTIONS
   - After getting location, proactively offer: "What would you like to do?
     • Browse restaurants by cuisine (Indian, Chinese, Italian, Japanese, Mexican, etc.)
     • See all available restaurants in your area
     • Tell me what you're craving and I'll suggest options"

3. RESTAURANT DISCOVERY
   - When user chooses cuisine, call searchRestaurants API
   - Show results with: Name, Rating, Price range, Delivery time, Minimum order, Delivery fee
   - Ask: "Would you like to see the menu from [Restaurant Name]?"

4. MENU BROWSING
   - Call getMenu API for selected restaurant
   - Show menu organized by categories
   - Highlight popular items with ⭐
   - Mark vegetarian items with 🥬 and spicy items with 🌶️
   - After showing menu, ask: "What would you like to order?"

5. ORDER COMPOSITION
   - Help user add items with quantities
   - Keep running total as items are added
   - Offer suggestions: "Would you like to add any sides or drinks?"
   - When done, show order summary with subtotal, delivery fee, tax, and total

6. DELIVERY & PAYMENT
   - Ask for delivery address (street, city, state, zip)
   - Confirm all details before placing order
   - Call createOrder API
   - Show order confirmation with: Order ID, Total, Estimated delivery time
   - Call processPayment API (simulated for demo)
   - Provide order tracking information

HELPFUL BEHAVIORS:
- Always be conversational and friendly
- Proactively suggest next steps
- Confirm important details before proceeding
- Show prices clearly
- Calculate totals accurately
- Handle errors gracefully (e.g., "That restaurant isn't available right now. Would you like to try another one?")

DEMO NOTES:
- This is a demo with mock restaurants in San Francisco
- If user asks about other cities, explain: "This demo currently has San Francisco restaurants. In production, we'll have restaurants in your city too! Would you like to see what's available in SF?"
- Payment is simulated (no real charges)
- Orders are for demonstration purposes

AVAILABLE CUISINES:
Indian, Chinese, Italian, Japanese, Mexican, Mediterranean, Thai, Korean

Always guide users through the process smoothly and make ordering food feel effortless!
```

## Updated OpenAPI Schema (Add to Actions)

Replace your current schema with this improved version:

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "Food Ordering API",
    "version": "1.0.0"
  },
  "servers": [
    {
      "url": "https://ai-food-ordering-poc.vercel.app"
    }
  ],
  "paths": {
    "/api/v1/user/location": {
      "get": {
        "operationId": "getUserLocation",
        "summary": "Get user's current location automatically",
        "description": "Detects user location to show nearby restaurants. Call this first when user wants to order food.",
        "parameters": [
          {
            "name": "city",
            "in": "query",
            "schema": {"type": "string"},
            "description": "Optional: specify city if user mentions one"
          }
        ]
      }
    },
    "/api/v1/cities": {
      "get": {
        "operationId": "getAvailableCities",
        "summary": "Get list of cities where restaurants are available",
        "description": "Returns all cities where we have restaurant coverage"
      }
    },
    "/api/v1/cuisines": {
      "get": {
        "operationId": "getAvailableCuisines",
        "summary": "Get list of available cuisine types",
        "description": "Returns all cuisine types available for ordering"
      }
    },
    "/api/v1/restaurants/search": {
      "get": {
        "operationId": "searchRestaurants",
        "summary": "Search restaurants by cuisine or location",
        "description": "Find restaurants based on user preferences",
        "parameters": [
          {
            "name": "city",
            "in": "query",
            "schema": {"type": "string"},
            "description": "City name to search in"
          },
          {
            "name": "cuisine",
            "in": "query",
            "schema": {"type": "string"},
            "description": "Cuisine type (Indian, Chinese, Italian, Japanese, Mexican, etc.)"
          }
        ]
      }
    },
    "/api/v1/restaurants/{restaurant_id}": {
      "get": {
        "operationId": "getRestaurant",
        "summary": "Get detailed restaurant information",
        "parameters": [
          {
            "name": "restaurant_id",
            "in": "path",
            "required": true,
            "schema": {"type": "string"}
          }
        ]
      }
    },
    "/api/v1/restaurants/{restaurant_id}/menu": {
      "get": {
        "operationId": "getMenu",
        "summary": "Get restaurant menu with all items and prices",
        "description": "Returns complete menu organized by categories with prices and dietary info",
        "parameters": [
          {
            "name": "restaurant_id",
            "in": "path",
            "required": true,
            "schema": {"type": "string"},
            "description": "Restaurant ID (e.g., rest_001)"
          }
        ]
      }
    },
    "/api/v1/orders/create": {
      "post": {
        "operationId": "createOrder",
        "summary": "Create a new food order",
        "description": "Places order with restaurant and calculates total with delivery fee and tax",
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "required": ["restaurant_id", "items", "delivery_address"],
                "properties": {
                  "restaurant_id": {
                    "type": "string",
                    "description": "Restaurant ID"
                  },
                  "items": {
                    "type": "array",
                    "description": "List of items to order",
                    "items": {
                      "type": "object",
                      "required": ["item_id", "name", "price", "quantity"],
                      "properties": {
                        "item_id": {"type": "string"},
                        "name": {"type": "string"},
                        "price": {"type": "number"},
                        "quantity": {"type": "integer", "minimum": 1}
                      }
                    }
                  },
                  "delivery_address": {
                    "type": "object",
                    "required": ["address", "city", "state", "zip"],
                    "properties": {
                      "address": {"type": "string"},
                      "city": {"type": "string"},
                      "state": {"type": "string"},
                      "zip": {"type": "string"}
                    }
                  },
                  "special_instructions": {
                    "type": "string",
                    "description": "Optional special requests"
                  }
                }
              }
            }
          }
        }
      }
    },
    "/api/v1/orders/{order_id}": {
      "get": {
        "operationId": "getOrderStatus",
        "summary": "Get order status and tracking information",
        "parameters": [
          {
            "name": "order_id",
            "in": "path",
            "required": true,
            "schema": {"type": "string"}
          }
        ]
      }
    },
    "/api/v1/orders/{order_id}/payment": {
      "post": {
        "operationId": "processPayment",
        "summary": "Process payment for an order",
        "description": "Simulates payment processing (demo only - no real charges)",
        "parameters": [
          {
            "name": "order_id",
            "in": "path",
            "required": true,
            "schema": {"type": "string"}
          }
        ],
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "payment_method": {
                    "type": "object",
                    "properties": {
                      "type": {
                        "type": "string",
                        "enum": ["credit_card", "debit_card", "paypal", "apple_pay"]
                      },
                      "last_four": {"type": "string"}
                    }
                  }
                }
              }
            }
          }
        }
      }
    }
  }
}
```

## Key Improvements

### 1. ✅ Auto-Location Detection
- GPT calls `getUserLocation` first
- Gets city automatically
- Shows: "I see you're in San Francisco..."

### 2. ✅ Guided Options (Better than buttons)
- GPT proactively suggests: "What would you like to do?"
- Lists options in natural language
- Users can type or choose

### 3. ✅ Show Available Cities
- GPT can call `getAvailableCities` 
- Shows: "We have restaurants in: San Francisco"
- In production, will show all cities

### 4. ✅ Better Flow
```
User: "I want to order food"
↓
GPT: Calls getUserLocation → "I see you're in San Francisco!"
↓
GPT: "What would you like to do?
      • Browse by cuisine (Indian, Chinese, Italian...)
      • See all restaurants
      • Tell me what you're craving"
↓
User: "Indian food"
↓
GPT: Shows Taj Palace with all details
↓
GPT: "Would you like to see their menu?"
```

## 🚀 Next Steps

1. **Update your Custom GPT**:
   - Copy the new instructions above
   - Replace the OpenAPI schema with the improved version
   - Save

2. **Test the improved flow**:
   ```
   "I want to order food"
   ```
   
   GPT should automatically detect location and offer options!

3. **Commit the changes**:

Let me commit and push the API improvements:

<function_calls>
<invoke name="run_terminal_cmd">
<parameter name="command">cd /Users/premkalyan/code/CORP/ai-food-ordering-poc && git add main.py IMPROVED_GPT_INSTRUCTIONS.md && git commit -m "Improve: Add auto-location detection and better user flow guidance" && git push
