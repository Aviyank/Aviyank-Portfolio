# 🚀 Koyeb Deployment Guide

Complete guide to deploy your Django portfolio on **Koyeb** for FREE!

## 🎯 Why Koyeb?

- ✅ **Simple deployment** process
- ✅ **Global edge network** for fast performance
- ✅ **Auto-scaling** capabilities
- ✅ **Automatic HTTPS** (SSL certificates)

## ⚠️ Important: Koyeb Pricing

**Hobby Plan (Free, No Credit Card):**
- ✅ 1 web service
- ✅ 512MB RAM
- ✅ 2GB SSD storage
- ❌ **No PostgreSQL database included** (would need external DB)
- ❌ Limited features

**Starter Plan (Free Services, But Requires Credit Card):**
- ✅ 1 free web service
- ✅ 1 free database
- ⚠️ **Requires payment method** (pay-per-use for additional resources)
- ⚠️ Charges apply if you exceed free tier limits

**Note:** For a truly free Django deployment with database, consider **Render** or **Railway** instead (see alternatives below).

---

## 📋 Prerequisites

- ✅ Your code is on GitHub: `https://github.com/Aviyank/Aviyank-Portfolio.git`
- ✅ Python 3.11.7 (specified in `runtime.txt`)
- ✅ All dependencies in `requirements.txt`

---

## 🚀 Step-by-Step Deployment

### Step 1: Sign Up for Koyeb

