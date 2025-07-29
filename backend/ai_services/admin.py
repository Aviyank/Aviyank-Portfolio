from django.contrib import admin
from .models import (
    AIService, AIRequest, SentimentAnalysis, TextGeneration, 
    DataAnalysis, AIModel, AIUsage
)


@admin.register(AIService)
class AIServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'service_type', 'is_active', 'created_at']
    list_filter = ['service_type', 'is_active', 'created_at']
    search_fields = ['name', 'description']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(AIRequest)
class AIRequestAdmin(admin.ModelAdmin):
    list_display = ['service', 'user', 'status', 'processing_time', 'created_at']
    list_filter = ['service', 'status', 'created_at']
    search_fields = ['service__name', 'user__username', 'input_data']
    readonly_fields = ['created_at', 'completed_at', 'processing_time']
    actions = ['mark_as_completed', 'mark_as_failed']
    
    def mark_as_completed(self, request, queryset):
        queryset.update(status='completed')
    mark_as_completed.short_description = "Mark selected requests as completed"
    
    def mark_as_failed(self, request, queryset):
        queryset.update(status='failed')
    mark_as_failed.short_description = "Mark selected requests as failed"


@admin.register(SentimentAnalysis)
class SentimentAnalysisAdmin(admin.ModelAdmin):
    list_display = ['sentiment', 'confidence', 'text_preview', 'created_at']
    list_filter = ['sentiment', 'created_at']
    search_fields = ['text']
    readonly_fields = ['created_at']
    
    def text_preview(self, obj):
        return obj.text[:50] + '...' if len(obj.text) > 50 else obj.text
    text_preview.short_description = 'Text Preview'


@admin.register(TextGeneration)
class TextGenerationAdmin(admin.ModelAdmin):
    list_display = ['model_used', 'prompt_preview', 'created_at']
    list_filter = ['model_used', 'created_at']
    search_fields = ['prompt', 'generated_text']
    readonly_fields = ['created_at']
    
    def prompt_preview(self, obj):
        return obj.prompt[:50] + '...' if len(obj.prompt) > 50 else obj.prompt
    prompt_preview.short_description = 'Prompt Preview'


@admin.register(DataAnalysis)
class DataAnalysisAdmin(admin.ModelAdmin):
    list_display = ['name', 'analysis_type', 'created_at']
    list_filter = ['analysis_type', 'created_at']
    search_fields = ['name', 'insights']
    readonly_fields = ['created_at']


@admin.register(AIModel)
class AIModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'model_type', 'version', 'is_active', 'created_at']
    list_filter = ['model_type', 'is_active', 'created_at']
    search_fields = ['name', 'description']
    readonly_fields = ['created_at']


@admin.register(AIUsage)
class AIUsageAdmin(admin.ModelAdmin):
    list_display = ['service', 'user', 'date', 'requests_count', 'successful_requests', 'failed_requests']
    list_filter = ['service', 'date', 'user']
    search_fields = ['service__name', 'user__username']
    readonly_fields = ['created_at']
    ordering = ['-date', '-requests_count'] 