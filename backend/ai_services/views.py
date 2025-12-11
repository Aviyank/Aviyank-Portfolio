from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
import json

from .models import AIService, AIRequest, SentimentAnalysis, TextGeneration, DataAnalysis
from .services import SentimentAnalysisService, TextGenerationService, DataAnalysisService, AIServiceManager


class AIServicesView(LoginRequiredMixin, ListView):
    """View for AI services dashboard."""
    model = AIService
    template_name = 'ai_services/dashboard.html'
    context_object_name = 'services'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        manager = AIServiceManager()
        context['usage_stats'] = manager.get_service_usage_stats(self.request.user, days=7)
        context['recent_requests'] = manager.get_recent_requests(self.request.user, limit=5)
        return context


class AIRequestDetailView(LoginRequiredMixin, DetailView):
    """View for AI request details."""
    model = AIRequest
    template_name = 'ai_services/request_detail.html'
    context_object_name = 'request'


# API Views
@api_view(['POST'])
@permission_classes([AllowAny])
def sentiment_analysis_api(request):
    """API endpoint for sentiment analysis."""
    try:
        data = request.data
        text = data.get('text', '').strip()
        
        if not text:
            return Response({
                'error': 'Text is required'
            }, status=status.HTTP_400_BAD_REQUEST)
        
        service = SentimentAnalysisService()
        result = service.analyze_sentiment(text, request.user)
        
        return Response(result, status=status.HTTP_200_OK)
        
    except Exception as e:
        return Response({
            'error': str(e)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
@permission_classes([AllowAny])
def text_generation_api(request):
    """API endpoint for text generation."""
    try:
        data = request.data
        prompt = data.get('prompt', '').strip()
        max_tokens = data.get('max_tokens', 100)
        temperature = data.get('temperature', 0.7)
        
        if not prompt:
            return Response({
                'error': 'Prompt is required'
            }, status=status.HTTP_400_BAD_REQUEST)
        
        service = TextGenerationService()
        result = service.generate_text(
            prompt=prompt,
            user=request.user,
            max_tokens=max_tokens,
            temperature=temperature
        )
        
        return Response(result, status=status.HTTP_200_OK)
        
    except Exception as e:
        return Response({
            'error': str(e)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
@permission_classes([AllowAny])
def data_analysis_api(request):
    """API endpoint for data analysis."""
    try:
        data = request.data
        input_data = data.get('data')
        analysis_type = data.get('analysis_type', 'descriptive')
        
        if not input_data:
            return Response({
                'error': 'Data is required'
            }, status=status.HTTP_400_BAD_REQUEST)
        
        service = DataAnalysisService()
        result = service.analyze_data(
            data=input_data,
            analysis_type=analysis_type,
            user=request.user
        )
        
        return Response(result, status=status.HTTP_200_OK)
        
    except Exception as e:
        return Response({
            'error': str(e)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
@permission_classes([AllowAny])
def ai_services_list_api(request):
    """API endpoint to list available AI services."""
    try:
        services = AIService.objects.filter(is_active=True)
        data = [{
            'id': service.id,
            'name': service.name,
            'service_type': service.service_type,
            'description': service.description,
        } for service in services]
        
        return Response(data, status=status.HTTP_200_OK)
        
    except Exception as e:
        return Response({
            'error': str(e)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
@permission_classes([AllowAny])
def ai_usage_stats_api(request):
    """API endpoint for AI usage statistics."""
    try:
        manager = AIServiceManager()
        days = int(request.GET.get('days', 30))
        user = request.user if request.user.is_authenticated else None
        
        usage_stats = manager.get_service_usage_stats(user, days)
        
        data = [{
            'service_name': stat.service.name,
            'date': stat.date,
            'requests_count': stat.requests_count,
            'successful_requests': stat.successful_requests,
            'failed_requests': stat.failed_requests,
            'total_processing_time': stat.total_processing_time,
        } for stat in usage_stats]
        
        return Response(data, status=status.HTTP_200_OK)
        
    except Exception as e:
        return Response({
            'error': str(e)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
@permission_classes([AllowAny])
def sentiment_history_api(request):
    """API endpoint for sentiment analysis history."""
    try:
        analyses = SentimentAnalysis.objects.all().order_by('-created_at')[:50]
        
        data = [{
            'id': analysis.id,
            'text': analysis.text[:100] + '...' if len(analysis.text) > 100 else analysis.text,
            'sentiment': analysis.sentiment,
            'confidence': analysis.confidence,
            'keywords': analysis.keywords,
            'created_at': analysis.created_at,
        } for analysis in analyses]
        
        return Response(data, status=status.HTTP_200_OK)
        
    except Exception as e:
        return Response({
            'error': str(e)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
@permission_classes([AllowAny])
def text_generation_history_api(request):
    """API endpoint for text generation history."""
    try:
        generations = TextGeneration.objects.all().order_by('-created_at')[:50]
        
        data = [{
            'id': generation.id,
            'prompt': generation.prompt[:100] + '...' if len(generation.prompt) > 100 else generation.prompt,
            'generated_text': generation.generated_text[:200] + '...' if len(generation.generated_text) > 200 else generation.generated_text,
            'model_used': generation.model_used,
            'parameters': generation.parameters,
            'created_at': generation.created_at,
        } for generation in generations]
        
        return Response(data, status=status.HTTP_200_OK)
        
    except Exception as e:
        return Response({
            'error': str(e)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
@permission_classes([AllowAny])
def data_analysis_history_api(request):
    """API endpoint for data analysis history."""
    try:
        analyses = DataAnalysis.objects.all().order_by('-created_at')[:50]
        
        data = [{
            'id': analysis.id,
            'name': analysis.name,
            'analysis_type': analysis.analysis_type,
            'insights': analysis.insights,
            'created_at': analysis.created_at,
        } for analysis in analyses]
        
        return Response(data, status=status.HTTP_200_OK)
        
    except Exception as e:
        return Response({
            'error': str(e)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
@permission_classes([AllowAny])
def models_api(request):
    """API endpoint for models."""
    data = {"message": "This is the /v1/models endpoint.", "version": "1.0"}
    return Response(data, status=status.HTTP_200_OK)


# Demo views for frontend
def sentiment_demo(request):
    """Demo page for sentiment analysis."""
    return render(request, 'ai_services/sentiment_demo.html')


def text_generation_demo(request):
    """Demo page for text generation."""
    return render(request, 'ai_services/text_generation_demo.html')


def data_analysis_demo(request):
    """Demo page for data analysis."""
    return render(request, 'ai_services/data_analysis_demo.html')


def ai_dashboard(request):
    """Main AI services dashboard."""
    manager = AIServiceManager()
    context = {
        'services': manager.get_available_services(),
        'usage_stats': manager.get_service_usage_stats(request.user if request.user.is_authenticated else None, days=7),
        'recent_requests': manager.get_recent_requests(request.user if request.user.is_authenticated else None, limit=10),
    }
    return render(request, 'ai_services/ai_dashboard.html', context)
