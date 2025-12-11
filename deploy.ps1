# Portfolio Deployment Script for Windows
Write-Host "🚀 Portfolio Deployment Script" -ForegroundColor Green
Write-Host "================================" -ForegroundColor Green

# Check if we're in the right directory
if (-not (Test-Path "backend/manage.py")) {
    Write-Host "❌ Error: Please run this script from the project root directory" -ForegroundColor Red
    exit 1
}

Write-Host "📋 Pre-deployment checklist:" -ForegroundColor Yellow
Write-Host ""

# Check if .env file exists
if (-not (Test-Path "backend/.env")) {
    Write-Host "⚠️  Warning: No .env file found in backend/" -ForegroundColor Yellow
    Write-Host "   Create one with your environment variables before deploying" -ForegroundColor Yellow
    Write-Host "   See backend/env.example for reference" -ForegroundColor Yellow
    Write-Host ""
}

# Check if requirements.txt exists
if (-not (Test-Path "requirements.txt")) {
    Write-Host "❌ Error: requirements.txt not found" -ForegroundColor Red
    exit 1
}

Write-Host "✅ Requirements file found" -ForegroundColor Green

# Check if Procfile exists
if (-not (Test-Path "backend/Procfile")) {
    Write-Host "❌ Error: Procfile not found in backend/" -ForegroundColor Red
    exit 1
}

Write-Host "✅ Procfile found" -ForegroundColor Green

# Check if runtime.txt exists
if (-not (Test-Path "backend/runtime.txt")) {
    Write-Host "❌ Error: runtime.txt not found in backend/" -ForegroundColor Red
    exit 1
}

Write-Host "✅ Runtime file found" -ForegroundColor Green

Write-Host ""
Write-Host "🎯 Next Steps:" -ForegroundColor Cyan
Write-Host "==============" -ForegroundColor Cyan
Write-Host ""
Write-Host "1. Push your code to GitHub:" -ForegroundColor White
Write-Host "   git add ." -ForegroundColor Gray
Write-Host "   git commit -m 'Prepare for deployment'" -ForegroundColor Gray
Write-Host "   git push origin main" -ForegroundColor Gray
Write-Host ""
Write-Host "2. Deploy to Railway:" -ForegroundColor White
Write-Host "   - Go to https://railway.app" -ForegroundColor Gray
Write-Host "   - Sign up with GitHub" -ForegroundColor Gray
Write-Host "   - Click 'New Project' -> 'Deploy from GitHub repo'" -ForegroundColor Gray
Write-Host "   - Select your portfolio repository" -ForegroundColor Gray
Write-Host ""
Write-Host "3. Configure Environment Variables in Railway:" -ForegroundColor White
Write-Host "   - SECRET_KEY=your-secret-key-here" -ForegroundColor Gray
Write-Host "   - DEBUG=False" -ForegroundColor Gray
Write-Host "   - OPENAI_API_KEY=your-api-key - optional" -ForegroundColor Gray
Write-Host ""
Write-Host "4. Add PostgreSQL Database:" -ForegroundColor White
Write-Host "   - In Railway dashboard, click 'New' -> 'Database' -> 'PostgreSQL'" -ForegroundColor Gray
Write-Host ""
Write-Host "5. Your site will be live at: https://your-app-name.railway.app" -ForegroundColor Green
Write-Host ""
Write-Host "📚 For detailed instructions, see DEPLOYMENT.md" -ForegroundColor Blue
Write-Host ""
Write-Host "🎉 Happy deploying!" -ForegroundColor Green 