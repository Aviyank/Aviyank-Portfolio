# 🔧 Vercel Environment Variables Setup

## ❌ Error: SECRET_KEY not found

You're seeing this error because `SECRET_KEY` environment variable is not set in Vercel.

## ✅ Quick Fix

### Step 1: Add Environment Variables in Vercel

1. Go to **Vercel Dashboard** → Your Project
2. Click **Settings** → **Environment Variables**
3. Click **"Add New"** and add these variables:

**Required Variables:**

```
SECRET_KEY
Value: t+ee)x8ii9xy2b46rxxr==iji!8s%_y+n#ui+lz9f^y9%h-(y9
Environment: Production, Preview, Development (select all)
```

```
DEBUG
Value: False
Environment: Production, Preview, Development (select all)
```

```
ALLOWED_HOSTS
Value: *.vercel.app,localhost,127.0.0.1
Environment: Production, Preview, Development (select all)
```

```
DATABASE_URL
Value: <your-postgresql-connection-string>
Environment: Production, Preview, Development (select all)
```

```
DJANGO_SETTINGS_MODULE
Value: portfolio.settings
Environment: Production, Preview, Development (select all)
```

**Optional (if using AI features):**

```
OPENAI_API_KEY
Value: <your-openai-api-key>
Environment: Production, Preview, Development (select all)
```

### Step 2: Redeploy

After adding environment variables:

1. Go to **Deployments** tab
2. Click **"..."** on latest deployment
3. Click **"Redeploy"**
4. Or push a new commit to trigger auto-deploy

---

## 📝 Complete Environment Variables List

Copy and paste these into Vercel:

| Variable | Value | Required |
|----------|-------|----------|
| `SECRET_KEY` | `t+ee)x8ii9xy2b46rxxr==iji!8s%_y+n#ui+lz9f^y9%h-(y9` | ✅ Yes |
| `DEBUG` | `False` | ✅ Yes |
| `ALLOWED_HOSTS` | `*.vercel.app,localhost,127.0.0.1` | ✅ Yes |
| `DATABASE_URL` | `postgresql://user:pass@host:port/db` | ✅ Yes |
| `DJANGO_SETTINGS_MODULE` | `portfolio.settings` | ✅ Yes |
| `OPENAI_API_KEY` | `your-key-here` | ❌ Optional |

---

## 🔍 How to Check if Variables are Set

1. Vercel Dashboard → Your Project → Settings → Environment Variables
2. You should see all the variables listed above
3. Make sure they're enabled for **Production**, **Preview**, and **Development**

---

## ⚠️ Important Notes

- **SECRET_KEY** must be set - this is critical for Django security
- **DATABASE_URL** must be your external PostgreSQL connection string
- All variables should be set for all environments (Production, Preview, Development)
- After adding variables, **redeploy** for changes to take effect

---

## 🚀 After Setting Variables

1. Variables are set ✅
2. Redeploy your project
3. Check function logs - error should be gone
4. Your site should work!

---

**The error will be fixed once you add the SECRET_KEY environment variable!**

