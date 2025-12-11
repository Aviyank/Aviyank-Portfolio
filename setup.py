#!/usr/bin/env python3
"""
Setup script for AI-Enhanced Portfolio Website
This script automates the initial setup process.
"""

import os
import sys
import subprocess
import secrets
from pathlib import Path

def run_command(command, cwd=None):
    """Run a shell command and return the result."""
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True, cwd=cwd)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {command}")
        print(f"Error: {e.stderr}")
        return None

def create_env_file():
    """Create .env file with default configuration."""
    env_content = f"""# Django Settings
SECRET_KEY={secrets.token_urlsafe(50)}
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# OpenAI API (optional - for text generation features)
OPENAI_API_KEY=your-openai-api-key-here

# Database (optional - defaults to SQLite)
# DATABASE_URL=postgresql://user:password@localhost:5432/dbname

# Email Settings (optional)
# EMAIL_HOST=smtp.gmail.com
# EMAIL_PORT=587
# EMAIL_USE_TLS=True
# EMAIL_HOST_USER=your-email@gmail.com
# EMAIL_HOST_PASSWORD=your-app-password
"""
    
    with open('.env', 'w') as f:
        f.write(env_content)
    print("✅ Created .env file with default configuration")

def check_python_version():
    """Check if Python version is compatible."""
    if sys.version_info < (3, 8):
        print("❌ Python 3.8 or higher is required")
        sys.exit(1)
    print(f"✅ Python {sys.version_info.major}.{sys.version_info.minor} detected")

def create_virtual_environment():
    """Create virtual environment if it doesn't exist."""
    if not os.path.exists('venv'):
        print("Creating virtual environment...")
        result = run_command('python -m venv venv')
        if result is not None:
            print("✅ Virtual environment created")
        else:
            print("❌ Failed to create virtual environment")
            sys.exit(1)
    else:
        print("✅ Virtual environment already exists")

def install_dependencies():
    """Install Python dependencies."""
    print("Installing dependencies...")
    
    # Determine the correct pip command
    if os.name == 'nt':  # Windows
        pip_cmd = 'venv\\Scripts\\pip'
    else:  # Unix/Linux/macOS
        pip_cmd = 'venv/bin/pip'
    
    result = run_command(f'{pip_cmd} install -r requirements.txt')
    if result is not None:
        print("✅ Dependencies installed successfully")
    else:
        print("❌ Failed to install dependencies")
        sys.exit(1)

def setup_database():
    """Set up the database."""
    print("Setting up database...")
    
    # Determine the correct python command
    if os.name == 'nt':  # Windows
        python_cmd = 'venv\\Scripts\\python'
    else:  # Unix/Linux/macOS
        python_cmd = 'venv/bin/python'
    
    # Change to backend directory
    os.chdir('backend')
    
    # Run migrations
    result = run_command(f'{python_cmd} manage.py makemigrations')
    if result is not None:
        print("✅ Database migrations created")
    
    result = run_command(f'{python_cmd} manage.py migrate')
    if result is not None:
        print("✅ Database migrations applied")
    else:
        print("❌ Failed to apply migrations")
        sys.exit(1)
    
    # Collect static files
    result = run_command(f'{python_cmd} manage.py collectstatic --noinput')
    if result is not None:
        print("✅ Static files collected")
    
    # Go back to root directory
    os.chdir('..')

def create_superuser():
    """Create a superuser account."""
    print("\n" + "="*50)
    print("SUPERUSER CREATION")
    print("="*50)
    print("You'll need to create a superuser account to access the admin panel.")
    print("Run the following command after activating your virtual environment:")
    print()
    
    if os.name == 'nt':  # Windows
        print("venv\\Scripts\\python backend\\manage.py createsuperuser")
    else:  # Unix/Linux/macOS
        print("venv/bin/python backend/manage.py createsuperuser")
    print()

def print_next_steps():
    """Print next steps for the user."""
    print("\n" + "="*50)
    print("SETUP COMPLETE! 🎉")
    print("="*50)
    print("Your AI-Enhanced Portfolio website is ready!")
    print()
    print("Next steps:")
    print("1. Activate your virtual environment:")
    if os.name == 'nt':  # Windows
        print("   venv\\Scripts\\activate")
    else:  # Unix/Linux/macOS
        print("   source venv/bin/activate")
    print()
    print("2. Create a superuser account:")
    if os.name == 'nt':  # Windows
        print("   venv\\Scripts\\python backend\\manage.py createsuperuser")
    else:  # Unix/Linux/macOS
        print("   venv/bin/python backend/manage.py createsuperuser")
    print()
    print("3. Start the development server:")
    if os.name == 'nt':  # Windows
        print("   venv\\Scripts\\python backend\\manage.py runserver")
    else:  # Unix/Linux/macOS
        print("   venv/bin/python backend/manage.py runserver")
    print()
    print("4. Open your browser and go to: http://localhost:8000")
    print()
    print("5. Access the admin panel at: http://localhost:8000/admin/")
    print()
    print("Optional:")
    print("- Get an OpenAI API key for text generation features")
    print("- Update the .env file with your API keys")
    print("- Customize the templates and styles")
    print()
    print("For more information, see the README.md file")
    print("="*50)

def main():
    """Main setup function."""
    print("🚀 AI-Enhanced Portfolio Website Setup")
    print("="*50)
    
    # Check Python version
    check_python_version()
    
    # Create .env file
    if not os.path.exists('.env'):
        create_env_file()
    else:
        print("✅ .env file already exists")
    
    # Create virtual environment
    create_virtual_environment()
    
    # Install dependencies
    install_dependencies()
    
    # Setup database
    setup_database()
    
    # Print superuser creation instructions
    create_superuser()
    
    # Print next steps
    print_next_steps()

if __name__ == '__main__':
    main() 