1. Go to **[koyeb.com](https://www.koyeb.com)**
2. Click **"Sign Up"** or **"Get Started"**
3. Sign up with **GitHub** (recommended - easiest way)
4. Authorize Koyeb to access your GitHub repositories

### Step 2: Create PostgreSQL Database

1. In Koyeb dashboard, click **"Create"** → **"Database"**
2. Select **"PostgreSQL"**
3. Configure:
   - **Name:** `portfolio-db` (or any name you prefer)
   - **Region:** Choose closest to you (e.g., `us-east`)
   - **Plan:** **Starter** (Free tier)
4. Click **"Create Database"**
5. **Important:** Copy the **Connection String** - you'll need it!
   - It looks like: `postgresql://user:password@host:port/database`

### Step 3: Create Web Service

1. In Koyeb dashboard, click **"Create"** → **"Web Service"**
2. Select **"GitHub"** as source
3. Find and select your repository: **Aviyank/Aviyank-Portfolio**
4. Click **"Deploy"**

### Step 4: Configure Build Settings

In the deployment configuration:

**Build Settings:**
- **Build Command:** 
  ```
  pip install -r requirements.txt && cd backend && python manage.py collectstatic --noinput
  ```
- **Run Command:**
  ```
  cd backend && gunicorn portfolio.wsgi:application --bind 0.0.0.0:$PORT
  ```
- **Port:** Koyeb will auto-detect, but ensure it's set to `$PORT`

**Environment Variables:**
Click **"Environment Variables"** and add:

```
SECRET_KEY=t+ee)x8ii9xy2b46rxxr==iji!8s%_y+n#ui+lz9f^y9%h-(y9
DEBUG=False
ALLOWED_HOSTS=your-app-name.koyeb.app,localhost,127.0.0.1
DATABASE_URL=<paste the PostgreSQL connection string from Step 2>
DJANGO_SETTINGS_MODULE=portfolio.settings
PORT=8000
```

**Important Notes:**
- Replace `<paste the PostgreSQL connection string>` with the actual connection string from Step 2
- Replace `your-app-name.koyeb.app` with your actual Koyeb app URL (you'll see it after deployment)

### Step 5: Deploy!

1. Review all settings
2. Click **"Deploy"**
3. Koyeb will:
   - Clone your repository
   - Install dependencies
   - Collect static files
   - Start your Django app

### Step 6: Run Migrations

After deployment completes:

1. Go to your **Web Service** in Koyeb dashboard
2. Click on **"Shell"** or **"Logs"** tab
3. Run migrations:
   ```bash
   cd backend
   python manage.py migrate
   ```

**Alternative:** You can also SSH into your service if Koyeb provides that option.

### Step 7: Create Superuser

In the same shell, run:
```bash
cd backend
python manage.py createsuperuser
```

Follow prompts to create your admin account.

### Step 8: Access Your Site!

Your portfolio is now live at:
```
https://your-app-name.koyeb.app
```

Access admin panel at:
```
https://your-app-name.koyeb.app/admin/
```

---

## 🔧 Advanced Configuration

### Using Koyeb Configuration File (Optional)

You can create a `koyeb.yaml` file in your repo root for easier configuration:

```yaml
services:
  - name: django-portfolio
    type: web
    build:
      type: dockerfile
      dockerfile_path: ./Dockerfile
    env:
      - name: SECRET_KEY
        value: t+ee)x8ii9xy2b46rxxr==iji!8s%_y+n#ui+lz9f^y9%h-(y9
      - name: DEBUG
        value: "False"
      - name: DATABASE_URL
        secret: DATABASE_URL
```

However, for Django apps, the manual configuration above is simpler.

### Custom Domain

1. In Koyeb dashboard → Your Web Service → **"Domains"**
2. Click **"Add Domain"**
3. Enter your domain name
4. Update DNS records as instructed by Koyeb
5. Update `ALLOWED_HOSTS` environment variable to include your domain

---

## 📊 Koyeb Free Tier Limits

### Hobby Plan (No Credit Card Required)
- ✅ **1 web service**
- ✅ **512MB RAM**
- ✅ **2GB SSD storage**
- ❌ **No database included** (would need external database service)
- ✅ **Automatic HTTPS**
- ✅ **Global edge network**

### Starter Plan (Requires Credit Card)
- ✅ **1 free web service**
- ✅ **1 free database**
- ⚠️ **Payment method required** (charges apply for additional usage)
- ⚠️ **Pay-per-use** model beyond free tier

## 💡 Better Free Alternatives

If you want a **truly free** Django deployment with database (no credit card):

1. **Render** - 750 hours/month, PostgreSQL included, no credit card
2. **Railway** - 500 hours/month, PostgreSQL included, no credit card  
3. **Fly.io** - 3 shared VMs, PostgreSQL available, no credit card

See `ALTERNATIVE_HOSTING.md` for details on these platforms.

---

## 🐛 Troubleshooting

### Build Fails

**Issue:** Build command fails
- **Solution:** Check build logs in Koyeb dashboard
- Ensure `requirements.txt` has all dependencies
- Verify Python version compatibility

**Issue:** Static files not collecting
- **Solution:** Check build command includes `collectstatic`
- Verify `STATIC_ROOT` is set correctly in settings

### Database Connection Issues

**Issue:** Can't connect to database
- **Solution:** 
  - Verify `DATABASE_URL` is set correctly
  - Use the **internal** connection string from Koyeb
  - Ensure database service is running
  - Check `dj-database-url` is in requirements.txt (it is!)

### Application Crashes

**Issue:** App starts then crashes
- **Solution:**
  - Check logs in Koyeb dashboard
  - Verify `SECRET_KEY` is set
  - Ensure `DEBUG=False` in production
  - Check `ALLOWED_HOSTS` includes your Koyeb domain

**Issue:** Port binding errors
- **Solution:** 
  - Ensure run command uses `$PORT` variable
  - Gunicorn should bind to `0.0.0.0:$PORT`
  - Koyeb sets `$PORT` automatically

### Static Files Not Loading

**Issue:** CSS/JS/images not loading
- **Solution:**
  - Verify `whitenoise` is in MIDDLEWARE (it is!)
  - Check `collectstatic` ran during build
  - Ensure `STATIC_ROOT` is set correctly
  - Check `STATIC_URL` is `/static/`

### 500 Errors

**Issue:** Getting 500 Internal Server Error
- **Solution:**
  - Check application logs in Koyeb dashboard
  - Verify all environment variables are set
  - Run migrations: `python manage.py migrate`
  - Check database connection

---

## ✅ Post-Deployment Checklist

After deployment, verify:

- [ ] Site loads at your Koyeb URL
- [ ] Static files (CSS, JS, images) load correctly
- [ ] Admin panel accessible at `/admin/`
- [ ] Database migrations ran successfully
- [ ] Can create superuser and login
- [ ] All pages render correctly
- [ ] Contact form works (if configured)
- [ ] AI services work (if using OpenAI API)

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
3. **Koyeb will automatically redeploy** (if auto-deploy is enabled)
4. Or **manually trigger** redeploy from Koyeb dashboard

---

## 📝 Environment Variables Reference

Here's a complete list of environment variables you should set:

```bash
# Required
SECRET_KEY=t+ee)x8ii9xy2b46rxxr==iji!8s%_y+n#ui+lz9f^y9%h-(y9
DEBUG=False
ALLOWED_HOSTS=your-app-name.koyeb.app,localhost,127.0.0.1
DATABASE_URL=postgresql://user:password@host:port/database
DJANGO_SETTINGS_MODULE=portfolio.settings
PORT=8000

# Optional - AI Features
OPENAI_API_KEY=your-openai-api-key-here

# Optional - Email (for contact form)
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```

---

## 🎉 Success!

Your Django portfolio is now live on Koyeb!

**Next Steps:**
1. Add your content via admin panel
2. Customize your profile
3. Upload projects and blog posts
4. (Optional) Add custom domain

---

## 📞 Need Help?

- **Koyeb Docs:** https://www.koyeb.com/docs
- **Koyeb Discord:** Check Koyeb website for community
- **Koyeb Support:** Available in dashboard

---

## 🚀 Quick Command Reference

**Generate new SECRET_KEY:**
```powershell
python generate_secret_key.py
```

**Test locally before deploying:**
```powershell
cd backend
python manage.py collectstatic
python manage.py migrate
python manage.py runserver
```

**Check deployment logs:**
- Go to Koyeb dashboard → Your service → Logs

---

**Happy deploying! Your portfolio will be live in minutes! 🎉**

