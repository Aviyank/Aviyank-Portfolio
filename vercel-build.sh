#!/bin/bash
set -e

echo "🚀 Starting Vercel build..."

# Install dependencies
echo "📦 Installing dependencies..."
pip install -r requirements.txt

# Set Django settings module for collectstatic
export DJANGO_SETTINGS_MODULE=portfolio.settings

# Change to backend directory and collect static files
echo "📁 Collecting static files..."
cd backend && python manage.py collectstatic --noinput || echo "⚠️  Static collection failed, continuing..."

echo "✅ Build completed!"
