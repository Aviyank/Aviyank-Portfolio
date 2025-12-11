# ⚡ Koyeb Quick Start - 5 Minutes to Deploy

## 🎯 Super Quick Steps

### 1. Sign Up
- Go to [koyeb.com](https://www.koyeb.com)
- Sign up with **GitHub**

### 2. Create Database
- Click **"Create"** → **"Database"** → **"PostgreSQL"**
- Name: `portfolio-db`
- Plan: **Starter** (Free)
- **Copy the Connection String!**

### 3. Create Web Service
- Click **"Create"** → **"Web Service"**
- Connect GitHub repo: **Aviyank/Aviyank-Portfolio**

### 4. Configure Build & Run

**Build Command:**
```bash
pip install -r requirements.txt && cd backend && python manage.py collectstatic --noinput
```

**Run Command:**
```bash
cd backend && gunicorn portfolio.wsgi:application --bind 0.0.0.0:$PORT
```

### 5. Add Environment Variables

Click **"Environment Variables"** and add:

```
SECRET_KEY=t+ee)x8ii9xy2b46rxxr==iji!8s%_y+n#ui+lz9f^y9%h-(y9
DEBUG=False
ALLOWED_HOSTS=*.koyeb.app,localhost,127.0.0.1
DATABASE_URL=<paste connection string from step 2>
PORT=8000
```

### 6. Deploy!
- Click **"Deploy"**
- Wait 2-5 minutes
- Your site: `https://your-app-name.koyeb.app`

### 7. Run Migrations & Create Admin

After deployment, use Koyeb Shell:
```bash
cd backend
python manage.py migrate
python manage.py createsuperuser
```

---

## ✅ That's It!

Your portfolio is live! 🎉

See `KOYEB_DEPLOY.md` for detailed troubleshooting and advanced options.

