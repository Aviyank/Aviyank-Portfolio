# ⚡ Vercel Quick Start - 5 Minutes to Deploy

## 🎯 Super Quick Steps

### Step 1: Set Up Free Database (Required)

**Option A: Render PostgreSQL (Recommended)**
1. Go to [render.com](https://render.com) → Sign up with GitHub
2. Click **"New +"** → **"PostgreSQL"**
3. Name: `portfolio-db`, Plan: **Free**
4. **Copy the External Database URL** (you'll need it!)

**Option B: Railway PostgreSQL**
1. Go to [railway.app](https://railway.app) → Sign up
2. Click **"New Project"** → **"Database"** → **"PostgreSQL"**
3. Copy the `DATABASE_URL` from dashboard

### Step 2: Sign Up for Vercel
1. Go to [vercel.com](https://vercel.com)
2. Sign up with **GitHub**

### Step 3: Deploy Your Project
1. In Vercel dashboard, click **"Add New..."** → **"Project"**
2. Select your repo: **Aviyank/Aviyank-Portfolio**
3. Click **"Import"**

### Step 4: Configure Settings

**Framework Preset:** Leave as auto-detected or select "Other"

**Root Directory:** `.` (root)

**Build Settings:**
- **Build Command:** 
  ```bash
  pip install -r requirements.txt && cd backend && python manage.py collectstatic --noinput
  ```
- **Output Directory:** `backend`
- **Install Command:** `pip install -r requirements.txt`

### Step 5: Add Environment Variables

Click **"Environment Variables"** and add:

```
SECRET_KEY=t+ee)x8ii9xy2b46rxxr==iji!8s%_y+n#ui+lz9f^y9%h-(y9
DEBUG=False
ALLOWED_HOSTS=*.vercel.app,localhost,127.0.0.1
DATABASE_URL=<paste database URL from Step 1>
DJANGO_SETTINGS_MODULE=portfolio.settings
PYTHON_VERSION=3.11
```

**Important:** Replace `<paste database URL>` with your actual database connection string!

### Step 6: Deploy!
- Click **"Deploy"**
- Wait 2-5 minutes
- Your site: `https://your-app-name.vercel.app`

### Step 7: Run Migrations

After deployment, run migrations locally pointing to your production database:

```powershell
# Set your production DATABASE_URL
$env:DATABASE_URL="your-production-database-url-from-step-1"
cd backend
python manage.py migrate
python manage.py createsuperuser
```

### Step 8: Access Your Site!

- Portfolio: `https://your-app-name.vercel.app`
- Admin: `https://your-app-name.vercel.app/admin/`

---

## ✅ That's It!

Your portfolio is live on Vercel! 🎉

See `VERCEL_DEPLOY.md` for detailed troubleshooting and advanced options.

---

## 📝 Important Notes

- ✅ Vercel is **100% FREE** - no credit card required
- ⚠️ You need an **external database** (Render or Railway PostgreSQL)
- ⚠️ Vercel is **serverless** - some Django features may need adjustment
- ⚠️ Free tier has **10-second function timeout**

---

## 🆘 Quick Troubleshooting

**Build fails?** Check build logs in Vercel dashboard

**Database errors?** Verify `DATABASE_URL` is correct and database is accessible

**Static files not loading?** Ensure `collectstatic` ran during build

**500 errors?** Check function logs and verify all environment variables are set

