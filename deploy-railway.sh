#!/bin/bash

echo "🚂 Railway Deployment Script"
echo "================================"

# Check if we're in the right directory
if [ ! -f "backend/manage.py" ]; then
    echo "❌ Error: Please run this script from the project root directory"
    exit 1
fi

echo "📋 Pre-deployment checklist:"
echo ""

# Check if railway CLI is installed
if ! command -v railway &> /dev/null; then
    echo "❌ Railway CLI not found"
    echo "Please install Railway CLI with: npm i -g @railway/cli"
    echo "Then login with: railway login"
    exit 1
fi

echo "✅ Railway CLI found: $(railway version)"

# Check if user is logged in to Railway
if railway status | grep -q "Not logged in"; then
    echo "❌ Not logged in to Railway"
    echo "Please login with: railway login"
    exit 1
fi

echo "✅ Logged in to Railway"

# Check if .env file exists
if [ ! -f "backend/.env" ]; then
    echo "⚠️  Warning: No .env file found in backend/"
    echo "   Environment variables should be configured in Railway dashboard"
    echo "   See backend/env.example for reference"
    echo ""
fi

# Check if railway.json exists
if [ ! -f "railway.json" ]; then
    echo "❌ Error: railway.json not found"
    echo "This file is required for Railway deployment"
    exit 1
fi

echo "✅ railway.json found"

# Deployment options
echo ""
echo "Select deployment option:"
echo "1. Link to existing Railway project"
echo "2. Create new Railway project"
echo "3. Exit"

read -p "Enter option (1-3): " option

case $option in
    1)
        echo "Linking to existing Railway project..."
        railway link
        ;;
    2)
        echo "Creating new Railway project..."
        railway init
        ;;
    3)
        echo "Exiting..."
        exit 0
        ;;
    *)
        echo "Invalid option. Exiting..."
        exit 1
        ;;
esac

# Deploy to Railway
echo ""
echo "Deploying to Railway..."
railway up

# Get deployment URL
echo ""
echo "Deployment complete!"
echo "Your site should be available at the URL provided by Railway"
echo "You can also check the Railway dashboard for your deployment URL"