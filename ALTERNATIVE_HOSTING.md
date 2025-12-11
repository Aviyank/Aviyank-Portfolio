# 🚀 Alternative Free Hosting Options for Your Portfolio

Since you want alternatives to Railway, here are the best **FREE** hosting platforms for your Django portfolio:

---

## 🎯 Option 1: Render (Recommended Alternative)

**Why Render?**
- ✅ **750 hours/month** free (more than Railway!)
- ✅ Easy GitHub integration
- ✅ Automatic SSL certificates
- ✅ PostgreSQL database included
- ✅ Custom domains supported

### Quick Deploy Steps:

1. **Sign Up:**
   - Go to [render.com](https://render.com)
   - Sign up with GitHub

2. **Create Web Service:**
   - Click **"New +"** → **"Web Service"**
   - Connect your GitHub repo: `Aviyank/Aviyank-Portfolio`
   - Render will auto-detect settings from `render.yaml`

3. **Configure:**
   - **Build Command:** `chmod +x ./build.sh && ./build.sh`
   - **Start Command:** `cd backend && gunicorn portfolio.wsgi:application`
   - **Environment:** Python 3

4. **Add Environment Variables:**
   ```
   SECRET_KEY=t+ee)x8ii9xy2b46rxxr==iji!8s%_y+n#ui+lz9f^y9%h-(y9
   DEBUG=False
   DJANGO_SETTINGS_MODULE=portfolio.settings
   ```

5. **Add PostgreSQL Database:**
   - Click **"New +"** → **"PostgreSQL"**
   - Render automatically links it via `DATABASE_URL`

6. **Deploy!**
   - Your site: `https://your-app-name.onrender.com`

**Free Tier:** 750 hours/month, 512MB RAM, spins down after 15 min inactivity

---

## 🎯 Option 2: Fly.io

**Why Fly.io?**
- ✅ **3 shared VMs** free forever
- ✅ Global edge network
- ✅ Great for Django apps
- ✅ PostgreSQL included

### Quick Deploy Steps:

1. **Install Fly CLI:**
   ```powershell
   # Windows (PowerShell)
   iwr https://fly.io/install.ps1 -useb | iex
   ```

2. **Sign Up:**
   - Go to [fly.io](https://fly.io)
   - Sign up and install CLI

3. **Create App:**
   ```bash
   fly launch
   # Follow prompts, select your region
   ```

4. **Add PostgreSQL:**
   ```bash
   fly postgres create --name your-app-db
   fly postgres attach your-app-db
   ```

5. **Deploy:**
   ```bash
   fly deploy
   ```

**Free Tier:** 3 shared VMs, 3GB storage, 160GB outbound data transfer

---

## 🎯 Option 3: PythonAnywhere

**Why PythonAnywhere?**
- ✅ **Beginner-friendly** web interface
- ✅ Free tier available
- ✅ Great for learning
- ✅ Built-in Python console

### Quick Deploy Steps:

1. **Sign Up:**
   - Go to [pythonanywhere.com](https://www.pythonanywhere.com)
   - Create free account

2. **Upload Your Code:**
   - Use **Files** tab to upload your project
   - Or clone from GitHub using **Bash Console**

3. **Configure Web App:**
   - Go to **Web** tab
   - Click **"Add a new web app"**
   - Select **Django** and Python version
   - Point to your project directory

4. **Set Environment Variables:**
   - In **Web** tab → **WSGI configuration file**
   - Add your SECRET_KEY and other vars

5. **Reload:**
   - Click **"Reload"** button
   - Your site: `https://yourusername.pythonanywhere.com`

**Free Tier:** 1 web app, 512MB disk space, 1 CPU hour/day

---

## 🎯 Option 4: Vercel (with Serverless)

**Why Vercel?**
- ✅ **Excellent performance**
- ✅ Automatic deployments
- ✅ Great for static + API
- ✅ Edge network

**Note:** Requires some configuration for Django (works best with serverless functions)

### Quick Deploy Steps:

1. **Sign Up:**
   - Go to [vercel.com](https://vercel.com)
   - Sign up with GitHub

2. **Import Project:**
   - Click **"Add New"** → **"Project"**
   - Import `Aviyank/Aviyank-Portfolio`

3. **Configure:**
   - Framework: Django
   - Build Command: `pip install -r requirements.txt && cd backend && python manage.py collectstatic`
   - Output Directory: `backend`

4. **Add Environment Variables:**
   - Add SECRET_KEY, DEBUG, etc.

**Free Tier:** Unlimited deployments, 100GB bandwidth

---

## 🎯 Option 5: Koyeb

**⚠️ Important: Koyeb Pricing**

**Hobby Plan (Free, No Credit Card):**
- ✅ 1 web service, 512MB RAM, 2GB storage
- ❌ **No PostgreSQL database included**

**Starter Plan (Free Services, But Requires Credit Card):**
- ✅ 1 free web service + 1 free database
- ⚠️ **Requires payment method** (pay-per-use model)

**Note:** For truly free hosting with database, use **Render** or **Railway** instead.

### Quick Deploy Steps (If Using Starter Plan):

1. **Sign Up:**
   - Go to [koyeb.com](https://www.koyeb.com)
   - Sign up with GitHub
   - **Note:** Starter plan requires credit card

2. **Create App:**
   - Click **"Create App"**
   - Connect GitHub repo
   - Select **"Docker"** or **"Buildpack"**

3. **Configure:**
   - Build Command: `pip install -r requirements.txt`
   - Run Command: `cd backend && gunicorn portfolio.wsgi:application`

4. **Add Database:**
   - Add PostgreSQL service (free on Starter plan)
   - Link to your app

**Free Tier:** Hobby = 1 service (no DB), Starter = 1 service + 1 DB (requires credit card)

---

## 🎯 Option 6: Cyclic.sh

**Why Cyclic?**
- ✅ **Serverless Django**
- ✅ Auto-scaling
- ✅ GitHub integration
- ✅ Free PostgreSQL

### Quick Deploy Steps:

1. **Sign Up:**
   - Go to [cyclic.sh](https://www.cyclic.sh)
   - Sign up with GitHub

2. **Deploy:**
   - Connect your repo
   - Cyclic auto-detects Django
   - Add environment variables

**Free Tier:** Unlimited apps, 1GB storage, 100GB bandwidth

---

## 📊 Comparison Table

| Platform | Free Hours/Month | RAM | Database | Best For |
|----------|-----------------|-----|----------|----------|
| **Render** | 750 hours | 512MB | ✅ PostgreSQL | Best overall alternative |
| **Fly.io** | Unlimited* | Shared | ✅ PostgreSQL | Global edge network |
| **PythonAnywhere** | 1 CPU hour/day | 512MB | ❌ (use SQLite) | Beginners |
| **Vercel** | Unlimited | Serverless | ❌ (external) | Static + API |
| **Koyeb** | Unlimited* | 256MB | ✅ PostgreSQL | Simple deployment |
| **Cyclic** | Unlimited* | Serverless | ✅ PostgreSQL | Serverless Django |

*With usage limits

---

## 🎯 My Recommendation

**For your Django portfolio, I recommend:**

1. **Render** - Best free tier (750 hours), easy setup, PostgreSQL included, **NO CREDIT CARD**
2. **Railway** - Good alternative (500 hours), 1GB RAM, PostgreSQL included, **NO CREDIT CARD**
3. **Fly.io** - If you want global edge network and more control, **NO CREDIT CARD**

**Avoid Koyeb** if you want truly free hosting - it requires a credit card for database access.

---

## 🚀 Quick Start: Render (Easiest Alternative)

Since you already have `render.yaml` configured, Render is the easiest:

1. Go to [render.com](https://render.com) → Sign up with GitHub
2. Click **"New +"** → **"Web Service"**
3. Select your repo: `Aviyank/Aviyank-Portfolio`
4. Render will auto-detect your `render.yaml` configuration!
5. Add environment variables:
   - `SECRET_KEY=t+ee)x8ii9xy2b46rxxr==iji!8s%_y+n#ui+lz9f^y9%h-(y9`
   - `DEBUG=False`
6. Add PostgreSQL database
7. Deploy!

**That's it!** Your site will be live at `https://your-app-name.onrender.com`

---

## 📝 Need Help?

Each platform has excellent documentation:
- **Render:** https://render.com/docs
- **Fly.io:** https://fly.io/docs
- **PythonAnywhere:** https://help.pythonanywhere.com
- **Vercel:** https://vercel.com/docs
- **Koyeb:** https://www.koyeb.com/docs
- **Cyclic:** https://docs.cyclic.sh

---

**🎉 Choose the platform that works best for you!**

