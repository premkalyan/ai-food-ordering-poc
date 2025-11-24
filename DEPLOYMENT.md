# Deployment Guide

## Quick Start (Local Testing)

### 1. Install Dependencies

```bash
cd ai-food-ordering-poc
pip install -r requirements.txt
```

### 2. Run the API

```bash
python main.py
```

API will be available at: http://localhost:8000

### 3. Test the API

```bash
# In another terminal
python test_api.py
```

### 4. View API Documentation

Open in browser: http://localhost:8000/docs

## Expose API for ChatGPT (ngrok)

### Install ngrok

```bash
# macOS
brew install ngrok

# Or download from https://ngrok.com
```

### Create ngrok account and authenticate

```bash
ngrok config add-authtoken YOUR_AUTH_TOKEN
```

### Expose your local API

```bash
# Terminal 1: Run API
python main.py

# Terminal 2: Expose with ngrok
ngrok http 8000
```

You'll get output like:
```
Forwarding  https://abc123.ngrok.io -> http://localhost:8000
```

Use this URL in your ChatGPT Custom GPT configuration!

### Keep ngrok running

The free tier gives you a random URL each time. For a permanent URL, upgrade to ngrok paid plan.

## Production Deployment Options

### Option 1: Railway (Recommended for POC)

**Pros**: Free tier, easy deployment, automatic HTTPS
**Cons**: May sleep after inactivity on free tier

```bash
# Install Railway CLI
npm install -g @railway/cli

# Login
railway login

# Initialize project
railway init

# Deploy
railway up
```

Add `Procfile`:
```
web: uvicorn main:app --host 0.0.0.0 --port $PORT
```

### Option 2: Heroku

**Pros**: Well-documented, easy to use
**Cons**: No free tier anymore

```bash
# Install Heroku CLI
brew install heroku/brew/heroku

# Login
heroku login

# Create app
heroku create your-food-ordering-api

# Deploy
git push heroku main
```

Add `Procfile`:
```
web: uvicorn main:app --host 0.0.0.0 --port $PORT
```

Add `runtime.txt`:
```
python-3.11.0
```

### Option 3: DigitalOcean App Platform

**Pros**: Simple, affordable ($5/month)
**Cons**: Requires payment

1. Push code to GitHub
2. Go to DigitalOcean App Platform
3. Connect GitHub repo
4. Configure:
   - Build Command: `pip install -r requirements.txt`
   - Run Command: `uvicorn main:app --host 0.0.0.0 --port 8080`
5. Deploy

### Option 4: AWS Lambda (Serverless)

**Pros**: Pay per use, scales automatically
**Cons**: More complex setup

Use Mangum adapter:

```bash
pip install mangum
```

Update `main.py`:
```python
from mangum import Mangum

# ... existing code ...

handler = Mangum(app)
```

Deploy with AWS SAM or Serverless Framework.

### Option 5: Google Cloud Run

**Pros**: Generous free tier, scales to zero
**Cons**: Requires GCP account

```bash
# Install gcloud CLI
# https://cloud.google.com/sdk/docs/install

# Build container
gcloud builds submit --tag gcr.io/PROJECT_ID/food-ordering-api

# Deploy
gcloud run deploy food-ordering-api \
  --image gcr.io/PROJECT_ID/food-ordering-api \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated
```

Add `Dockerfile`:
```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
```

## Environment Configuration

### Production Settings

Create `.env` file:
```bash
# API Configuration
API_KEY=your-secret-api-key-here
PORT=8000
HOST=0.0.0.0
LOG_LEVEL=INFO

# CORS Settings
ALLOWED_ORIGINS=https://chat.openai.com,https://chatgpt.com

# Database (when integrating with Nomnom)
DATABASE_URL=postgresql://user:pass@host:5432/dbname

# Nomnom API (future)
NOMNOM_API_URL=https://api.nomnom.com
NOMNOM_API_KEY=your-nomnom-key
```

Update `main.py` to use environment variables:
```python
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
PORT = int(os.getenv("PORT", 8000))
```

## Security Checklist

Before going to production:

