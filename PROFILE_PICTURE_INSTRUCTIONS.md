# Profile Picture Replacement Instructions

## Overview
I've updated the templates to use a new profile picture file. Here's what you need to do to complete the replacement:

## Steps to Replace Profile Picture

### 1. Create the New Image File
- Save the anime portrait image as `backend/static/images/profile-picture.png`
- Recommended specifications:
  - Format: PNG (preferably with transparent background)
  - Size: 300x300 pixels or larger
  - Quality: High resolution for crisp display

### 2. Files Already Updated
I've already updated these template files to use the new profile picture:

- `backend/templates/portfolio/home.html` - Hero section profile picture
- `backend/templates/portfolio/about.html` - About page profile picture

### 3. Image Placement
The new image will be displayed as:
- A circular profile picture (300x300px on home page, 200x200px on about page)
- With a white border and shadow effect
- Responsive design that scales on mobile devices

### 4. Alternative Formats
If you prefer a different format, you can:
- Use JPG instead of PNG (update file extension in templates)
- Use SVG format for vector graphics
- Use WebP for better compression

### 5. Testing
After adding the image file:
1. Run `python manage.py collectstatic` to collect static files
2. Restart your Django development server
3. Visit the home and about pages to see the new profile picture

## Current Status
✅ Templates updated to use new image path
⏳ Waiting for actual image file to be added
⏳ Static files need to be collected after image is added

## Notes
- The image will automatically be styled with CSS for circular display
- The existing CSS classes handle responsive design and hover effects
- If you want to use the Django admin to upload profile pictures instead, you can use the Profile model's avatar field 