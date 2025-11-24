# 🚀 DEPLOY NOW - Quick Commands

**Everything is ready. Just run these commands:**

---

## Step 1: Push to GitHub (2 minutes)

```bash
cd /Users/premkalyan/code/CORP/ai-food-ordering-poc

# Authenticate GitHub CLI
gh auth login
# Follow the prompts in your browser

# Create repo and push (one command!)
gh repo create ai-food-ordering-poc --public --source=. --remote=origin --push
```

**✅ Done!** Your code is now at: `https://github.com/premkalyan/ai-food-ordering-poc`

---

## Step 2: Deploy to Vercel (3 minutes)

### Option A: Vercel Dashboard (Easiest - Recommended)

1. **Go to**: https://vercel.com/new
2. **Sign in** with GitHub
3. **Import** `premkalyan/ai-food-ordering-poc`
4. **Settings**:
   - Framework Preset: **Other**
   - Root Directory: `./`
   - Build Command: (leave empty)
   - Output Directory: (leave empty)
   - Install Command: `pip install -r requirements.txt`
5. **Click**: Deploy

**✅ Done!** Your API is live at: `https://ai-food-ordering-poc.vercel.app`

### Option B: Vercel CLI (Alternative)

```bash
# Install Vercel CLI
npm install -g vercel

# Login
vercel login

# Deploy
cd /Users/premkalyan/code/CORP/ai-food-ordering-poc
vercel --prod
```

---

## Step 3: Test Your API (1 minute)

```bash
# Test health endpoint
curl https://ai-food-ordering-poc.vercel.app/health

# Test restaurant search
curl "https://ai-food-ordering-poc.vercel.app/api/v1/restaurants/search?cuisine=Indian"

# View API docs in browser
open https://ai-food-ordering-poc.vercel.app/docs
```

**Expected**: All endpoints return 200 OK with JSON data

---

## Step 4: Set Up ChatGPT Custom GPT (5 minutes)

### 4.1 Create Custom GPT

1. Go to: https://chat.openai.com
2. Click: **Your Profile** → **My GPTs** → **Create a GPT**
3. Click: **Configure** tab

### 4.2 Basic Configuration

**Name:**
```
Food Ordering Assistant
```

**Description:**
```
AI-powered food ordering assistant for discovering restaurants and placing orders
```

**Instructions:**
```
You help users order food from restaurants through natural conversation.

Process:
1. Ask for location or cuisine preference
2. Search restaurants using the API
3. Show menu when user selects a restaurant
4. Help compose order with items and quantities
5. Confirm delivery address
6. Process payment and provide order tracking

Always be conversational and confirm important details before finalizing orders.
```

**Conversation starters:**
```
I want to order Indian food
Show me restaurants near me
What's good for dinner tonight?
I'm craving sushi
```

### 4.3 Add Actions

Click **"Create new action"** and paste this:

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

**Important**: Make sure the URL is your actual Vercel URL!

### 4.4 Privacy & Save

- **Privacy**: "Only me" (for testing)
- Click **Save**
- Click **View GPT**

---

## Step 5: Test Complete Flow! (2 minutes)

In your Custom GPT, try:

```
"I want to order Indian food"
```

**Expected Flow**:
1. ✅ GPT searches restaurants
2. ✅ Shows Taj Palace Indian Cuisine
3. ✅ You ask for menu
4. ✅ GPT shows menu with prices
5. ✅ You order items
6. ✅ GPT confirms and creates order
7. ✅ You get order ID and tracking

**🎉 SUCCESS!** You've built and deployed an AI-powered food ordering system!

---

## 🎯 What You've Accomplished

✅ Built complete mock API (2000+ lines)  
✅ Pushed to GitHub  
✅ Deployed to Vercel  
✅ Created ChatGPT Custom GPT  
✅ End-to-end ordering works  

**Time**: From idea to deployed in one day! 🚀

---

## 📊 Share Your Work

### GitHub Repository
```
https://github.com/premkalyan/ai-food-ordering-poc
```

### Live API
```
https://ai-food-ordering-poc.vercel.app
```

### API Documentation
```
https://ai-food-ordering-poc.vercel.app/docs
```

### Custom GPT
Share link from ChatGPT (Settings → Share)

---

## 🔄 Make Updates

To update your deployed API:

```bash
cd /Users/premkalyan/code/CORP/ai-food-ordering-poc

# Make your changes
# ...

# Commit and push
git add .
git commit -m "Your update description"
git push

# Vercel automatically deploys!
```

---

## 📞 Next Steps

### Immediate
- ✅ Deploy (you're doing this now!)
- ⏭️ Test with team
- ⏭️ Gather feedback
- ⏭️ Share demo with Sudarshan

### This Week
- Get Nomnom API documentation
- Test with pilot restaurants
- Refine based on feedback

### Next Week
- Integrate Nomnom API
- Onboard 50 restaurants
- Prepare OpenAI partnership pitch

---

## 🆘 Need Help?

**GitHub Issues**: See [GITHUB_SETUP.md](GITHUB_SETUP.md)  
**Vercel Issues**: See [VERCEL_DEPLOYMENT.md](VERCEL_DEPLOYMENT.md)  
**ChatGPT Issues**: See [CHATGPT_SETUP.md](CHATGPT_SETUP.md)

---

## 🎉 You're Ready!

**Just run the commands above and you'll have:**
- Live API on Vercel
- ChatGPT integration working
- Complete food ordering system
- Ready to demo!

**Let's go!** 🚀

