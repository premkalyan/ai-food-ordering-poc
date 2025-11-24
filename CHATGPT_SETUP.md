# ChatGPT Custom GPT Setup Guide

## Overview
This guide walks you through creating a Custom GPT in ChatGPT that connects to our mock food ordering API.

## Prerequisites
1. ChatGPT Plus or Enterprise account
2. Mock API running locally or deployed publicly
3. Public URL for API (use ngrok for local testing)

## Step 1: Make API Publicly Accessible

### Option A: Using ngrok (for local testing)

```bash
# Install ngrok
brew install ngrok  # macOS
# or download from https://ngrok.com

# Start your API
python main.py

# In another terminal, expose it
ngrok http 8000

# You'll get a public URL like: https://abc123.ngrok.io
```

### Option B: Deploy to Cloud (for production)

Deploy to:
- **Heroku**: Easy deployment
- **Railway**: Simple and free tier
- **AWS Lambda**: Serverless option
- **DigitalOcean**: Full control

## Step 2: Create Custom GPT

1. Go to ChatGPT: https://chat.openai.com
2. Click your profile → "My GPTs"
3. Click "Create a GPT"
4. Click "Configure" tab

### Basic Configuration

**Name:**
```
Food Ordering Assistant
```

**Description:**
```
AI-powered food ordering assistant that helps you discover restaurants, browse menus, and place orders through natural conversation.
```

**Instructions:**
```
You are a helpful food ordering assistant that helps users discover restaurants, browse menus, and place orders.

Your capabilities:
1. Search for restaurants by location, cuisine type, or user preferences
2. Show detailed restaurant information including ratings, delivery time, and fees
3. Display restaurant menus with prices and descriptions
4. Help users compose orders with multiple items
5. Process orders and provide order tracking information

Conversation flow:
1. Start by asking the user's location or cuisine preference
2. Show relevant restaurants with key details
3. When user selects a restaurant, offer to show the menu
4. Help add items to order, confirming quantities and special requests
5. Calculate total including delivery fee and tax
6. Confirm delivery address before placing order
7. Process payment and provide order confirmation with tracking

Be conversational, helpful, and proactive in suggesting popular items or good deals.
Always confirm important details like delivery address and order items before finalizing.

When showing restaurants, highlight:
- Restaurant name and cuisine
- Rating and price range
- Delivery time and minimum order
- Delivery fee

When showing menu items, include:
- Item name and description
- Price
- Dietary info (vegetarian, spicy) if applicable
- Popular items

For orders, always show:
- Itemized list with quantities
- Subtotal, delivery fee, tax, and total
- Estimated delivery time
- Order tracking ID after confirmation
```

**Conversation starters:**
```
1. "I want to order Indian food"
2. "Show me restaurants near me"
3. "What's good for dinner tonight?"
4. "I'm craving sushi"
```

## Step 3: Configure API Actions

