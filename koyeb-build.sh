#!/bin/bash
# Build script specifically for Koyeb deployment

set -e  # Exit on error

echo "🚀 Starting Koyeb build process..."

# Install Python dependencies
echo "📦 Installing dependencies..."
pip install -r requirements.txt

# Change to backend directory
cd backend

# Collect static files
echo "📁 Collecting static files..."
python manage.py collectstatic --noinput

# Run migrations (optional - can be done after deployment)
# Uncomment if you want migrations to run during build
# echo "🗄️ Running migrations..."
# python manage.py migrate --noinput

echo "✅ Build completed successfully!"

