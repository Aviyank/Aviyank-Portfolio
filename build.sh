#!/usr/bin/env bash
# Build script for Render deployment

# Exit on error
set -o errexit

# Install Python dependencies
pip install -r requirements.txt

# Change to backend directory
cd backend

# Collect static files
python manage.py collectstatic --no-input

# Run migrations
python manage.py migrate

echo "Build completed successfully!"