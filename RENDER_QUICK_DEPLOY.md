# 🚀 Render Quick Deploy Guide

**Easiest alternative to Railway!** Your project already has `render.yaml` configured, so deployment is super simple.

## ⚡ 5-Minute Deployment

### Step 1: Sign Up
1. Go to **[render.com](https://render.com)**
2. Click **"Get Started for Free"**
3. Sign up with **GitHub** (recommended)

### Step 2: Deploy from Blueprint (Easiest Method)
1. In Render dashboard, click **"New +"**
2. Select **"Blueprint"**
3. Connect your GitHub account if not already connected
4. Select your repository: **Aviyank/Aviyank-Portfolio**
5. Render will automatically detect `render.yaml` and configure everything!
6. Click **"Apply"**

**That's it!** Render will:
- ✅ Create web service
- ✅ Create PostgreSQL database
- ✅ Set up environment variables
- ✅ Deploy your app

### Step 3: Update SECRET_KEY (Important!)
1. Once deployed, go to your **Web Service** (django-portfolio)
2. Click on **"Environment"** tab
3. Find `SECRET_KEY` (Render generates one, but you can update it)
4. Click **"Edit"** and set it to:
   ```
   t+ee)x8ii9xy2b46rxxr==iji!8s%_y+n#ui+lz9f^y9%h-(y9
   ```
5. Click **"Save Changes"**

### Step 4: Access Your Site
- Your site will be live at: `https://django-portfolio.onrender.com`
- (Or whatever name Render assigns)

### Step 5: Create Admin User
1. Go to your **Web Service** → **"Shell"** tab
2. Run:
   ```bash
   cd backend
   python manage.py migrate
   python manage.py createsuperuser
   ```
3. Follow prompts to create admin account

### Step 6: Access Admin Panel
- Go to: `https://django-portfolio.onrender.com/admin/`
- Login and start adding content!

---

## 🎯 Manual Deployment (If Blueprint Doesn't Work)

### 1. Create PostgreSQL Database
1. Click **"New +"** → **"PostgreSQL"**
2. Name: `django-portfolio-db`
3. Database: `django_portfolio`
4. User: `django_portfolio_user`
5. Plan: **Free**
6. Click **"Create Database"**
7. Copy the **Internal Database URL**

### 2. Create Web Service
1. Click **"New +"** → **"Web Service"**
2. Connect GitHub repo: **Aviyank/Aviyank-Portfolio**
3. Configure:
   - **Name:** `django-portfolio`
   - **Environment:** `Python 3`
   - **Build Command:** `chmod +x ./build.sh && ./build.sh`
   - **Start Command:** `cd backend && gunicorn portfolio.wsgi:application`
   - **Plan:** Free

### 3. Add Environment Variables
In your web service → **Environment** tab, add:
```
SECRET_KEY=t+ee)x8ii9xy2b46rxxr==iji!8s%_y+n#ui+lz9f^y9%h-(y9
DEBUG=False
ALLOWED_HOSTS=.onrender.com,localhost,127.0.0.1
DATABASE_URL=<paste Internal Database URL from step 1>
PYTHON_VERSION=3.11.7
```

### 4. Deploy!
- Click **"Create Web Service"**
- Wait for deployment (2-5 minutes)

---

## 📊 Render Free Tier

- ✅ **750 hours/month** (more than Railway!)
- ✅ **512MB RAM**
- ✅ **PostgreSQL database** included
- ✅ **Automatic SSL** (HTTPS)
- ✅ **Custom domains** supported
- ⚠️ **Note:** Free tier spins down after 15 minutes of inactivity (first request may be slow)

---

## 🔧 Troubleshooting

### Build Fails
- Check build logs in Render dashboard
- Ensure `build.sh` has execute permissions (it does in your repo)
- Verify Python 3.11.7 is available

### Database Connection Issues
- Verify `DATABASE_URL` is set correctly
- Use **Internal Database URL** (not external)
- Check database is running in Render dashboard

### Static Files Not Loading
- Static files are collected during build automatically
- Check `whitenoise` is in MIDDLEWARE (it is!)
- Verify build logs show `collectstatic` ran successfully

### 500 Errors
- Check logs in Render dashboard → **Logs** tab
- Ensure `SECRET_KEY` is set
- Verify `DEBUG=False` in production

### Slow First Load
- Free tier apps spin down after 15 min inactivity
- First request after spin-down takes ~30 seconds
- This is normal for free tier

---

## 🎉 Success!

Your portfolio is now live on Render!

**Next Steps:**
1. Add your content via admin panel
2. Customize your profile
3. (Optional) Add custom domain in Render settings

---

## 📝 Your Configuration

Your `render.yaml` is already set up with:
- ✅ Web service configuration
- ✅ PostgreSQL database
- ✅ Environment variables
- ✅ Build and start commands

**Just deploy and go!** 🚀

