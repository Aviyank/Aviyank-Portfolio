#!/usr/bin/env python3
"""
Profile Picture Update Script
Automatically copies profile pictures from profile_images folder to Django static files
"""

import os
import shutil
import glob
from pathlib import Path

def update_profile_picture():
    """Update profile picture from profile_images folder"""
    
    # Define paths
    project_root = Path(__file__).parent
    profile_images_dir = project_root / "profile_images"
    django_static_dir = project_root / "backend" / "static" / "images"
    
    # Check if profile_images directory exists
    if not profile_images_dir.exists():
        print("❌ profile_images directory not found!")
        print("Please create the profile_images folder first.")
        return False
    
    # Look for profile picture files
    profile_picture_patterns = [
        "profile-picture.*",
        "avatar.*", 
        "me.*",
        "portrait.*"
    ]
    
    found_files = []
    for pattern in profile_picture_patterns:
        files = glob.glob(str(profile_images_dir / pattern))
        found_files.extend(files)
    
    if not found_files:
        print("❌ No profile picture found in profile_images folder!")
        print("Please add your profile picture to the profile_images folder.")
        print("Supported formats: PNG, JPG, JPEG, SVG, WebP")
        return False
    
    # Use the first found file
    source_file = Path(found_files[0])
    file_extension = source_file.suffix.lower()
    
    # Determine target filename
    if file_extension in ['.png', '.jpg', '.jpeg', '.svg', '.webp']:
        target_filename = f"profile-picture{file_extension}"
    else:
        target_filename = "profile-picture.png"
    
    target_file = django_static_dir / target_filename
    
    try:
        # Copy the file
        shutil.copy2(source_file, target_file)
        print(f"✅ Successfully copied {source_file.name} to {target_file}")
        
        # Update Django templates to use the correct file extension
        update_templates(file_extension)
        
        # Collect static files
        collect_static_files()
        
        print("🎉 Profile picture updated successfully!")
        print(f"📁 Source: {source_file}")
        print(f"📁 Target: {target_file}")
        print("🔄 Please restart your Django development server to see the changes.")
        
        return True
        
    except Exception as e:
        print(f"❌ Error copying file: {e}")
        return False

def update_templates(file_extension):
    """Update Django templates to use the correct file extension"""
    
    project_root = Path(__file__).parent
    templates = [
        project_root / "backend" / "templates" / "portfolio" / "home.html",
        project_root / "backend" / "templates" / "portfolio" / "about.html"
    ]
    
    for template_file in templates:
        if template_file.exists():
            try:
                with open(template_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Update the image source to use the correct extension
                old_pattern = r"{% static 'images/profile-picture\.(png|svg|jpg|jpeg|webp)' %}"
                new_source = f"{{% static 'images/profile-picture{file_extension}' %}}"
                
                # Simple replacement for now
                content = content.replace("{% static 'images/profile-picture.svg' %}", new_source)
                content = content.replace("{% static 'images/profile-picture.png' %}", new_source)
                
                with open(template_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                print(f"✅ Updated template: {template_file.name}")
                
            except Exception as e:
                print(f"⚠️  Warning: Could not update template {template_file.name}: {e}")

def collect_static_files():
    """Collect Django static files"""
    
    project_root = Path(__file__).parent
    backend_dir = project_root / "backend"
    
    if backend_dir.exists():
        try:
            import subprocess
            import sys
            
            # Change to backend directory
            os.chdir(backend_dir)
            
            # Run collectstatic
            result = subprocess.run([
                sys.executable, "manage.py", "collectstatic", "--noinput"
            ], capture_output=True, text=True)
            
            if result.returncode == 0:
                print("✅ Static files collected successfully")
            else:
                print(f"⚠️  Warning: Static file collection failed: {result.stderr}")
                
        except Exception as e:
            print(f"⚠️  Warning: Could not collect static files: {e}")

if __name__ == "__main__":
    print("🔄 Updating profile picture...")
    print("=" * 50)
    
    success = update_profile_picture()
    
    if success:
        print("=" * 50)
        print("🎉 Profile picture update completed!")
        print("📝 Next steps:")
        print("   1. Restart your Django development server")
        print("   2. Visit your portfolio website")
        print("   3. Check the home and about pages")
    else:
        print("=" * 50)
        print("❌ Profile picture update failed!")
        print("📝 Please check the error messages above.") 