- [ ] Add API key authentication
- [ ] Configure CORS properly (restrict to ChatGPT domains)
- [ ] Enable HTTPS (automatic with most platforms)
- [ ] Add rate limiting
- [ ] Set up monitoring and alerts
- [ ] Configure logging (don't log sensitive data)
- [ ] Add input validation
- [ ] Set up error tracking (Sentry)
- [ ] Regular security updates
- [ ] Backup strategy

## Monitoring & Logging

### Add Sentry for Error Tracking

```bash
pip install sentry-sdk[fastapi]
```

```python
import sentry_sdk

sentry_sdk.init(
    dsn="your-sentry-dsn",
    traces_sample_rate=1.0,
)
```

### Add Logging

Already implemented in `main.py`:
- All requests logged to `api_calls.log`
- Console output for debugging
- Structured JSON logging

### Monitor with Uptime Robot

1. Sign up at https://uptimerobot.com (free)
2. Add monitor for your API health endpoint
3. Get alerts if API goes down

## Performance Optimization

### Add Caching

```bash
pip install fastapi-cache2[redis]
```

```python
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache.decorator import cache

@cache(expire=300)  # 5 minutes
@app.get("/api/v1/restaurants/search")
async def search_restaurants(...):
    ...
```

### Add Database Connection Pooling

When integrating with Nomnom:
```bash
pip install asyncpg databases
```

### Enable Gzip Compression

```python
from fastapi.middleware.gzip import GZipMiddleware

app.add_middleware(GZipMiddleware, minimum_size=1000)
```

## Testing in Production

### Smoke Tests

```bash
# Test health endpoint
curl https://your-api.com/health

# Test restaurant search
curl "https://your-api.com/api/v1/restaurants/search?cuisine=Indian"

# Test with authentication
curl -H "X-API-Key: your-key" https://your-api.com/api/v1/restaurants/search
```

### Load Testing

```bash
pip install locust
```

Create `locustfile.py`:
```python
from locust import HttpUser, task, between

class FoodOrderingUser(HttpUser):
    wait_time = between(1, 3)
    
    @task
    def search_restaurants(self):
        self.client.get("/api/v1/restaurants/search?cuisine=Indian")
    
    @task
    def get_menu(self):
        self.client.get("/api/v1/restaurants/rest_001/menu")
```

Run:
```bash
locust -f locustfile.py --host=https://your-api.com
```

## Rollback Plan

If deployment fails:

1. **Railway/Heroku**: Rollback to previous deployment
   ```bash
   railway rollback
   # or
   heroku rollback
   ```

2. **Keep old version running**: Deploy to new URL first, test, then switch

3. **Database migrations**: Always reversible, test on staging first

## Next Steps After Deployment

1. ✅ API deployed and accessible
2. ✅ ChatGPT Custom GPT configured with production URL
3. ✅ Monitoring and alerts set up
4. ⏭️ Test with real users
5. ⏭️ Collect feedback and iterate
6. ⏭️ Integrate with Nomnom API
7. ⏭️ Add real payment processing
8. ⏭️ Scale based on usage

## Cost Estimates

### Free Tier Options
- **Railway**: Free tier available (500 hours/month)
- **Google Cloud Run**: 2 million requests/month free
- **ngrok**: Free with random URLs

### Paid Options
- **Railway Pro**: $5/month
- **DigitalOcean**: $5-10/month
- **Heroku**: $7/month (Eco dyno)
- **AWS Lambda**: Pay per use (~$0.20 per million requests)

## Support & Troubleshooting

### Common Issues

**Issue**: CORS errors in ChatGPT
**Solution**: Add ChatGPT domains to CORS allowed origins

**Issue**: Timeout errors
**Solution**: Optimize slow endpoints, add caching

**Issue**: 502 Bad Gateway
**Solution**: Check if API is running, check logs

**Issue**: High latency
**Solution**: Deploy closer to users, add CDN, optimize database queries

### Getting Help

- Check logs: `tail -f api_calls.log`
- Test endpoints: http://your-api.com/docs
- Monitor uptime: UptimeRobot dashboard
- Error tracking: Sentry dashboard

