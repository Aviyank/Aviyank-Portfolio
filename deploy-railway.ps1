# Railway Deployment Script for Windows
Write-Host "🚂 Railway Deployment Script" -ForegroundColor Green
Write-Host "================================" -ForegroundColor Green

# Check if we're in the right directory
if (-not (Test-Path "backend/manage.py")) {
    Write-Host "❌ Error: Please run this script from the project root directory" -ForegroundColor Red
    exit 1
}

Write-Host "📋 Pre-deployment checklist:" -ForegroundColor Yellow
Write-Host ""

# Check if railway CLI is installed
try {
    $railwayVersion = railway version
    Write-Host "✅ Railway CLI found: $railwayVersion" -ForegroundColor Green
} catch {
    Write-Host "❌ Railway CLI not found" -ForegroundColor Red
    Write-Host "Please install Railway CLI with: npm i -g @railway/cli" -ForegroundColor Yellow
    Write-Host "Then login with: railway login" -ForegroundColor Yellow
    exit 1
}

# Check if user is logged in to Railway
try {
    $railwayStatus = railway status
    if ($railwayStatus -match "Not logged in") {
        Write-Host "❌ Not logged in to Railway" -ForegroundColor Red
        Write-Host "Please login with: railway login" -ForegroundColor Yellow
        exit 1
    }
    Write-Host "✅ Logged in to Railway" -ForegroundColor Green
} catch {
    Write-Host "❌ Error checking Railway login status" -ForegroundColor Red
    Write-Host "Please login with: railway login" -ForegroundColor Yellow
    exit 1
}

# Check if .env file exists
if (-not (Test-Path "backend/.env")) {
    Write-Host "⚠️  Warning: No .env file found in backend/" -ForegroundColor Yellow
    Write-Host "   Environment variables should be configured in Railway dashboard" -ForegroundColor Yellow
    Write-Host "   See backend/env.example for reference" -ForegroundColor Yellow
    Write-Host ""
}

# Check if railway.json exists
if (-not (Test-Path "railway.json")) {
    Write-Host "❌ Error: railway.json not found" -ForegroundColor Red
    Write-Host "This file is required for Railway deployment" -ForegroundColor Yellow
    exit 1
}

Write-Host "✅ railway.json found" -ForegroundColor Green

# Deployment options
Write-Host ""
Write-Host "Select deployment option:" -ForegroundColor Cyan
Write-Host "1. Link to existing Railway project" -ForegroundColor Cyan
Write-Host "2. Create new Railway project" -ForegroundColor Cyan
Write-Host "3. Exit" -ForegroundColor Cyan

$option = Read-Host "Enter option (1-3)"

switch ($option) {
    "1" {
        Write-Host "Linking to existing Railway project..." -ForegroundColor Green
        railway link
    }
    "2" {
        Write-Host "Creating new Railway project..." -ForegroundColor Green
        railway init
    }
    "3" {
        Write-Host "Exiting..." -ForegroundColor Yellow
        exit 0
    }
    default {
        Write-Host "Invalid option. Exiting..." -ForegroundColor Red
        exit 1
    }
}

# Deploy to Railway
Write-Host ""
Write-Host "Deploying to Railway..." -ForegroundColor Green
railway up

# Get deployment URL
Write-Host ""
Write-Host "Deployment complete!" -ForegroundColor Green
Write-Host "Your site should be available at the URL provided by Railway" -ForegroundColor Green
Write-Host "You can also check the Railway dashboard for your deployment URL" -ForegroundColor Green