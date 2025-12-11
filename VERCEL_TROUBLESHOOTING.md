# 🔧 Vercel Troubleshooting Guide

## Common Issues and Solutions

### Issue 1: Build Fails

**Symptoms:**
- Build fails in Vercel dashboard
- Error messages in build logs

**Solutions:**

1. **Check Build Logs:**
   - Go to Vercel dashboard → Your project → Deployments
   - Click on the failed deployment
   - Check the build logs for specific errors

2. **Common Build Errors:**

   **Error: "Module not found"**
   - Ensure all dependencies are in `requirements.txt`
   - Check if `gunicorn`, `whitenoise`, `dj-database-url` are included (they are!)

   **Error: "Python version mismatch"**
   - Set `PYTHON_VERSION=3.11` in environment variables
   - Or update `runtime.txt` to `3.11.7`

   **Error: "collectstatic failed"**
   - This is okay - static files can be handled by Vercel
   - Try removing `collectstatic` from build command temporarily

---

### Issue 2: 500 Internal Server Error

**Symptoms:**
- Site loads but shows 500 error
- Blank page or error message

**Solutions:**

1. **Check Function Logs:**
   - Vercel dashboard → Your project → Functions tab
   - Or Deployments → Click deployment → Functions → View logs

2. **Common Causes:**

   **Missing Environment Variables:**
   - Verify `SECRET_KEY` is set
   - Verify `DATABASE_URL` is set
   - Verify `ALLOWED_HOSTS` includes your Vercel domain

   **Database Connection Error:**
   - Check `DATABASE_URL` is correct
   - Ensure database is accessible from internet (not internal URL)
   - Verify `dj-database-url` is in requirements.txt

   **Django Settings Error:**
   - Vercel might not be using production settings
   - Check if `DJANGO_SETTINGS_MODULE` is set to `portfolio.settings`
   - Or update wsgi.py to use production settings

---

### Issue 3: Static Files Not Loading (404)

**Symptoms:**
- CSS/JS/images return 404
- Site loads but no styling

**Solutions:**

1. **Check vercel.json Routes:**
   ```json
   {
     "src": "/static/(.*)",
     "dest": "/backend/staticfiles/$1"
   }
   ```

2. **Verify Static Files Collected:**
   - Build command should include `collectstatic`
   - Check if `backend/staticfiles/` directory exists after build

3. **Alternative: Use WhiteNoise:**
   - WhiteNoise is already in your MIDDLEWARE
   - Should serve static files automatically
   - But Vercel routing might interfere

---

### Issue 4: Database Errors

**Symptoms:**
- "OperationalError: no such table"
- "Connection refused"
- Database-related errors

**Solutions:**

1. **Verify DATABASE_URL:**
   - Check environment variable is set correctly
   - Use **external** database URL (not internal)
   - Format: `postgresql://user:password@host:port/database`

2. **Run Migrations:**
   ```powershell
   $env:DATABASE_URL="your-production-database-url"
   cd backend
   python manage.py migrate
   ```

3. **Check Database Access:**
   - Ensure database allows external connections
   - Check firewall/security settings
   - Verify credentials are correct

---

### Issue 5: Function Timeout

**Symptoms:**
- Request takes too long
- "Function execution exceeded timeout"

**Solutions:**

1. **Vercel Free Tier Limit:**
   - Free tier has 10-second timeout
   - Optimize your views to respond quickly
   - Consider upgrading to Vercel Pro

2. **Optimize Database Queries:**
   - Use `select_related()` and `prefetch_related()`
   - Add database indexes
   - Cache frequently accessed data

---

### Issue 6: "Application Error" or Blank Page

**Symptoms:**
- Page shows "Application Error"
- Completely blank page
- No error details

**Solutions:**

1. **Check Function Logs:**
   - Vercel dashboard → Functions → View logs
   - Look for Python tracebacks

2. **Enable Debug Temporarily:**
   - Set `DEBUG=True` in environment variables
   - This will show error details (remove after fixing!)

3. **Check ALLOWED_HOSTS:**
   - Add your Vercel domain: `*.vercel.app`
   - Or specific domain: `your-app-name.vercel.app`

---

## 🔍 Step-by-Step Debugging

### Step 1: Check Build Logs

1. Go to Vercel dashboard
2. Click your project
3. Click "Deployments"
4. Click on the latest deployment
5. Check "Build Logs" tab

**Look for:**
- ✅ "Build successful"
- ❌ Any error messages
- ❌ Missing dependencies
- ❌ Python version issues

### Step 2: Check Function Logs

1. In same deployment page
2. Click "Functions" tab
3. Click on the function
4. Check "Logs" tab

**Look for:**
- ✅ Django startup messages
- ❌ Import errors
- ❌ Database connection errors
- ❌ Settings errors

### Step 3: Verify Environment Variables

1. Vercel dashboard → Your project
2. Click "Settings" → "Environment Variables"
3. Verify all required variables are set:

**Required:**
- `SECRET_KEY` ✅
- `DEBUG` (set to `False`) ✅
- `ALLOWED_HOSTS` (include `*.vercel.app`) ✅
- `DATABASE_URL` ✅
- `DJANGO_SETTINGS_MODULE` (set to `portfolio.settings`) ✅

### Step 4: Test Database Connection

Run locally with production database:

```powershell
$env:DATABASE_URL="your-production-database-url"
$env:SECRET_KEY="your-secret-key"
$env:DEBUG="False"
cd backend
python manage.py check --database default
python manage.py migrate
```

### Step 5: Check Vercel Configuration

Verify `vercel.json` is correct:

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
      "dest": "/backend/staticfiles/$1"
    },
    {
      "src": "/(.*)",
      "dest": "backend/wsgi.py"
    }
  ]
}
```

---

## 🚨 Quick Fixes

### Fix 1: Update wsgi.py for Production

If Vercel isn't using production settings, update `backend/wsgi.py`:

```python
import os
from django.core.wsgi import get_wsgi_application

# Use production settings on Vercel
if os.environ.get('VERCEL'):
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.production')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')

application = get_wsgi_application()
```

### Fix 2: Simplify Build Command

Try this simpler build command:

```bash
pip install -r requirements.txt
```

Remove `collectstatic` temporarily to see if that's causing issues.

### Fix 3: Add Vercel Detection

Add to your settings to detect Vercel:

```python
# In settings.py or production.py
import os

# Detect if running on Vercel
ON_VERCEL = os.environ.get('VERCEL') == '1'

if ON_VERCEL:
    # Vercel-specific settings
    DEBUG = False
    # Add other Vercel-specific configs
```

---

## 📞 Getting More Help

1. **Check Vercel Logs:**
   - Dashboard → Project → Deployments → Logs

2. **Check Django Logs:**
   - Temporarily set `DEBUG=True` to see errors

3. **Test Locally:**
   - Run with production settings locally
   - Point to production database

4. **Vercel Support:**
   - Vercel Discord: https://vercel.com/discord
   - Vercel Docs: https://vercel.com/docs

---

## ✅ Checklist

Before asking for help, verify:

- [ ] Build succeeds in Vercel dashboard
- [ ] All environment variables are set
- [ ] Database is accessible
- [ ] Migrations have been run
- [ ] `ALLOWED_HOSTS` includes Vercel domain
- [ ] `vercel.json` is correct
- [ ] Function logs show no errors
- [ ] Static files are collected (or using WhiteNoise)

---

**Share the specific error message you're seeing, and I can help you fix it!**

