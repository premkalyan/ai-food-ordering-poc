# GitHub Setup & Push Instructions

## ✅ Git Repository Ready

Your local git repository is initialized and committed with all files.

**Status**: 
- ✅ Git initialized
- ✅ All files committed
- ✅ Branch: `main`
- ⏭️ Ready to push to GitHub

## 🚀 Quick Push to GitHub

### Option 1: GitHub CLI (Recommended)

```bash
cd /Users/premkalyan/code/CORP/ai-food-ordering-poc

# Authenticate (if needed)
gh auth login

# Create repo and push
gh repo create ai-food-ordering-poc --public --source=. --remote=origin --push

# That's it! Repository created and code pushed.
```

### Option 2: GitHub Web UI + Git Push

**Step 1: Create Repository on GitHub**

1. Go to https://github.com/new
2. Repository name: `ai-food-ordering-poc`
3. Description: `AI-powered food ordering POC - ChatGPT Custom GPT integration with mock restaurant API`
4. Visibility: **Public** (so Vercel can access it)
5. **DO NOT** initialize with README, .gitignore, or license
6. Click "Create repository"

**Step 2: Push Your Code**

```bash
cd /Users/premkalyan/code/CORP/ai-food-ordering-poc

# Add GitHub as remote
git remote add origin https://github.com/premkalyan/ai-food-ordering-poc.git

# Push to GitHub
git push -u origin main
```

### Option 3: SSH (If you prefer SSH)

```bash
cd /Users/premkalyan/code/CORP/ai-food-ordering-poc

# Add GitHub as remote (SSH)
git remote add origin git@github.com:premkalyan/ai-food-ordering-poc.git

# Push to GitHub
git push -u origin main
```

## 📋 What Gets Pushed

All these files will be in your GitHub repo:

```
ai-food-ordering-poc/
├── .env.example              # Environment variables template
├── .gitignore               # Git ignore rules
├── .vercelignore            # Vercel ignore rules
├── vercel.json              # Vercel configuration
├── requirements.txt         # Python dependencies
├── main.py                  # FastAPI application (300+ lines)
├── mock_data.py            # Mock restaurants & menus (600+ lines)
├── test_api.py             # Test suite (200+ lines)
├── api/
│   └── index.py            # Vercel serverless entry point
└── Documentation:
    ├── README.md           # Project overview
    ├── QUICK_START.md      # 5-minute setup
    ├── CHATGPT_SETUP.md    # Custom GPT guide
    ├── DEPLOYMENT.md       # Deployment options
    ├── VERCEL_DEPLOYMENT.md # Vercel-specific guide
    ├── NOMNOM_INTEGRATION.md # Nomnom integration
    ├── ARCHITECTURE.md     # Technical architecture
    ├── PITCH_DECK.md       # Partnership pitch
    └── EXECUTIVE_SUMMARY.md # Business case
```

**Total**: 18 files, 5274 lines of code + documentation

## 🔒 Security Note

The `.gitignore` file ensures these are **NOT** pushed:
- `.env` (your actual environment variables)
- `__pycache__/` (Python cache)
- `*.log` (log files)
- `venv/` (virtual environment)

Only `.env.example` is pushed (safe template without secrets).

## ✅ Verify Push

After pushing, verify at:
```
https://github.com/premkalyan/ai-food-ordering-poc
```

You should see:
- All 18 files
- README.md displayed on homepage
- Green "Public" badge
- Your commit message

## 🚀 Next Step: Deploy to Vercel

Once code is on GitHub, deploy to Vercel:

### Method 1: Vercel Dashboard (Easiest)

1. Go to https://vercel.com/new
2. Click "Import Git Repository"
3. Select `premkalyan/ai-food-ordering-poc`
4. Framework Preset: **Other**
5. Root Directory: `./`
6. Build Command: (leave empty)
7. Output Directory: (leave empty)
8. Install Command: `pip install -r requirements.txt`
9. Click **Deploy**

### Method 2: Vercel CLI

