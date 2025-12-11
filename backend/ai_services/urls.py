from django.urls import path
from . import views

app_name = 'ai_services'

urlpatterns = [
    # Dashboard and management views
    path('dashboard/', views.AIServicesView.as_view(), name='dashboard'),
    path('ai-dashboard/', views.ai_dashboard, name='ai_dashboard'),
    path('requests/<int:pk>/', views.AIRequestDetailView.as_view(), name='request_detail'),

    # API endpoint for models
    path('v1/models/', views.models_api, name='models_api'),

    # Demo pages
    path('sentiment-demo/', views.sentiment_demo, name='sentiment_demo'),
    path('text-generation-demo/', views.text_generation_demo, name='text_generation_demo'),
    path('data-analysis-demo/', views.data_analysis_demo, name='data_analysis_demo'),

    # API endpoints
    path('api/sentiment/', views.sentiment_analysis_api, name='sentiment_api'),
    path('api/text-generation/', views.text_generation_api, name='text_generation_api'),
    path('api/data-analysis/', views.data_analysis_api, name='data_analysis_api'),
    path('api/services/', views.ai_services_list_api, name='services_list_api'),
    path('api/usage-stats/', views.ai_usage_stats_api, name='usage_stats_api'),
    path('api/sentiment/history/', views.sentiment_history_api, name='sentiment_history_api'),
    path('api/text-generation/history/', views.text_generation_history_api, name='text_generation_history_api'),
    path('api/data-analysis/history/', views.data_analysis_history_api, name='data_analysis_history_api'),
]
