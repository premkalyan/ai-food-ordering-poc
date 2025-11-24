# Quick Start Guide - AI Food Ordering POC

## 🚀 Get Running in 5 Minutes

### Step 1: Install Dependencies (1 min)

```bash
cd ai-food-ordering-poc
pip install -r requirements.txt
```

### Step 2: Start the API (30 seconds)

```bash
python main.py
```

You should see:
```
INFO:     Started server process
INFO:     Uvicorn running on http://0.0.0.0:8000
```

### Step 3: Test the API (1 min)

Open another terminal:
```bash
python test_api.py
```

You should see all tests passing ✅

### Step 4: View API Documentation (30 seconds)

Open in browser: http://localhost:8000/docs

You'll see interactive API documentation where you can test all endpoints.

### Step 5: Expose for ChatGPT (2 min)

```bash
# Install ngrok
brew install ngrok

# Expose your API
ngrok http 8000
```

Copy the ngrok URL (e.g., `https://abc123.ngrok.io`)

## 🤖 Set Up ChatGPT Custom GPT

### 1. Create Custom GPT

1. Go to https://chat.openai.com
2. Click your profile → "My GPTs" → "Create a GPT"
3. Click "Configure" tab

### 2. Basic Info

**Name:** `Food Ordering Assistant`

**Description:**
```
AI-powered food ordering assistant for discovering restaurants and placing orders
```

**Instructions:** (Copy from CHATGPT_SETUP.md or use this short version)
```
You help users order food from restaurants. 

Process:
1. Ask for location or cuisine preference
2. Search restaurants using the API
3. Show menu when user selects a restaurant
4. Help compose order with items and quantities
5. Confirm delivery address
6. Process payment and provide order tracking

Always be conversational and confirm important details before finalizing orders.
```

### 3. Add Actions

Click "Create new action" and paste:

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "Food Ordering API",
    "version": "1.0.0"
  },
  "servers": [
    {
      "url": "YOUR_NGROK_URL_HERE"
    }
  ],
  "paths": {
    "/api/v1/restaurants/search": {
      "get": {
        "operationId": "searchRestaurants",
        "summary": "Search restaurants",
        "parameters": [
          {"name": "city", "in": "query", "schema": {"type": "string"}},
          {"name": "cuisine", "in": "query", "schema": {"type": "string"}}
        ]
      }
    },
    "/api/v1/restaurants/{restaurant_id}/menu": {
      "get": {
        "operationId": "getMenu",
        "summary": "Get restaurant menu",
        "parameters": [
          {"name": "restaurant_id", "in": "path", "required": true, "schema": {"type": "string"}}
        ]
      }
    },
    "/api/v1/orders/create": {
      "post": {
        "operationId": "createOrder",
        "summary": "Create order",
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "restaurant_id": {"type": "string"},
                  "items": {"type": "array"},
                  "delivery_address": {"type": "object"}
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

**Replace `YOUR_NGROK_URL_HERE` with your actual ngrok URL!**

### 4. Test It!

Click "Preview" and try:
```
"I want to order Indian food"
```

Watch the magic happen! 🎉

## 📊 Monitor API Calls

Watch real-time logs:
```bash
tail -f api_calls.log
```

You'll see every request ChatGPT makes to your API!

## 🎯 Quick Test Scenarios

### Scenario 1: Restaurant Discovery
```
User: "Show me Chinese restaurants"
Expected: API calls /api/v1/restaurants/search?cuisine=Chinese
```

### Scenario 2: Menu Browsing
```
User: "What's on the menu at Golden Dragon?"
Expected: API calls /api/v1/restaurants/rest_002/menu
```

### Scenario 3: Complete Order
```
User: "Order kung pao chicken and fried rice from Golden Dragon"
Expected: API calls /api/v1/orders/create with items
```

## 📁 Project Structure

```
ai-food-ordering-poc/
├── main.py                 # FastAPI application
├── mock_data.py           # Restaurant and menu data
├── test_api.py            # Test suite
├── requirements.txt       # Python dependencies
├── README.md             # Project overview
├── CHATGPT_SETUP.md      # Detailed ChatGPT setup
├── DEPLOYMENT.md         # Deployment options
├── NOMNOM_INTEGRATION.md # Nomnom integration guide
├── PITCH_DECK.md         # Partnership pitch
└── api_calls.log         # API request logs
```

## 🔧 Troubleshooting

### API won't start
```bash
# Check if port 8000 is in use
lsof -i :8000

# Kill the process if needed
kill -9 <PID>

# Try again
python main.py
```

### ChatGPT can't reach API
1. Verify ngrok is running
2. Check ngrok URL is correct in Custom GPT
3. Test manually: `curl https://your-ngrok-url.ngrok.io/health`

### Tests failing
```bash
# Make sure API is running first
python main.py

# Then run tests in another terminal
python test_api.py
```

## 📚 Next Steps

1. ✅ **You are here** - POC running locally
2. 📝 Review CHATGPT_SETUP.md for detailed Custom GPT configuration
3. 🚀 Review DEPLOYMENT.md to deploy publicly
4. 🔌 Review NOMNOM_INTEGRATION.md for real API integration
5. 💼 Review PITCH_DECK.md for partnership strategy

## 💡 Tips

- **Keep ngrok running** while testing ChatGPT
- **Watch the logs** to see what ChatGPT is doing
- **Iterate on instructions** based on ChatGPT's behavior
- **Test edge cases** (closed restaurants, unavailable items)

## 🆘 Need Help?

1. Check the logs: `tail -f api_calls.log`
2. Test endpoints manually: http://localhost:8000/docs
3. Review error messages in terminal
4. Check CHATGPT_SETUP.md for detailed guidance

## 🎉 Success Checklist

- [ ] API running locally
- [ ] Tests passing
- [ ] API docs accessible
- [ ] ngrok exposing API
- [ ] Custom GPT created
- [ ] Custom GPT can search restaurants
- [ ] Custom GPT can show menus
- [ ] Custom GPT can create orders
- [ ] Logs showing API calls

Once all checked, you're ready to demo! 🚀

