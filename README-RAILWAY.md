# Railway Deployment Guide

This guide provides step-by-step instructions for deploying your AI Portfolio to Railway.

## Prerequisites

1. A [Railway](https://railway.app/) account (sign up with GitHub)
2. Your portfolio code pushed to a GitHub repository

## Deployment Steps

### 1. Fork or Clone the Repository

Ensure you have your own copy of the repository on GitHub.

### 2. Connect to Railway

1. Log in to [Railway](https://railway.app/)
2. Click "New Project" → "Deploy from GitHub repo"
3. Select your portfolio repository
4. Railway will automatically detect it's a Django app

### 3. Configure Environment Variables

In the Railway dashboard, go to your project's "Variables" tab and add the following:

```
SECRET_KEY=your-super-secret-key-here
DEBUG=False
```

Optionally, add:
```
OPENAI_API_KEY=your-openai-api-key
```

### 4. Add PostgreSQL Database

1. In Railway dashboard, click "New" → "Database" → "PostgreSQL"
2. Railway will automatically set `DATABASE_URL` in your environment

### 5. Deploy

Railway will automatically build and deploy your app. The deployment process uses:

- `railway.json` - Configuration for build and deploy commands
- `backend/build.sh` - Script that installs dependencies and runs migrations
- `backend/Procfile` - Defines how to run the web server

### 6. Access Your Site

Once deployed, you can access your site at the URL provided by Railway, typically:
```
https://your-app-name.up.railway.app
```

## Troubleshooting

### Deployment Fails

1. Check the build logs in Railway dashboard
2. Ensure all required environment variables are set
3. Verify your `railway.json` file is correctly configured

### Database Connection Issues

1. Verify the `DATABASE_URL` is set in your environment variables
2. Check that `dj-database-url` is in your requirements.txt

### Static Files Not Loading

1. Ensure `whitenoise` is installed and configured
2. Verify `STATIC_ROOT` is set correctly in `production.py`

## Customizing Your Deployment

### Custom Domain

1. Purchase a domain from a provider
2. In Railway dashboard, go to your project settings
3. Add your custom domain
4. Update DNS records as instructed by Railway

### Scaling

Railway's free tier includes:
- 500 hours of runtime per month
- 1GB of RAM
- 1GB of storage

For production use, consider upgrading to a paid plan.