```bash
cd /Users/premkalyan/code/CORP/ai-food-ordering-poc

# Install Vercel CLI (if not installed)
npm install -g vercel

# Login to Vercel
vercel login

# Deploy
vercel --prod
```

## 📊 After Deployment

You'll get a URL like:
```
https://ai-food-ordering-poc.vercel.app
```

Test it:
```bash
# Health check
curl https://ai-food-ordering-poc.vercel.app/health

# Restaurant search
curl "https://ai-food-ordering-poc.vercel.app/api/v1/restaurants/search?cuisine=Indian"

# API docs
open https://ai-food-ordering-poc.vercel.app/docs
```

## 🤖 Update ChatGPT Custom GPT

Once deployed, update your Custom GPT's OpenAPI schema:

Replace:
```json
"servers": [
  {
    "url": "http://localhost:8000"
  }
]
```

With:
```json
"servers": [
  {
    "url": "https://ai-food-ordering-poc.vercel.app"
  }
]
```

## 🔄 Continuous Deployment

Every time you push to `main` branch:
1. GitHub triggers Vercel
2. Vercel automatically deploys
3. Your live URL updates

To make changes:
```bash
# Make your changes
# ...

# Commit and push
git add .
git commit -m "Your change description"
git push

# Vercel automatically deploys!
```

## 🌿 Branch Deployments

Create a feature branch:
```bash
git checkout -b feature-name
# Make changes
git push -u origin feature-name
```

Vercel creates preview URL:
```
https://ai-food-ordering-poc-git-feature-name.vercel.app
```

## 📝 Repository Settings

### Recommended Settings

1. **Branch Protection** (optional for POC):
   - Settings → Branches → Add rule
   - Branch name pattern: `main`
   - Require pull request reviews

2. **About Section**:
   - Add description
   - Add topics: `ai`, `chatgpt`, `food-ordering`, `fastapi`, `vercel`
   - Add website: Your Vercel URL

3. **README Badges** (optional):
   Add to README.md:
   ```markdown
   ![Vercel](https://img.shields.io/badge/vercel-deployed-success)
   ![Python](https://img.shields.io/badge/python-3.11+-blue)
   ![FastAPI](https://img.shields.io/badge/fastapi-latest-green)
   ```

## 🆘 Troubleshooting

### Issue: Authentication failed

**Solution**: Re-authenticate GitHub CLI
```bash
gh auth login
# Follow prompts
```

### Issue: Remote already exists

**Solution**: Remove and re-add
```bash
git remote remove origin
git remote add origin https://github.com/premkalyan/ai-food-ordering-poc.git
git push -u origin main
```

### Issue: Permission denied (publickey)

**Solution**: Use HTTPS instead of SSH
```bash
git remote set-url origin https://github.com/premkalyan/ai-food-ordering-poc.git
git push
```

### Issue: Repository already exists

**Solution**: Delete the repo on GitHub and recreate, or push to existing:
```bash
git remote add origin https://github.com/premkalyan/ai-food-ordering-poc.git
git push -u origin main
```

## ✅ Success Checklist

- [ ] Code pushed to GitHub
- [ ] Repository is public
- [ ] All files visible on GitHub
- [ ] README displays correctly
- [ ] Connected to Vercel
- [ ] Vercel deployment successful
- [ ] API accessible at Vercel URL
- [ ] ChatGPT Custom GPT updated with Vercel URL
- [ ] End-to-end ordering test successful

## 🎉 You're Done!

Once completed:
1. ✅ Code on GitHub: `https://github.com/premkalyan/ai-food-ordering-poc`
2. ✅ API live on Vercel: `https://ai-food-ordering-poc.vercel.app`
3. ✅ ChatGPT Custom GPT connected
4. ✅ Ready to demo!

---

**Need Help?**
- GitHub Docs: https://docs.github.com
- Vercel Docs: https://vercel.com/docs
- Check VERCEL_DEPLOYMENT.md for Vercel-specific help

