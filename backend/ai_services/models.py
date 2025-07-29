from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class AIService(models.Model):
    """Base model for AI services."""
    SERVICE_TYPES = [
        ('sentiment', 'Sentiment Analysis'),
        ('text_gen', 'Text Generation'),
        ('data_analysis', 'Data Analysis'),
        ('image_gen', 'Image Generation'),
        ('code_gen', 'Code Generation'),
        ('translation', 'Translation'),
    ]
    
    name = models.CharField(max_length=100)
    service_type = models.CharField(max_length=20, choices=SERVICE_TYPES)
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.get_service_type_display()})"


class AIRequest(models.Model):
    """Model to track AI service requests."""
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    service = models.ForeignKey(AIService, on_delete=models.CASCADE)
    input_data = models.TextField()
    output_data = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    ], default='pending')
    error_message = models.TextField(blank=True)
    processing_time = models.FloatField(null=True, blank=True)  # in seconds
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.service.name} - {self.status} ({self.created_at})"


class SentimentAnalysis(models.Model):
    """Model for sentiment analysis results."""
    text = models.TextField()
    sentiment = models.CharField(max_length=20, choices=[
        ('positive', 'Positive'),
        ('negative', 'Negative'),
        ('neutral', 'Neutral'),
    ])
    confidence = models.FloatField()  # 0.0 to 1.0
    keywords = models.JSONField(default=list)  # List of important keywords
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sentiment} ({self.confidence:.2f}) - {self.text[:50]}..."


class TextGeneration(models.Model):
    """Model for text generation results."""
    prompt = models.TextField()
    generated_text = models.TextField()
    model_used = models.CharField(max_length=100)
    parameters = models.JSONField(default=dict)  # Generation parameters
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.model_used} - {self.prompt[:50]}..."


class DataAnalysis(models.Model):
    """Model for data analysis results."""
    ANALYSIS_TYPES = [
        ('descriptive', 'Descriptive Statistics'),
        ('correlation', 'Correlation Analysis'),
        ('trend', 'Trend Analysis'),
        ('prediction', 'Prediction Model'),
        ('clustering', 'Clustering Analysis'),
    ]
    
    name = models.CharField(max_length=200)
    analysis_type = models.CharField(max_length=20, choices=ANALYSIS_TYPES)
    input_data = models.JSONField()  # Input data structure
    results = models.JSONField()  # Analysis results
    visualizations = models.JSONField(default=list)  # Chart configurations
    insights = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.get_analysis_type_display()})"


class AIModel(models.Model):
    """Model for AI model configurations."""
    name = models.CharField(max_length=100)
    model_type = models.CharField(max_length=50)
    version = models.CharField(max_length=20)
    description = models.TextField()
    parameters = models.JSONField(default=dict)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} v{self.version}"


class AIUsage(models.Model):
    """Model to track AI service usage statistics."""
    service = models.ForeignKey(AIService, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    requests_count = models.IntegerField(default=0)
    successful_requests = models.IntegerField(default=0)
    failed_requests = models.IntegerField(default=0)
    total_processing_time = models.FloatField(default=0.0)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['service', 'user', 'date']
        ordering = ['-date']

    def __str__(self):
        return f"{self.service.name} - {self.date} ({self.requests_count} requests)" 