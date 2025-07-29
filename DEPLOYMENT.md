# 🚀 Portfolio Website Deployment Guide

## Pre-Deployment Checklist

### 1. **Environment Variables** (CRITICAL)
Create a `.env` file in the `backend/` directory:
```env
SECRET_KEY=your-super-secret-key-change-this-immediately
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
OPENAI_API_KEY=your-openai-api-key-here
```

### 2. **Generate a New Secret Key**
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### 3. **Database Setup**
For production, consider switching from SQLite to PostgreSQL:
```bash
# Install PostgreSQL dependencies
pip install psycopg2-binary

# Update settings.py DATABASES configuration
```

### 4. **Static Files**
```bash
cd backend
python manage.py collectstatic --noinput
```

### 5. **Database Migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. **Create Superuser**
```bash
python manage.py createsuperuser
```

## Hosting Options

### Option 1: **Railway** (Recommended for beginners)
1. Push your code to GitHub
2. Connect Railway to your GitHub repo
3. Set environment variables in Railway dashboard
4. Deploy!

### Option 2: **Heroku**
1. Create `Procfile` in backend/:
```
web: gunicorn portfolio.wsgi --log-file -
```
2. Add `runtime.txt`:
```
python-3.11.0
```
3. Deploy using Heroku CLI

### Option 3: **DigitalOcean App Platform**
1. Connect your GitHub repo
2. Set environment variables
3. Deploy

### Option 4: **VPS (DigitalOcean, AWS, etc.)**
1. Set up server with Ubuntu
2. Install Python, Nginx, PostgreSQL
3. Configure Nginx as reverse proxy
4. Use systemd for process management

## Security Checklist

- [ ] Changed default SECRET_KEY
- [ ] Set DEBUG=False
- [ ] Configured ALLOWED_HOSTS
- [ ] Set up HTTPS/SSL
- [ ] Configured proper CORS settings
- [ ] Set up email backend for contact form
- [ ] Regular backups of database
- [ ] Updated dependencies regularly

## Performance Optimization

- [ ] Enable database connection pooling
- [ ] Configure caching (Redis/Memcached)
- [ ] Optimize static files with CDN
- [ ] Enable Gzip compression
- [ ] Set up monitoring and logging

## Post-Deployment

1. Test all functionality
2. Set up domain and SSL
3. Configure email for contact form
4. Set up monitoring
5. Create backup strategy 