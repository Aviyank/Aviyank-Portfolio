# 🔑 Vercel Environment Variables - How to Get Values

## 1. DATABASE_URL (Required)

### Option A: Render PostgreSQL (Recommended - Free, No Credit Card)

1. **Sign up:** Go to [render.com](https://render.com) → Sign up with GitHub
2. **Create Database:**
   - Click **"New +"** → **"PostgreSQL"**
   - Name: `portfolio-db`
   - Database: `portfolio_db`
   - User: `portfolio_user`
   - Region: Choose closest (e.g., `Oregon (US West)`)
   - Plan: **Free**
   - Click **"Create Database"**
3. **Get Connection String:**
   - Wait for database to be created
   - Go to your database dashboard
   - Find **"External Database URL"** (NOT Internal)
   - Copy the URL
   - Format: `postgresql://portfolio_user:password@dpg-xxxxx-a.oregon-postgres.render.com/portfolio_db`
4. **Use in Vercel:**
   - Name: `DATABASE_URL`
   - Value: `postgresql://portfolio_user:password@dpg-xxxxx-a.oregon-postgres.render.com/portfolio_db`
   - Environment: Production, Preview, Development

### Option B: Railway PostgreSQL

1. **Sign up:** Go to [railway.app](https://railway.app) → Sign up with GitHub
2. **Create Database:**
   - Click **"New Project"** → **"Database"** → **"PostgreSQL"**
   - Railway automatically creates it
3. **Get Connection String:**
   - Click on your database
   - Go to **"Variables"** tab
   - Find `DATABASE_URL`
   - Copy the value
   - Format: `postgresql://postgres:password@containers-us-west-xxx.railway.app:5432/railway`
4. **Use in Vercel:**
   - Name: `DATABASE_URL`
   - Value: `postgresql://postgres:password@containers-us-west-xxx.railway.app:5432/railway`
   - Environment: Production, Preview, Development

### Option C: Supabase (Free PostgreSQL)

1. **Sign up:** Go to [supabase.com](https://supabase.com) → Sign up
2. **Create Project:**
   - Click **"New Project"**
   - Name: `portfolio-db`
   - Database Password: (choose a strong password)
   - Region: Choose closest
   - Click **"Create new project"**
3. **Get Connection String:**
   - Wait for project to be ready
   - Go to **Settings** → **Database**
   - Find **"Connection string"** section
   - Click **"URI"** tab
   - Copy the connection string
   - Format: `postgresql://postgres.xxxxx:password@aws-0-us-west-1.pooler.supabase.com:6543/postgres`
4. **Use in Vercel:**
   - Name: `DATABASE_URL`
   - Value: `postgresql://postgres.xxxxx:password@aws-0-us-west-1.pooler.supabase.com:6543/postgres`
   - Environment: Production, Preview, Development

---

## 2. OPENAI_API_KEY (Optional - Only if Using AI Features)

### If You Want AI Features:

1. **Sign up:** Go to [platform.openai.com](https://platform.openai.com)
2. **Create Account:**
   - Sign up or log in
   - Add payment method (OpenAI requires this for API access)
3. **Get API Key:**
   - Go to [API Keys page](https://platform.openai.com/api-keys)
   - Click **"Create new secret key"**
   - Name it: `Portfolio App`
   - Click **"Create secret key"**
   - **Copy the key immediately** (you won't see it again!)
   - Format: `sk-proj-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`
4. **Use in Vercel:**
   - Name: `OPENAI_API_KEY`
   - Value: `sk-proj-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`
   - Environment: Production, Preview, Development

### If You DON'T Need AI Features:

- **Skip this variable entirely**
- Your portfolio will work fine without it
- You just won't be able to use AI services (text generation, etc.)
- This is **completely optional**

---

## 📝 Quick Setup Checklist

### Required Variables:

- [ ] **SECRET_KEY** = `t+ee)x8ii9xy2b46rxxr==iji!8s%_y+n#ui+lz9f^y9%h-(y9`
- [ ] **DEBUG** = `False`
- [ ] **ALLOWED_HOSTS** = `*.vercel.app,localhost,127.0.0.1`
- [ ] **DATABASE_URL** = `postgresql://...` (from Render/Railway/Supabase)
- [ ] **DJANGO_SETTINGS_MODULE** = `portfolio.settings`

### Optional Variables:

- [ ] **OPENAI_API_KEY** = `sk-...` (only if using AI features)

---

## 🎯 Recommended Setup

**For easiest setup, use:**

1. **Render PostgreSQL** for database (free, no credit card, easy setup)
2. **Skip OPENAI_API_KEY** if you don't need AI features

**Steps:**
1. Create Render PostgreSQL database (5 minutes)
2. Copy External Database URL
3. Add to Vercel environment variables
4. Redeploy
5. Done! ✅

---

## ⚠️ Important Notes

- **DATABASE_URL** must be the **External** URL (not Internal)
- **DATABASE_URL** format: `postgresql://user:password@host:port/database`
- **OPENAI_API_KEY** is optional - only add if you need AI features
- All variables should be set for **Production, Preview, and Development**
- After adding variables, **redeploy** your project

---

## 🆘 Need Help?

If you're having trouble:
1. Check the database provider's documentation
2. Make sure you're copying the **External** database URL (not Internal)
3. Verify the connection string format is correct
4. Test the connection string locally if possible

---

**Once you have these values, add them to Vercel and redeploy!**