Click "Create new action" and paste this OpenAPI schema:

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "AI Food Ordering API",
    "description": "Restaurant ordering platform API",
    "version": "1.0.0"
  },
  "servers": [
    {
      "url": "https://YOUR_NGROK_URL_HERE"
    }
  ],
  "paths": {
    "/api/v1/restaurants/search": {
      "get": {
        "operationId": "searchRestaurants",
        "summary": "Search for restaurants",
        "description": "Search restaurants by location, cuisine, or coordinates",
        "parameters": [
          {
            "name": "city",
            "in": "query",
            "description": "City name to search in",
            "required": false,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "cuisine",
            "in": "query",
            "description": "Cuisine type (e.g., Indian, Chinese, Italian)",
            "required": false,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "lat",
            "in": "query",
            "description": "Latitude for location search",
            "required": false,
            "schema": {
              "type": "number"
            }
          },
          {
            "name": "lng",
            "in": "query",
            "description": "Longitude for location search",
            "required": false,
            "schema": {
              "type": "number"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "List of restaurants",
            "content": {
              "application/json": {
                "schema": {
                  "type": "array",
                  "items": {
                    "$ref": "#/components/schemas/Restaurant"
                  }
                }
              }
            }
          }
        }
      }
    },
    "/api/v1/restaurants/{restaurant_id}": {
      "get": {
        "operationId": "getRestaurant",
        "summary": "Get restaurant details",
        "parameters": [
          {
            "name": "restaurant_id",
            "in": "path",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Restaurant details",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Restaurant"
                }
              }
            }
          }
        }
      }
    },
    "/api/v1/restaurants/{restaurant_id}/menu": {
      "get": {
        "operationId": "getRestaurantMenu",
        "summary": "Get restaurant menu",
        "parameters": [
          {
            "name": "restaurant_id",
            "in": "path",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Restaurant menu",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Menu"
                }
              }
            }
          }
        }
      }
    },
    "/api/v1/orders/create": {
      "post": {
        "operationId": "createOrder",
        "summary": "Create a new order",
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/CreateOrderRequest"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Order created",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Order"
                }
              }
            }
          }
        }
      }
    },
    "/api/v1/orders/{order_id}": {
      "get": {
        "operationId": "getOrder",
        "summary": "Get order status",
        "parameters": [
          {
            "name": "order_id",
            "in": "path",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Order details",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Order"
                }
              }
            }
          }
        }
      }
    },
    "/api/v1/orders/{order_id}/payment": {
      "post": {
        "operationId": "processPayment",
        "summary": "Process order payment",
        "parameters": [
          {
            "name": "order_id",
            "in": "path",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/PaymentRequest"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Payment processed",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/PaymentResponse"
                }
              }
            }
          }
        }
      }
    },
    "/api/v1/cuisines": {
      "get": {
        "operationId": "getCuisines",
        "summary": "Get available cuisines",
        "responses": {
          "200": {
            "description": "List of cuisines",
            "content": {
              "application/json": {
                "schema": {
                  "type": "array",
                  "items": {
                    "type": "string"
                  }
                }
              }
            }
          }
        }
      }
    },
    "/api/v1/user/location": {
      "get": {
        "operationId": "getUserLocation",
        "summary": "Get user location",
        "responses": {
          "200": {
            "description": "User location",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "city": {"type": "string"},
                    "state": {"type": "string"},
                    "lat": {"type": "number"},
                    "lng": {"type": "number"}
                  }
                }
              }
            }
          }
        }
      }
    }
  },
  "components": {
    "schemas": {
      "Restaurant": {
        "type": "object",
        "properties": {
          "id": {"type": "string"},
          "name": {"type": "string"},
          "cuisine": {"type": "string"},
          "rating": {"type": "number"},
          "price_range": {"type": "string"},
          "delivery_time": {"type": "string"},
          "minimum_order": {"type": "number"},
          "delivery_fee": {"type": "number"},
          "is_open": {"type": "boolean"}
        }
      },
      "Menu": {
        "type": "object",
        "properties": {
          "categories": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "name": {"type": "string"},
                "items": {
                  "type": "array",
                  "items": {
                    "$ref": "#/components/schemas/MenuItem"
                  }
                }
              }
            }
          }
        }
      },
      "MenuItem": {
        "type": "object",
        "properties": {
          "id": {"type": "string"},
          "name": {"type": "string"},
          "description": {"type": "string"},
          "price": {"type": "number"},
          "vegetarian": {"type": "boolean"},
          "spicy": {"type": "boolean"},
          "popular": {"type": "boolean"}
        }
      },
      "CreateOrderRequest": {
        "type": "object",
        "required": ["restaurant_id", "items", "delivery_address"],
        "properties": {
          "restaurant_id": {"type": "string"},
          "items": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "item_id": {"type": "string"},
                "name": {"type": "string"},
                "price": {"type": "number"},
                "quantity": {"type": "integer"},
                "special_instructions": {"type": "string"}
              }
            }
          },
          "delivery_address": {
            "type": "object",
            "properties": {
              "address": {"type": "string"},
              "city": {"type": "string"},
              "state": {"type": "string"},
              "zip": {"type": "string"}
            }
          },
          "special_instructions": {"type": "string"}
        }
      },
      "Order": {
        "type": "object",
        "properties": {
          "id": {"type": "string"},
          "restaurant_id": {"type": "string"},
          "restaurant_name": {"type": "string"},
          "subtotal": {"type": "number"},
          "delivery_fee": {"type": "number"},
          "tax": {"type": "number"},
          "total": {"type": "number"},
          "status": {"type": "string"},
          "estimated_delivery": {"type": "string"},
          "payment_status": {"type": "string"}
        }
      },
      "PaymentRequest": {
        "type": "object",
        "properties": {
          "payment_method": {
            "type": "object",
            "properties": {
              "type": {"type": "string"},
              "last_four": {"type": "string"}
            }
          }
        }
      },
      "PaymentResponse": {
        "type": "object",
        "properties": {
          "success": {"type": "boolean"},
          "transaction_id": {"type": "string"},
          "message": {"type": "string"}
        }
      }
    }
  }
}
```

**Important:** Replace `YOUR_NGROK_URL_HERE` with your actual ngrok URL (e.g., `https://abc123.ngrok.io`)

