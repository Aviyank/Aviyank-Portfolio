# 🚀 Quick Start - Deploy Your Portfolio in 5 Minutes

## ⚡ Super Quick Deployment

### Step 1: Push to GitHub
```bash
git add .
git commit -m "Ready for deployment"
git push origin main
```

### Step 2: Deploy to Railway
1. Go to [railway.app](https://railway.app)
2. Sign up with GitHub
3. Click "New Project" → "Deploy from GitHub repo"
4. Select your portfolio repository
5. Railway will auto-detect it's a Django app

### Step 3: Add Environment Variables
In Railway dashboard → Variables tab, add:
```
SECRET_KEY=your-secret-key-here
DEBUG=False
```

### Step 4: Add Database
1. In Railway dashboard, click "New" → "Database" → "PostgreSQL"
2. Railway will automatically set `DATABASE_URL`

### Step 5: Done! 🎉
Your portfolio will be live at: `https://your-app-name.railway.app`

---

## 🔧 Generate Secret Key
Run this in Python to get a secure secret key:
```python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

## 📱 Optional: Custom Domain
1. Buy a domain (Namecheap, GoDaddy, etc.)
2. In Railway → Settings → Domains → Add custom domain
3. Update DNS records as instructed

## 🆘 Need Help?
- See `DEPLOYMENT.md` for detailed instructions
- Railway Docs: [docs.railway.app](https://docs.railway.app)
- Your app is already configured for deployment! ✅ 