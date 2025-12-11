# 🚀 Quick Deployment Guide - Deploy Your Portfolio NOW!

Follow these steps to deploy your portfolio website for **FREE** on Railway (recommended) or Render.

## 🎯 Option 1: Railway (Easiest - Recommended)

### Step 1: Prepare Your Code
1. **Commit your changes** (if not already committed):
   ```powershell
   git add .
   git commit -m "Prepare for deployment"
   git push origin main
   ```

### Step 2: Sign Up for Railway
1. Go to **[railway.app](https://railway.app)** 
2. Click **"Start a New Project"**
3. Sign up with **GitHub** (free tier available)

### Step 3: Deploy Your App
1. In Railway dashboard, click **"New Project"**
2. Select **"Deploy from GitHub repo"**
3. Select your portfolio repository
4. Railway will automatically detect it's a Django app

### Step 4: Add PostgreSQL Database
1. In your Railway project, click **"New"** → **"Database"** → **"PostgreSQL"**
2. Railway automatically sets `DATABASE_URL` environment variable

### Step 5: Configure Environment Variables
1. Go to your project → **"Variables"** tab
2. Click **"New Variable"** and add these:

   **Required Variables:**
   ```
   SECRET_KEY=your-super-secret-key-here
   DEBUG=False
   ```

   **To generate SECRET_KEY, run this locally:**
   ```powershell
   cd backend
   python manage.py shell
   ```
   Then in Python shell:
   ```python
   from django.core.management.utils import get_random_secret_key
   print(get_random_secret_key())
   ```
   Copy the output and use it as your SECRET_KEY.

   **Optional Variables:**
   ```
   OPENAI_API_KEY=your-openai-api-key (if using AI features)
   ```

### Step 6: Deploy!
- Railway will automatically build and deploy
- Watch the build logs in the Railway dashboard
- Your site will be live at: `https://your-app-name.up.railway.app`

### Step 7: Run Initial Setup (After First Deploy)
1. In Railway dashboard, go to your service
2. Click **"Deployments"** → **"View Logs"**
3. Or use Railway CLI to run:
   ```bash
   railway run python manage.py migrate
   railway run python manage.py createsuperuser
   ```

---

## 🎯 Option 2: Render (Alternative)

### Step 1: Sign Up
1. Go to **[render.com](https://render.com)**
2. Sign up with **GitHub**

### Step 2: Create Web Service
1. Click **"New +"** → **"Web Service"**
2. Connect your GitHub repository
3. Render will auto-detect settings from `render.yaml`

### Step 3: Configure
- **Build Command:** `chmod +x ./build.sh && ./build.sh`
- **Start Command:** `cd backend && gunicorn portfolio.wsgi:application`

### Step 4: Add Environment Variables
In Render dashboard → **Environment**:
```
SECRET_KEY=your-super-secret-key-here
DEBUG=False
```

### Step 5: Add Database
1. Click **"New +"** → **"PostgreSQL"**
2. Render will automatically link it

---

## ✅ Post-Deployment Checklist

After deployment, make sure to:

1. **Run Migrations:**
   - Railway: Use Railway CLI or dashboard shell
   - Render: Add to build command or run manually

2. **Create Superuser:**
   ```bash
   python manage.py createsuperuser
   ```

3. **Test Your Site:**
   - Visit your deployed URL
   - Check all pages load correctly
   - Test contact form (if configured)

4. **Set Up Custom Domain (Optional):**
   - Buy a domain (Namecheap, GoDaddy, etc.)
   - Add domain in Railway/Render dashboard
   - Update DNS records as instructed

---

## 🆓 Free Tier Limits

### Railway
- ✅ **500 hours/month** free
- ✅ **1GB RAM**
- ✅ **PostgreSQL database** included
- ✅ **Custom domains** supported

### Render
- ✅ **750 hours/month** free
- ✅ **512MB RAM**
- ✅ **PostgreSQL database** included
- ✅ **Custom domains** supported

---

## 🐛 Troubleshooting

### Build Fails
- Check build logs in dashboard
- Ensure all dependencies in `requirements.txt`
- Verify Python version in `runtime.txt` is supported

### Database Errors
- Ensure `DATABASE_URL` is set automatically
- Run migrations: `python manage.py migrate`

### Static Files Not Loading
- Check `whitenoise` is in `MIDDLEWARE`
- Verify `STATIC_ROOT` is set correctly
- Static files should be collected during build

### 500 Errors
- Check logs in Railway/Render dashboard
- Ensure `DEBUG=False` in production
- Verify `SECRET_KEY` is set

---

## 📝 Quick Commands

**Generate Secret Key:**
```powershell
cd backend
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

**Test Locally Before Deploying:**
```powershell
cd backend
python manage.py collectstatic
python manage.py migrate
python manage.py runserver
```

---

## 🎉 Success!

Once deployed, your portfolio will be live and accessible worldwide!

**Next Steps:**
- Add your projects and content via Django admin
- Customize your profile
- Share your portfolio URL!

---

**Need Help?**
- Railway Docs: [docs.railway.app](https://docs.railway.app)
- Render Docs: [render.com/docs](https://render.com/docs)
- Django Docs: [docs.djangoproject.com](https://docs.djangoproject.com)

