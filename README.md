# AI-Enhanced Portfolio Website

A modern, interactive portfolio website built with Django backend and AI/ML capabilities. This project showcases professional skills, projects, and cutting-edge AI services including sentiment analysis, text generation, and data analysis.

## 🚀 Features

### Core Portfolio Features
- **Professional Portfolio**: Showcase projects, skills, experience, and education
- **Blog System**: Write and publish technical articles and insights
- **Contact Management**: Handle contact form submissions with admin interface
- **Responsive Design**: Modern, mobile-friendly UI with Bootstrap 5
- **Admin Dashboard**: Complete Django admin interface for content management

### AI/ML Services
- **Sentiment Analysis**: Analyze text sentiment using NLP techniques
- **Text Generation**: Generate creative text using OpenAI API
- **Data Analysis**: Comprehensive data analysis with automated insights
- **Interactive Demos**: Live demonstrations of AI capabilities
- **Usage Tracking**: Monitor AI service usage and performance

### Technical Features
- **Django REST Framework**: Robust API endpoints for frontend integration
- **Database Models**: Comprehensive data models for all portfolio content
- **Static File Management**: Optimized CSS, JS, and image handling
- **Security**: CSRF protection, form validation, and secure configurations
- **Performance**: Optimized queries, caching, and efficient data handling

## 🛠️ Technology Stack

### Backend
- **Django 4.2.7**: Web framework
- **Django REST Framework**: API development
- **SQLite**: Database (easily configurable for PostgreSQL/MySQL)
- **Python 3.8+**: Programming language

### AI/ML Libraries
- **OpenAI API**: Text generation
- **TextBlob**: Sentiment analysis
- **scikit-learn**: Machine learning algorithms
- **pandas**: Data manipulation
- **numpy**: Numerical computing
- **matplotlib/seaborn**: Data visualization
- **plotly**: Interactive charts

### Frontend
- **Bootstrap 5**: CSS framework
- **FontAwesome**: Icons
- **jQuery**: JavaScript library
- **Custom CSS/JS**: Tailored styling and interactions

## 📋 Prerequisites

Before running this project, make sure you have:

- Python 3.8 or higher
- pip (Python package installer)
- Git
- OpenAI API key (for text generation features)

## 🚀 Installation & Setup

### 1. Clone the Repository
```bash
git clone <repository-url>
cd portfolio
```

### 2. Create Virtual Environment
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Environment Configuration
Create a `.env` file in the project root:
```env
SECRET_KEY=your-secret-key-here
DEBUG=True
OPENAI_API_KEY=your-openai-api-key-here
```

### 5. Database Setup
```bash
cd backend
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Superuser
```bash
python manage.py createsuperuser
```

### 7. Collect Static Files
```bash
python manage.py collectstatic
```

### 8. Run the Development Server
```bash
python manage.py runserver
```

Visit `http://localhost:8000` to see your portfolio website!

## 📁 Project Structure

```
portfolio/
├── backend/                    # Django application
│   ├── ai_services/           # AI/ML services
│   │   ├── models.py          # AI service models
│   │   ├── services.py        # AI service implementations
│   │   ├── views.py           # AI service views
│   │   └── urls.py            # AI service URLs
│   ├── portfolio/             # Main Django app
│   │   ├── models.py          # Portfolio models
│   │   ├── views.py           # Portfolio views
│   │   ├── forms.py           # Django forms
│   │   ├── admin.py           # Admin interface
│   │   └── urls.py            # Portfolio URLs
│   ├── templates/             # HTML templates
│   │   ├── base.html          # Base template
│   │   ├── portfolio/         # Portfolio templates
│   │   └── ai_services/       # AI service templates
│   ├── static/                # Static files
│   │   ├── css/               # Stylesheets
│   │   ├── js/                # JavaScript files
│   │   └── images/            # Images
│   └── manage.py              # Django management script
├── requirements.txt           # Python dependencies
└── README.md                 # Project documentation
```

## 🎯 Usage Guide

### Adding Portfolio Content

1. **Access Admin Panel**: Go to `http://localhost:8000/admin/`
2. **Login**: Use your superuser credentials
3. **Add Content**:
   - **Profile**: Update your personal information
   - **Skills**: Add technical skills with proficiency levels
   - **Projects**: Showcase your work with descriptions and links
   - **Experience**: Add work history and achievements
   - **Education**: Include academic background
   - **Blog Posts**: Write and publish articles

### AI Services

#### Sentiment Analysis
- Navigate to AI Services Dashboard
- Enter text in the sentiment analysis form
- Get instant sentiment analysis with confidence scores

#### Text Generation
- Use the text generation demo
- Enter prompts and adjust parameters
- Generate creative text using OpenAI API

#### Data Analysis
- Input JSON data in the data analysis form
- Choose analysis type (descriptive, correlation, trend, clustering)
- Get automated insights and visualizations

### Customization

#### Styling
- Modify `backend/static/css/style.css` for custom styles
- Update color variables in CSS root for theme changes
- Add custom animations and effects

#### Content
- Edit templates in `backend/templates/` for layout changes
- Modify models in `backend/portfolio/models.py` for data structure
- Update forms in `backend/portfolio/forms.py` for form customization

#### AI Services
- Extend AI services in `backend/ai_services/services.py`
- Add new service types in `backend/ai_services/models.py`
- Create new API endpoints in `backend/ai_services/views.py`

## 🔧 Configuration

### Database Configuration
The project uses SQLite by default. To use PostgreSQL or MySQL:

1. Install database adapter:
```bash
# For PostgreSQL
pip install psycopg2-binary

# For MySQL
pip install mysqlclient
```

2. Update `backend/portfolio/settings.py`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',  # or mysql
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',  # or 3306 for MySQL
    }
}
```

### OpenAI Configuration
To use text generation features:

1. Get an OpenAI API key from [OpenAI Platform](https://platform.openai.com/)
2. Add to your `.env` file:
```env
OPENAI_API_KEY=your-api-key-here
```

### Production Deployment

1. **Update Settings**:
```python
DEBUG = False
ALLOWED_HOSTS = ['your-domain.com', 'www.your-domain.com']
```

2. **Static Files**:
```bash
python manage.py collectstatic
```

3. **Database**:
```bash
python manage.py migrate
```

4. **Web Server**: Use Gunicorn with Nginx or Apache

## 🧪 Testing

Run tests to ensure everything works correctly:

```bash
python manage.py test
```

## 📊 API Endpoints

### Portfolio API
- `GET /api/skills/` - Get all skills
- `GET /api/projects/` - Get all projects
- `POST /api/contact/` - Submit contact form

### AI Services API
- `POST /api/sentiment/` - Sentiment analysis
- `POST /api/text-generation/` - Text generation
- `POST /api/data-analysis/` - Data analysis
- `GET /api/services/` - List available services
- `GET /api/usage-stats/` - Usage statistics

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Commit changes: `git commit -am 'Add feature'`
4. Push to branch: `git push origin feature-name`
5. Submit a pull request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

If you encounter any issues:

1. Check the Django debug page for error details
2. Review the console logs for JavaScript errors
3. Verify your environment variables are set correctly
4. Ensure all dependencies are installed

## 🎉 Acknowledgments

- Django community for the excellent web framework
- Bootstrap team for the responsive CSS framework
- OpenAI for providing the text generation API
- All contributors and users of this project

---

**Happy coding! 🚀**

This AI-Enhanced Portfolio website demonstrates modern web development practices while showcasing AI/ML capabilities. Perfect for developers looking to create an impressive online presence with cutting-edge technology. 