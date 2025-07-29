"""
URL configuration for portfolio project.
"""
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib import admin



urlpatterns = [
    path('admin/', admin.site.urls),
    # Main pages
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('projects/', views.ProjectListView.as_view(), name='projects'),
    path('projects/<int:pk>/', views.ProjectDetailView.as_view(), name='project_detail'),
    path('blog/', views.BlogPostListView.as_view(), name='blog'),
    path('blog/<slug:slug>/', views.BlogPostDetailView.as_view(), name='blog_detail'),
    path('contact/', views.contact, name='contact'),
    
    # API endpoints
    path('api/contact/', views.contact_api, name='contact_api'),
    path('api/skills/', views.skills_api, name='skills_api'),
    path('api/projects/', views.projects_api, name='projects_api'),
    
    # Admin views (require login)
    path('dashboard/', views.dashboard, name='dashboard'),
    
    # Project management
    path('projects/create/', views.ProjectCreateView.as_view(), name='project_create'),
    path('projects/<int:pk>/update/', views.ProjectUpdateView.as_view(), name='project_update'),
    path('projects/<int:pk>/delete/', views.ProjectDeleteView.as_view(), name='project_delete'),
    
    # Blog management
    path('blog/create/', views.BlogPostCreateView.as_view(), name='blog_create'),
    path('blog/<slug:slug>/update/', views.BlogPostUpdateView.as_view(), name='blog_update'),
    path('blog/<slug:slug>/delete/', views.BlogPostDeleteView.as_view(), name='blog_delete'),

    path('ai_services/', include('ai_services.urls', namespace='ai_services')),
]

# Serve static files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 