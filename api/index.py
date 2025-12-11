"""
Vercel serverless function for Django
This file is used by Vercel to handle all requests
"""
import os
import sys
from pathlib import Path

# Add backend to Python path
backend_path = Path(__file__).parent.parent / 'backend'
sys.path.insert(0, str(backend_path))

# Set Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.production')

# Import Django WSGI application
from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
