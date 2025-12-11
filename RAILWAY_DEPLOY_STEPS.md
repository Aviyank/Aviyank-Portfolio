# 🚀 Railway Deployment Steps for Your Portfolio

Your code is now on GitHub: **https://github.com/Aviyank/Aviyank-Portfolio.git**

Follow these steps to deploy your portfolio for FREE on Railway:

## Step-by-Step Deployment

### 1. Sign Up for Railway
1. Go to **[railway.app](https://railway.app)**
2. Click **"Start a New Project"** or **"Login"**
3. Sign up with **GitHub** (recommended - it's free!)

### 2. Create New Project
1. Once logged in, click **"New Project"**
2. Select **"Deploy from GitHub repo"**
3. Authorize Railway to access your GitHub if prompted
4. Find and select **"Aviyank-Portfolio"** repository
5. Click **"Deploy Now"**

### 3. Add PostgreSQL Database
1. In your Railway project dashboard, click **"+ New"**
2. Select **"Database"** → **"Add PostgreSQL"**
3. Railway will automatically create the database and set `DATABASE_URL` environment variable

### 4. Configure Environment Variables
1. Click on your **web service** (not the database)
2. Go to the **"Variables"** tab
3. Click **"+ New Variable"** and add these:

   **Required Variables:**
   ```
   SECRET_KEY=t+ee)x8ii9xy2b46rxxr==iji!8s%_y+n#ui+lz9f^y9%h-(y9
   DEBUG=False
   ```

   **Optional (if using AI features):**
   ```
   OPENAI_API_KEY=your-openai-api-key-here
   ```

### 5. Wait for Deployment
- Railway will automatically:
  - Install dependencies from `requirements.txt`
  - Run `collectstatic` to gather static files
  - Run database migrations
  - Start your Django app with Gunicorn

- Watch the **"Deployments"** tab for build progress
- Build typically takes 2-5 minutes

### 6. Access Your Live Site
Once deployment completes:
- Your site will be live at: `https://your-app-name.up.railway.app`
- Railway provides a random subdomain (you can customize it later)

### 7. Create Admin User (After First Deploy)
1. In Railway dashboard, go to your **web service**
2. Click **"Deployments"** → Find the latest deployment
3. Click **"..."** → **"View Logs"** or use **"Shell"**
4. Run these commands:
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```
   (Follow prompts to create admin username/password)

### 8. Access Admin Panel
- Go to: `https://your-app-name.up.railway.app/admin/`
- Login with your superuser credentials
- Start adding your portfolio content!

---

## 🎯 Quick Reference

**Your Repository:** https://github.com/Aviyank/Aviyank-Portfolio.git

**Your SECRET_KEY:** `t+ee)x8ii9xy2b46rxxr==iji!8s%_y+n#ui+lz9f^y9%h-(y9`

**Railway Dashboard:** https://railway.app/dashboard

---

## ✅ What Happens Automatically

Railway uses your `railway.json` file which:
- ✅ Installs all Python dependencies
- ✅ Collects static files
- ✅ Runs database migrations
- ✅ Starts the server with Gunicorn

---

## 🆓 Free Tier Limits

- **500 hours/month** free runtime
- **1GB RAM**
- **PostgreSQL database** included
- **Custom domains** supported
- **Automatic HTTPS** (SSL certificates)

---

## 🔧 Troubleshooting

### Build Fails
- Check the build logs in Railway dashboard
- Ensure `requirements.txt` has all dependencies
- Verify Python version in `runtime.txt` is supported (3.11.7)

### Database Connection Issues
- Verify PostgreSQL database is added
- Check `DATABASE_URL` is automatically set by Railway
- Ensure `dj-database-url` is in requirements.txt (it is!)

### Static Files Not Loading
- Static files are collected during build automatically
- Check `whitenoise` is in MIDDLEWARE (it is!)
- Verify `STATIC_ROOT` is set correctly

### 500 Errors
- Check logs in Railway dashboard → Deployments → View Logs
- Ensure `SECRET_KEY` is set correctly
- Verify `DEBUG=False` in production

---

## 🎉 Next Steps After Deployment

1. **Add Your Content:**
   - Login to admin panel
   - Add your profile information
   - Upload projects, skills, experience
   - Write blog posts

2. **Customize Domain (Optional):**
   - Buy a domain (Namecheap, GoDaddy, etc.)
   - In Railway: Settings → Domains → Add Custom Domain
   - Update DNS records as instructed

3. **Monitor Usage:**
   - Check Railway dashboard for usage stats
   - Monitor logs for any errors
   - Set up email notifications if needed

---

## 📞 Need Help?

- **Railway Docs:** https://docs.railway.app
- **Railway Discord:** https://discord.gg/railway
- **Your Deployment Guide:** See `DEPLOY_NOW.md` for more details

---

**🚀 Your portfolio will be live in minutes!**

