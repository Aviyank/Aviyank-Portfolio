#!/bin/bash

echo "🚀 Portfolio Deployment Script"
echo "================================"

# Check if we're in the right directory
if [ ! -f "backend/manage.py" ]; then
    echo "❌ Error: Please run this script from the project root directory"
    exit 1
fi

echo "📋 Pre-deployment checklist:"
echo ""

# Check if .env file exists
if [ ! -f "backend/.env" ]; then
    echo "⚠️  Warning: No .env file found in backend/"
    echo "   Create one with your environment variables before deploying"
    echo "   See backend/env.example for reference"
    echo ""
fi

# Check if requirements.txt exists
if [ ! -f "requirements.txt" ]; then
    echo "❌ Error: requirements.txt not found"
    exit 1
fi

echo "✅ Requirements file found"

# Check if Procfile exists
if [ ! -f "backend/Procfile" ]; then
    echo "❌ Error: Procfile not found in backend/"
    exit 1
fi

echo "✅ Procfile found"

# Check if runtime.txt exists
if [ ! -f "backend/runtime.txt" ]; then
    echo "❌ Error: runtime.txt not found in backend/"
    exit 1
fi

echo "✅ Runtime file found"

echo ""
echo "🎯 Next Steps:"
echo "=============="
echo ""
echo "1. Push your code to GitHub:"
echo "   git add ."
echo "   git commit -m 'Prepare for deployment'"
echo "   git push origin main"
echo ""
echo "2. Deploy to Railway:"
echo "   - Go to https://railway.app"
echo "   - Sign up with GitHub"
echo "   - Click 'New Project' → 'Deploy from GitHub repo'"
echo "   - Select your portfolio repository"
echo ""
echo "3. Configure Environment Variables in Railway:"
echo "   - SECRET_KEY=your-secret-key-here"
echo "   - DEBUG=False"
echo "   - OPENAI_API_KEY=your-api-key (optional)"
echo ""
echo "4. Add PostgreSQL Database:"
echo "   - In Railway dashboard, click 'New' → 'Database' → 'PostgreSQL'"
echo ""
echo "5. Your site will be live at: https://your-app-name.railway.app"
echo ""
echo "📚 For detailed instructions, see DEPLOYMENT.md"
echo ""
echo "🎉 Happy deploying!" 