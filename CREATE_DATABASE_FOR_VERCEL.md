# 🗄️ Create Database for Vercel - Step by Step

I'll guide you through creating a **FREE PostgreSQL database** on Render (easiest option).

---

## 🚀 Quick Setup (5 Minutes)

### Step 1: Sign Up for Render

1. Go to **[render.com](https://render.com)**
2. Click **"Get Started for Free"**
3. Sign up with **GitHub** (easiest way)
4. Authorize Render to access your GitHub

### Step 2: Create PostgreSQL Database

1. In Render dashboard, click **"New +"** (top right)
2. Select **"PostgreSQL"**
3. Fill in the form:
   - **Name:** `portfolio-db` (or any name you like)
   - **Database:** `portfolio_db` (or any name)
   - **User:** `portfolio_user` (or any name)
   - **Region:** Choose closest to you (e.g., `Oregon (US West)`)
   - **PostgreSQL Version:** Leave as default (latest)
   - **Plan:** Select **"Free"**
4. Click **"Create Database"**

### Step 3: Wait for Database to Start

- Render will create your database (takes 1-2 minutes)
- You'll see a status like "Available" when ready

### Step 4: Get Your Database URL

1. Click on your database name (`portfolio-db`)
2. You'll see database information
3. Look for **"External Database URL"** section
4. Click **"Show"** to reveal the password
5. **Copy the entire External Database URL**
   - It looks like: `postgresql://portfolio_user:abc123xyz@dpg-xxxxx-a.oregon-postgres.render.com/portfolio_db`

**⚠️ Important:** Copy the **External** URL, NOT the Internal URL!

### Step 5: Add to Vercel

1. Go to **Vercel Dashboard** → Your Project
2. Click **Settings** → **Environment Variables**
3. Click **"Add New"**
4. Add:
   - **Name:** `DATABASE_URL`
   - **Value:** `postgresql://portfolio_user:abc123xyz@dpg-xxxxx-a.oregon-postgres.render.com/portfolio_db`
     (Paste your actual URL from Step 4)
   - **Environment:** Select all three (Production, Preview, Development)
5. Click **"Save"**

### Step 6: Redeploy Vercel

1. Go to **Deployments** tab
2. Click **"..."** on latest deployment
3. Click **"Redeploy"**
4. Or push a new commit to trigger auto-redeploy

---

## ✅ That's It!

Your database is now connected to Vercel!

---

## 🔍 What Your DATABASE_URL Looks Like

```
postgresql://username:password@host:port/database
```

**Example:**
```
postgresql://portfolio_user:abc123xyz@dpg-abc123-a.oregon-postgres.render.com/portfolio_db
```

**Parts:**
- `postgresql://` - Protocol
- `portfolio_user` - Username
- `abc123xyz` - Password
- `dpg-abc123-a.oregon-postgres.render.com` - Host
- `portfolio_db` - Database name

---

## 🆘 Troubleshooting

### Can't Find External Database URL?

1. Make sure database status is "Available"
2. Scroll down in the database dashboard
3. Look for "Connections" or "Database URL" section
4. Make sure you're looking at **External** (not Internal)

### Database Not Starting?

- Wait a few more minutes
- Check Render status page
- Try creating a new database

### Connection Issues?

- Make sure you copied the **External** URL (not Internal)
- Verify the URL format is correct
- Check that database is "Available" status

---

## 📝 Alternative: Railway Database

If Render doesn't work, try Railway:

1. Go to [railway.app](https://railway.app)
2. Sign up with GitHub
3. Click **"New Project"**
4. Click **"New"** → **"Database"** → **"PostgreSQL"**
5. Railway automatically creates and sets `DATABASE_URL`
6. Go to database → **"Variables"** tab
7. Copy the `DATABASE_URL` value
8. Add to Vercel environment variables

---

## 🎯 Next Steps

After you have your DATABASE_URL:

1. ✅ Add to Vercel environment variables
2. ✅ Redeploy your Vercel project
3. ✅ Run migrations (see below)

### Run Migrations

After deployment, run migrations locally pointing to your production database:

```powershell
# Set your production DATABASE_URL
$env:DATABASE_URL="postgresql://portfolio_user:password@host:port/database"
cd backend
python manage.py migrate
python manage.py createsuperuser
```

---

**Follow these steps and you'll have your database URL in 5 minutes! 🚀**

