# Deploying Your AI Portfolio to Render

This guide provides step-by-step instructions for deploying your Django portfolio application to Render, a cloud platform that offers free hosting for web applications.

## Prerequisites

1. A GitHub account with your portfolio code pushed to a repository
2. A Render account (sign up at [render.com](https://render.com) - free tier available)

## Deployment Options

### Option 1: Deploy using render.yaml (Recommended)

This project includes a `render.yaml` file that allows for automatic configuration of your Render services.

1. **Sign in to Render** and go to your dashboard
2. Click **New** and select **Blueprint**
3. Connect your GitHub repository
4. Render will automatically detect the `render.yaml` file and configure:
   - A web service for your Django application
   - A PostgreSQL database
   - All necessary environment variables
5. Click **Apply** to start the deployment

### Option 2: Manual Deployment

If you prefer to set up your services manually:

1. **Create a PostgreSQL Database**
   - In your Render dashboard, click **New** → **PostgreSQL**
   - Name: `django-portfolio-db`
   - Database: `django_portfolio`
   - User: `django_portfolio_user`
   - Select the **Free** plan
   - Click **Create Database**
   - Note the **Internal Database URL** for the next step

2. **Create a Web Service**
   - Click **New** → **Web Service**
   - Connect your GitHub repository
   - Name: `django-portfolio`
   - Build Command: `chmod +x ./build.sh && ./build.sh`
   - Start Command: `cd backend && gunicorn portfolio.wsgi`
   - Select the **Free** plan

3. **Configure Environment Variables**
   - In your web service settings, add the following environment variables:
     - `SECRET_KEY`: Generate a secure random key
     - `DEBUG`: `False`
     - `ALLOWED_HOSTS`: `.onrender.com,localhost,127.0.0.1`
     - `DATABASE_URL`: Paste the Internal Database URL from step 1
     - `PYTHON_VERSION`: `3.11.7`

4. **Deploy**
   - Click **Create Web Service**
   - Render will build and deploy your application

## Accessing Your Deployed Site

Once deployment is complete, your portfolio will be available at:
`https://django-portfolio.onrender.com`

## Troubleshooting

### Common Issues

1. **Build Failures**
   - Check the build logs in your Render dashboard
   - Ensure all dependencies are in `requirements.txt`
   - Verify Python version compatibility

2. **Database Connection Issues**
   - Confirm `DATABASE_URL` is set correctly
   - Check that the database service is running

3. **Static Files Not Loading**
   - Verify `STATIC_ROOT` is set correctly in your settings
   - Ensure `whitenoise` is properly configured

4. **Application Errors**
   - Set `DEBUG=True` temporarily to see detailed error messages
   - Check application logs in the Render dashboard

## Free Tier Limitations

Render's free tier includes:
- 750 hours/month of service runtime
- 512MB RAM
- Shared CPU
- Free PostgreSQL database (1GB storage)
- Services spin down after 15 minutes of inactivity
- Services automatically spin up when receiving traffic

## Updating Your Deployed Site

When you push changes to your GitHub repository:
1. Go to your web service in the Render dashboard
2. Click **Manual Deploy** → **Deploy latest commit**

Or set up automatic deployments in your service settings.

## Custom Domain (Optional)

1. Purchase a domain from a domain registrar
2. In your Render dashboard, go to your web service
3. Navigate to **Settings** → **Custom Domain**
4. Add your domain and follow the DNS configuration instructions

## Additional Resources

- [Render Documentation](https://render.com/docs)
- [Django Deployment Checklist](https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/)
- [Render PostgreSQL Documentation](https://render.com/docs/databases)