# Vercel Deployment Guide

## Quick Deployment Steps

### 1. Push to GitHub

```bash
cd /Users/premkalyan/code/CORP/ai-food-ordering-poc

# Initialize git (if not already done)
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit: AI Food Ordering POC"

# Create GitHub repo and push
# (GitHub repo will be created separately)
git remote add origin https://github.com/premkalyan/ai-food-ordering-poc.git
git branch -M main
git push -u origin main
```

### 2. Deploy to Vercel

**Option A: Vercel CLI (Recommended)**

```bash
# Install Vercel CLI
npm install -g vercel

# Login to Vercel
vercel login

# Deploy
cd /Users/premkalyan/code/CORP/ai-food-ordering-poc
vercel

# Follow prompts:
# - Set up and deploy? Yes
# - Which scope? Your account
# - Link to existing project? No
# - Project name? ai-food-ordering-poc
# - Directory? ./
# - Override settings? No

# Production deployment
vercel --prod
```

**Option B: Vercel Dashboard (Easiest)**

1. Go to https://vercel.com
2. Click "Add New Project"
3. Import from GitHub: `premkalyan/ai-food-ordering-poc`
4. Framework Preset: "Other"
5. Build Command: (leave empty)
6. Output Directory: (leave empty)
7. Install Command: `pip install -r requirements.txt`
8. Click "Deploy"

### 3. Get Your Vercel URL

After deployment, you'll get a URL like:
```
https://ai-food-ordering-poc.vercel.app
```

Or with your custom domain:
```
https://ai-food-ordering-poc-premkalyan.vercel.app
```

### 4. Test the Deployment

```bash
# Test health endpoint
curl https://ai-food-ordering-poc.vercel.app/health

# Test restaurant search
curl "https://ai-food-ordering-poc.vercel.app/api/v1/restaurants/search?cuisine=Indian"

# View API docs
open https://ai-food-ordering-poc.vercel.app/docs
```

### 5. Update ChatGPT Custom GPT

In your Custom GPT configuration, update the server URL in the OpenAPI schema:

```json
{
  "servers": [
    {
      "url": "https://ai-food-ordering-poc.vercel.app"
    }
  ]
}
```

## Vercel Configuration

### Files for Vercel

1. **vercel.json** - Vercel configuration
   - Defines build settings
   - Routes configuration
   - Environment variables

2. **api/index.py** - Serverless function entry point
   - Required for Vercel Python runtime
   - Imports and exposes FastAPI app

3. **.vercelignore** - Files to exclude from deployment
   - Test files
   - Documentation
   - Local development files

### Environment Variables

Set in Vercel Dashboard:

1. Go to your project settings
2. Navigate to "Environment Variables"
3. Add:
   - `API_KEY` (optional, for future authentication)
   - `LOG_LEVEL` = `INFO`

## Vercel Features

### Automatic Benefits

✅ **HTTPS by default** - Secure connections  
✅ **Global CDN** - Fast worldwide  
✅ **Auto-scaling** - Handles traffic spikes  
✅ **Zero config** - Works out of the box  
✅ **Git integration** - Auto-deploy on push  
✅ **Preview deployments** - Test before production  

### Limitations (Free Tier)

- **Execution time**: 10 seconds max per request
- **Payload size**: 5MB max
- **Bandwidth**: 100GB/month
- **Deployments**: Unlimited

These limits are fine for our POC!

## Continuous Deployment

Once connected to GitHub, every push to `main` branch will:

1. Trigger automatic deployment
2. Run build process
3. Deploy to production
4. Update your live URL

### Branch Deployments

Every branch gets its own preview URL:
- `main` → https://ai-food-ordering-poc.vercel.app
- `feature-x` → https://ai-food-ordering-poc-git-feature-x.vercel.app

## Monitoring

### View Logs

```bash
# View deployment logs
vercel logs

# View real-time logs
vercel logs --follow

# View specific deployment
vercel logs [deployment-url]
```

### Vercel Dashboard

Access at https://vercel.com/dashboard:
- Deployment history
- Analytics
- Error tracking
- Performance metrics

## Troubleshooting

### Issue: Module not found

**Solution**: Ensure all dependencies are in `requirements.txt`

```bash
pip freeze > requirements.txt
git add requirements.txt
git commit -m "Update dependencies"
git push
```

### Issue: 404 on API routes

**Solution**: Check `vercel.json` routes configuration

### Issue: Timeout errors

**Solution**: Vercel has 10s execution limit. Optimize slow endpoints.

### Issue: CORS errors

**Solution**: Already configured in `main.py` with:
```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

## Custom Domain (Optional)

### Add Custom Domain

1. Go to Project Settings → Domains
2. Add your domain: `api.yourcompany.com`
3. Update DNS records as instructed
4. SSL certificate auto-generated

### Update ChatGPT

Update OpenAPI schema with custom domain:
```json
{
  "servers": [
    {
      "url": "https://api.yourcompany.com"
    }
  ]
}
```

## Rollback

If deployment fails:

```bash
# List deployments
vercel ls

# Rollback to previous deployment
vercel rollback [deployment-url]
```

Or in Vercel Dashboard:
1. Go to Deployments
2. Find working deployment
3. Click "Promote to Production"

## Performance Optimization

### Enable Caching

Add to response headers (already in FastAPI):
```python
@app.get("/api/v1/restaurants/search")
async def search_restaurants(...):
    # Vercel will cache this for 5 minutes
    return Response(
        content=json.dumps(restaurants),
        headers={"Cache-Control": "public, max-age=300"}
    )
```

### Monitor Performance

Check Vercel Analytics:
- Response times
- Error rates
- Traffic patterns
- Geographic distribution

## Security

### API Key Authentication (Future)

When ready to add authentication:

1. Set environment variable in Vercel:
   ```
   API_KEY=your-secret-key-here
   ```

2. Update `main.py` to validate API key

3. Update ChatGPT Custom GPT with authentication

## Cost Estimates

### Vercel Pricing

**Hobby (Free)**:
- Perfect for POC
- 100GB bandwidth/month
- Unlimited deployments
- Community support

**Pro ($20/month)**:
- 1TB bandwidth
- Priority support
- Team collaboration
- Analytics

**Enterprise (Custom)**:
- Custom limits
- SLA guarantees
- Advanced security

### When to Upgrade

Upgrade when you hit:
- 100GB bandwidth/month
- Need team collaboration
- Require SLA guarantees

For POC and initial launch, **Free tier is perfect!**

## Next Steps After Deployment

1. ✅ Deploy to Vercel
2. ✅ Test all endpoints
3. ✅ Update ChatGPT Custom GPT with Vercel URL
4. ✅ Test complete ordering flow
5. ⏭️ Share with team for feedback
6. ⏭️ Monitor usage and performance
7. ⏭️ Integrate Nomnom API when ready

## Support

- **Vercel Docs**: https://vercel.com/docs
- **Vercel Support**: https://vercel.com/support
- **FastAPI on Vercel**: https://vercel.com/guides/python-fastapi

## Quick Commands Reference

```bash
# Deploy to preview
vercel

# Deploy to production
vercel --prod

# View logs
vercel logs

# List deployments
vercel ls

# Remove deployment
vercel rm [deployment-url]

# Open project in browser
vercel open

# Check project info
vercel inspect
```

---

**Ready to deploy!** 🚀

Once deployed, your API will be live at:
`https://ai-food-ordering-poc.vercel.app`

Then update your ChatGPT Custom GPT with this URL and start ordering food!