## Step 4: Privacy Settings

- **Privacy**: Set to "Only me" for testing, "Anyone with a link" for sharing with team
- **Authentication**: None (for now, can add API key later)

## Step 5: Test Your Custom GPT

Click "Preview" and try these conversations:

### Test 1: Restaurant Discovery
```
You: I want to order Indian food
GPT: [Should call searchRestaurants with cuisine=Indian]
```

### Test 2: Menu Browsing
```
You: Show me the menu from Taj Palace
GPT: [Should call getRestaurantMenu]
```

### Test 3: Complete Order Flow
```
You: I'll order paneer butter masala and garlic naan from Taj Palace
GPT: [Should help compose order and call createOrder]
```

## Step 6: Monitor API Calls

Watch the logs in your terminal:

```bash
# Terminal 1: API server
python main.py

# Terminal 2: Watch logs
tail -f api_calls.log
```

You'll see detailed logs of every API call ChatGPT makes:
- Request method and URL
- Query parameters
- Request body
- Response status

## Troubleshooting

### Issue: ChatGPT can't reach API
- Verify ngrok is running
- Check ngrok URL is correct in OpenAPI schema
- Test API directly: `curl https://your-ngrok-url.ngrok.io/health`

### Issue: API returns errors
- Check logs in `api_calls.log`
- Verify request format matches expected schema
- Test endpoints manually with Postman or curl

### Issue: ChatGPT doesn't use actions
- Make sure instructions clearly tell GPT to use the API
- Try being more explicit: "Search for restaurants using the API"
- Check action configuration is saved

## Next Steps

1. **Test thoroughly**: Try various ordering scenarios
2. **Refine instructions**: Based on how ChatGPT behaves
3. **Add authentication**: Implement API key for security
4. **Deploy properly**: Move from ngrok to production hosting
5. **Integrate Nomnom**: Replace mock data with real API calls

## Production Deployment Checklist

- [ ] Deploy API to production server
- [ ] Add authentication (API key or OAuth)
- [ ] Set up proper logging and monitoring
- [ ] Add rate limiting
- [ ] Configure CORS properly
- [ ] Set up SSL certificate
- [ ] Add error tracking (Sentry)
- [ ] Create backup/fallback mechanisms
- [ ] Document API for Nomnom integration
- [ ] Test with real payment processing

## API Key Authentication (Optional)

To add API key authentication:

1. Add to Custom GPT Actions:
```json
"components": {
  "securitySchemes": {
    "ApiKeyAuth": {
      "type": "apiKey",
      "in": "header",
      "name": "X-API-Key"
    }
  }
},
"security": [
  {
    "ApiKeyAuth": []
  }
]
```

2. Update FastAPI to validate API key:
```python
from fastapi import Security, HTTPException
from fastapi.security import APIKeyHeader

API_KEY = "your-secret-key"
api_key_header = APIKeyHeader(name="X-API-Key")

async def verify_api_key(api_key: str = Security(api_key_header)):
    if api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Invalid API key")
    return api_key
```

3. Add to endpoints:
```python
@app.get("/api/v1/restaurants/search", dependencies=[Depends(verify_api_key)])
```

