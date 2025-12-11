# 🚀 Free Deployment Guide - AI Portfolio

This guide will help you deploy your Django portfolio for **FREE** using Railway.

## 🎯 Quick Start (5 minutes)

### Option 1: Railway (Recommended - Easiest)

1. **Sign up for Railway**
   - Go to [railway.app](https://railway.app)
   - Sign up with GitHub (free tier available)

2. **Deploy from GitHub**
   - Click "New Project" → "Deploy from GitHub repo"
   - Select your portfolio repository
   - Railway will automatically detect it's a Django app

3. **Configure Environment Variables**
   - Go to your project settings
   - Add these environment variables:
   ```
   SECRET_KEY=your-super-secret-key-here
   DEBUG=False
   OPENAI_API_KEY=your-openai-api-key (optional)
   ```

4. **Add Database (Free PostgreSQL)**
   - In Railway dashboard, click "New" → "Database" → "PostgreSQL"
   - Railway will automatically set `DATABASE_URL`

5. **Deploy!**
   - Railway will automatically build and deploy your app
   - Your site will be live at `https://your-app-name.railway.app`

### Option 2: Render (Alternative)

1. **Sign up for Render**
   - Go to [render.com](https://render.com)
   - Sign up with GitHub

2. **Create Web Service**
   - Click "New" → "Web Service"
   - Connect your GitHub repo
   - Set build command: `pip install -r requirements.txt`
   - Set start command: `gunicorn portfolio.wsgi:application`

3. **Configure Environment**
   - Add environment variables in Render dashboard
   - Add PostgreSQL database service

## 🔧 Manual Setup (If needed)

### 1. Prepare Your Code

Your project is already prepared with:
- ✅ `Procfile` - Tells Railway how to run the app
- ✅ `requirements.txt` - Lists all dependencies
- ✅ `runtime.txt` - Specifies Python version
- ✅ `build.sh` - Build script for deployment
- ✅ Production settings in `portfolio/production.py`

### 2. Environment Variables

Set these in your hosting platform:

```bash
# Required
SECRET_KEY=your-super-secret-key-here
DEBUG=False

# Database (Railway/Render will provide this)
DATABASE_URL=postgresql://...

# Optional - AI Features
OPENAI_API_KEY=your-openai-api-key

# Optional - Custom Domain
CUSTOM_DOMAIN=your-domain.com
```

### 3. Generate Secret Key

Run this in Python to generate a secure secret key:

```python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

## 🌐 Custom Domain (Optional)

1. **Buy a domain** (Namecheap, GoDaddy, etc.)
2. **In Railway/Render dashboard:**
   - Go to your app settings
   - Add custom domain
   - Update DNS records as instructed

## 📊 Free Tier Limits

### Railway
- ✅ 500 hours/month free
- ✅ 1GB RAM
- ✅ Shared CPU
- ✅ PostgreSQL database included
- ✅ Custom domains supported

### Render
- ✅ 750 hours/month free
- ✅ 512MB RAM
- ✅ Shared CPU
- ✅ PostgreSQL database included
- ✅ Custom domains supported

## 🛠️ Troubleshooting

### Common Issues:

1. **Build fails**
   - Check `requirements.txt` has all dependencies
   - Ensure Python version in `runtime.txt` is supported

2. **Database errors**
   - Make sure `DATABASE_URL` is set
   - Run migrations: `python manage.py migrate`

3. **Static files not loading**
   - Check `STATIC_ROOT` is set correctly
   - Ensure `whitenoise` is in `MIDDLEWARE`

4. **500 errors**
   - Check logs in Railway/Render dashboard
   - Ensure `DEBUG=False` in production

### Debug Commands:

```bash
# Check if app runs locally
python manage.py runserver

# Test static files
python manage.py collectstatic

# Check database
python manage.py migrate --plan
```

## 🎉 Success!

Once deployed, your portfolio will be live at:
- Railway: `https://your-app-name.railway.app`
- Render: `https://your-app-name.onrender.com`

## 🔄 Updates

To update your deployed site:
1. Push changes to GitHub
2. Railway/Render will automatically redeploy
3. Or manually trigger redeploy from dashboard

## 📞 Support

- Railway Docs: [docs.railway.app](https://docs.railway.app)
- Render Docs: [render.com/docs](https://render.com/docs)
- Django Docs: [docs.djangoproject.com](https://docs.djangoproject.com)

---

**🎯 Pro Tip:** Start with Railway - it's the easiest and most reliable free option for Django apps! 