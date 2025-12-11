"""
Vercel serverless function entry point for Django
"""
import os
import sys

# Add the backend directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'backend'))

# Set Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')

# Import Django WSGI application
from django.core.wsgi import get_wsgi_application

# Get the WSGI application
application = get_wsgi_application()

# Export for Vercel
def handler(request):
    """Vercel serverless function handler"""
    return application(request.environ, request.start_response)

