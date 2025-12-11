# 🚀 Vercel Deployment Guide - Step by Step

Complete guide to deploy your Django portfolio on **Vercel** for FREE!

## 🎯 Why Vercel?

- ✅ **100% FREE** - No credit card required
- ✅ **Unlimited deployments**
- ✅ **100GB bandwidth** per month
- ✅ **Automatic HTTPS** (SSL certificates)
- ✅ **Global CDN** for fast performance
- ✅ **Automatic deployments** from GitHub
- ✅ **Serverless** - Scales automatically

## ⚠️ Important Notes About Django on Vercel

Vercel is **serverless**, which means:
- ✅ Great for static files and API endpoints
- ⚠️ Django needs special configuration
- ⚠️ Database should be external (SQLite won't work well)
- ⚠️ Some Django features may need adjustment

**For best results, use:**
- External PostgreSQL database (Render, Railway, or Supabase free tier)
- Or use Vercel Postgres (requires credit card for free tier)

---

## 📋 Prerequisites

- ✅ Your code on GitHub: `https://github.com/Aviyank/Aviyank-Portfolio.git`
- ✅ Vercel account (free)
- ✅ External database (we'll set this up)

---

## 🚀 Step-by-Step Deployment

### Step 1: Set Up External Database (Required)

Since Vercel is serverless, you need an external database. **Choose one:**

#### Option A: Render PostgreSQL (Recommended - Free, No Credit Card)

1. Go to [render.com](https://render.com)
2. Sign up with GitHub
3. Click **"New +"** → **"PostgreSQL"**
4. Name: `portfolio-db`
5. Plan: **Free**
6. Click **"Create Database"**
7. **Copy the External Database URL** (not internal)

#### Option B: Railway PostgreSQL (Alternative)

1. Go to [railway.app](https://railway.app)
2. Sign up with GitHub
3. Click **"New Project"** → **"Database"** → **"PostgreSQL"**
4. Railway auto-sets `DATABASE_URL`
5. Copy the `DATABASE_URL` from Railway dashboard

#### Option C: Supabase (Free PostgreSQL)

1. Go to [supabase.com](https://supabase.com)
2. Sign up (free)
3. Create new project
4. Go to **Settings** → **Database**
5. Copy the **Connection String**

---

### Step 2: Sign Up for Vercel

1. Go to **[vercel.com](https://vercel.com)**
2. Click **"Sign Up"**
3. Sign up with **GitHub** (recommended)
4. Authorize Vercel to access your repositories

---

### Step 3: Create Vercel Project

1. In Vercel dashboard, click **"Add New..."** → **"Project"**
2. Find and select your repository: **Aviyank/Aviyank-Portfolio**
3. Click **"Import"**

---

### Step 4: Configure Project Settings

Vercel will auto-detect some settings, but you need to configure:

**Framework Preset:**
- Select **"Other"** or leave as auto-detected

**Root Directory:**
- Leave as **`.`** (root)

**Build and Output Settings:**
- **Build Command:** 
  ```bash
  pip install -r requirements.txt && cd backend && python manage.py collectstatic --noinput
  ```
- **Output Directory:** 
  ```
  backend
  ```
- **Install Command:** 
  ```bash
  pip install -r requirements.txt
  ```

**Note:** Vercel uses `vercel.json` for configuration (we'll create this).

---

### Step 5: Add Environment Variables

Click **"Environment Variables"** and add:

**Required Variables:**
```
SECRET_KEY=t+ee)x8ii9xy2b46rxxr==iji!8s%_y+n#ui+lz9f^y9%h-(y9
DEBUG=False
ALLOWED_HOSTS=*.vercel.app,your-app-name.vercel.app,localhost,127.0.0.1
DATABASE_URL=postgresql://user:password@host:port/database
DJANGO_SETTINGS_MODULE=portfolio.settings
PYTHON_VERSION=3.11
```

**Important:**
- Replace `DATABASE_URL` with your actual database connection string from Step 1
- Replace `your-app-name.vercel.app` with your actual Vercel domain (you'll see it after deployment)

**Optional Variables:**
```
OPENAI_API_KEY=your-openai-api-key-here
```

---

### Step 6: Create vercel.json Configuration

I've already created `vercel.json` in your repo. It should look like this:

```json
{
  "version": 2,
  "builds": [
    {
      "src": "backend/wsgi.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/static/(.*)",
      "dest": "/backend/static/$1"
    },
    {
      "src": "/media/(.*)",
      "dest": "/backend/media/$1"
    },
    {
      "src": "/(.*)",
      "dest": "backend/wsgi.py"
    }
  ],
  "env": {
    "PYTHON_VERSION": "3.11"
  }
}
```

This file is already in your repo! Vercel will use it automatically.

---

### Step 7: Update Django Settings for Vercel

We need to ensure Django works with Vercel's serverless environment. Let me check and update your settings:

**The `vercel.json` file handles routing, but we may need to adjust Django settings.**

---

### Step 8: Deploy!

1. Review all settings
2. Click **"Deploy"**
3. Vercel will:
   - Install dependencies
   - Build your app
   - Deploy to global CDN
   - Provide you with a URL

**Deployment takes 2-5 minutes.**

---

### Step 9: Run Migrations

After deployment:

1. Go to your Vercel project dashboard
2. Click **"Functions"** tab
3. Or use Vercel CLI (if installed):
   ```bash
   vercel env pull .env.local
   cd backend
   python manage.py migrate
   ```

**Alternative:** Use Vercel's serverless function to run migrations, or run them locally pointing to your production database.

**Easiest Method - Run Migrations Locally:**
```powershell
# Set your production DATABASE_URL locally
$env:DATABASE_URL="your-production-database-url"
cd backend
python manage.py migrate
python manage.py createsuperuser
```

---

### Step 10: Access Your Site!

Your portfolio is now live at:
```
https://your-app-name.vercel.app
```

Access admin panel at:
```
https://your-app-name.vercel.app/admin/
```

---

## 🔧 Additional Configuration

### Static Files Configuration

Vercel handles static files automatically through the `vercel.json` routes. However, you may need to:

1. **Ensure static files are collected:**
   - Build command includes `collectstatic`
   - Static files are in `backend/staticfiles/`

2. **Update settings.py for Vercel:**
   ```python
   STATIC_URL = '/static/'
   STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
   ```

### Media Files

For media files (user uploads), you'll need external storage:
- **Vercel Blob Storage** (requires credit card)
- **Cloudinary** (free tier available)
- **AWS S3** (free tier available)
- Or use external database for small files

---

## 🐛 Troubleshooting

### Build Fails

**Issue:** Build command fails
- **Solution:** 
  - Check build logs in Vercel dashboard
  - Ensure `requirements.txt` has all dependencies
  - Verify Python version (3.11)

**Issue:** Module not found errors
- **Solution:**
  - Check all dependencies in `requirements.txt`
  - Ensure `gunicorn` and `whitenoise` are included (they are!)

### Database Connection Issues

**Issue:** Can't connect to database
- **Solution:**
  - Verify `DATABASE_URL` is set correctly
  - Use **external** database URL (not internal)
  - Check database is accessible from internet
  - Ensure `dj-database-url` is in requirements.txt

### Static Files Not Loading

**Issue:** CSS/JS/images return 404
- **Solution:**
  - Verify `collectstatic` ran during build
  - Check `vercel.json` routes for `/static/`
  - Ensure `STATIC_ROOT` is set correctly
  - Check build logs for static file collection

### 500 Errors

**Issue:** Getting 500 Internal Server Error
- **Solution:**
  - Check function logs in Vercel dashboard
  - Verify all environment variables are set
  - Run migrations: `python manage.py migrate`
  - Check `ALLOWED_HOSTS` includes your Vercel domain

### Function Timeout

**Issue:** Request timeout errors
- **Solution:**
  - Vercel free tier has 10-second timeout for serverless functions
  - Optimize your views to respond quickly
  - Consider using Vercel Pro for longer timeouts

---

## 📊 Vercel Free Tier Limits

- ✅ **Unlimited deployments**
- ✅ **100GB bandwidth** per month
- ✅ **100 serverless function invocations** per day
- ✅ **Automatic HTTPS**
- ✅ **Global CDN**
- ⚠️ **10-second function timeout** (free tier)
- ⚠️ **100 function invocations/day** (free tier)

---

## ✅ Post-Deployment Checklist

After deployment, verify:

- [ ] Site loads at your Vercel URL
- [ ] Static files (CSS, JS, images) load correctly
- [ ] Admin panel accessible at `/admin/`
- [ ] Database migrations ran successfully
- [ ] Can create superuser and login
- [ ] All pages render correctly
- [ ] API endpoints work (if using)
- [ ] Contact form works (if configured)

---

## 🔄 Updating Your Site

To update your deployed site:

1. **Make changes** to your code locally
2. **Commit and push** to GitHub:
   ```powershell
   git add .
   git commit -m "Update portfolio"
   git push origin main
   ```
3. **Vercel automatically redeploys** (if auto-deploy is enabled)
4. Or **manually trigger** redeploy from Vercel dashboard

---

## 📝 Environment Variables Reference

Complete list of environment variables:

```bash
# Required
SECRET_KEY=t+ee)x8ii9xy2b46rxxr==iji!8s%_y+n#ui+lz9f^y9%h-(y9
DEBUG=False
ALLOWED_HOSTS=*.vercel.app,your-app-name.vercel.app,localhost,127.0.0.1
DATABASE_URL=postgresql://user:password@host:port/database
DJANGO_SETTINGS_MODULE=portfolio.settings
PYTHON_VERSION=3.11

# Optional - AI Features
OPENAI_API_KEY=your-openai-api-key-here

# Optional - Media Storage
CLOUDINARY_URL=your-cloudinary-url
```

---

## 🎉 Success!

Your Django portfolio is now live on Vercel!

**Next Steps:**
1. Add your content via admin panel
2. Customize your profile
3. Upload projects and blog posts
4. (Optional) Add custom domain in Vercel settings

---

## 📞 Need Help?

- **Vercel Docs:** https://vercel.com/docs
- **Vercel Discord:** https://vercel.com/discord
- **Django on Vercel:** https://vercel.com/guides/deploying-django-with-vercel

---

## 🚀 Quick Command Reference

**Install Vercel CLI (optional):**
```powershell
npm i -g vercel
```

**Deploy via CLI:**
```powershell
vercel
```

**View logs:**
```powershell
vercel logs
```

**Run migrations locally (pointing to production DB):**
```powershell
$env:DATABASE_URL="your-production-database-url"
cd backend
python manage.py migrate
python manage.py createsuperuser
```

---

**Happy deploying! Your portfolio will be live on Vercel in minutes! 🎉**

