import time
import json
import numpy as np
import pandas as pd
from textblob import TextBlob
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import openai
from django.conf import settings
from django.utils import timezone
from .models import (
    AIService, AIRequest, SentimentAnalysis, TextGeneration, 
    DataAnalysis, AIModel, AIUsage
)


class BaseAIService:
    """Base class for AI services."""
    
    def __init__(self, service_name):
        self.service = AIService.objects.get(name=service_name)
        self.start_time = None
    
    def start_request(self, user=None, input_data=""):
        """Start tracking an AI request."""
        self.request = AIRequest.objects.create(
            user=user,
            service=self.service,
            input_data=input_data,
            status='processing'
        )
        self.start_time = time.time()
        return self.request
    
    def complete_request(self, output_data, error_message=""):
        """Complete the AI request."""
        processing_time = time.time() - self.start_time if self.start_time else None
        
        self.request.output_data = output_data
        self.request.error_message = error_message
        self.request.processing_time = processing_time
        self.request.completed_at = timezone.now()
        
        if error_message:
            self.request.status = 'failed'
        else:
            self.request.status = 'completed'
        
        self.request.save()
        
        # Update usage statistics
        self._update_usage_stats()
        
        return self.request
    
    def _update_usage_stats(self):
        """Update usage statistics."""
        today = timezone.now().date()
        usage, created = AIUsage.objects.get_or_create(
            service=self.service,
            user=self.request.user,
            date=today,
            defaults={
                'requests_count': 0,
                'successful_requests': 0,
                'failed_requests': 0,
                'total_processing_time': 0.0
            }
        )
        
        usage.requests_count += 1
        if self.request.status == 'completed':
            usage.successful_requests += 1
        else:
            usage.failed_requests += 1
        
        if self.request.processing_time:
            usage.total_processing_time += self.request.processing_time
        
        usage.save()


class SentimentAnalysisService(BaseAIService):
    """Service for sentiment analysis."""
    
    def __init__(self):
        super().__init__('Sentiment Analysis')
    
    def analyze_sentiment(self, text, user=None):
        """Analyze sentiment of given text."""
        self.start_request(user, text)
        
        try:
            # Use TextBlob for sentiment analysis
            blob = TextBlob(text)
            polarity = blob.sentiment.polarity
            subjectivity = blob.sentiment.subjectivity
            
            # Determine sentiment
            if polarity > 0.1:
                sentiment = 'positive'
            elif polarity < -0.1:
                sentiment = 'negative'
            else:
                sentiment = 'neutral'
            
            # Calculate confidence based on subjectivity
            confidence = abs(polarity) * (1 - subjectivity)
            
            # Extract keywords (simple approach)
            words = text.lower().split()
            keywords = [word for word in words if len(word) > 3][:10]
            
            # Save result
            analysis = SentimentAnalysis.objects.create(
                text=text,
                sentiment=sentiment,
                confidence=confidence,
                keywords=keywords
            )
            
            result = {
                'sentiment': sentiment,
                'confidence': round(confidence, 3),
                'polarity': round(polarity, 3),
                'subjectivity': round(subjectivity, 3),
                'keywords': keywords,
                'analysis_id': analysis.id
            }
            
            self.complete_request(json.dumps(result))
            return result
            
        except Exception as e:
            self.complete_request("", str(e))
            raise


class TextGenerationService(BaseAIService):
    """Service for text generation using OpenAI."""
    
    def __init__(self):
        super().__init__('Text Generation')
        if settings.OPENAI_API_KEY:
            openai.api_key = settings.OPENAI_API_KEY
    
    def generate_text(self, prompt, user=None, max_tokens=100, temperature=0.7):
        """Generate text using OpenAI API."""
        self.start_request(user, prompt)
        
        try:
            if not settings.OPENAI_API_KEY:
                raise ValueError("OpenAI API key not configured")
            
            response = openai.ChatCompletion.create(
                model=settings.AI_MODEL_CONFIG['default_model'],
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=max_tokens,
                temperature=temperature
            )
            
            generated_text = response.choices[0].message.content
            
            # Save result
            generation = TextGeneration.objects.create(
                prompt=prompt,
                generated_text=generated_text,
                model_used=settings.AI_MODEL_CONFIG['default_model'],
                parameters={
                    'max_tokens': max_tokens,
                    'temperature': temperature
                }
            )
            
            result = {
                'generated_text': generated_text,
                'model_used': settings.AI_MODEL_CONFIG['default_model'],
                'parameters': {
                    'max_tokens': max_tokens,
                    'temperature': temperature
                },
                'generation_id': generation.id
            }
            
            self.complete_request(json.dumps(result))
            return result
            
        except Exception as e:
            self.complete_request("", str(e))
            raise


class DataAnalysisService(BaseAIService):
    """Service for data analysis."""
    
    def __init__(self):
        super().__init__('Data Analysis')
    
    def analyze_data(self, data, analysis_type='descriptive', user=None):
        """Analyze data and generate insights."""
        self.start_request(user, json.dumps(data))
        
        try:
            # Convert data to pandas DataFrame
            if isinstance(data, list):
                df = pd.DataFrame(data)
            elif isinstance(data, dict):
                df = pd.DataFrame([data])
            else:
                df = pd.DataFrame(data)
            
            results = {}
            visualizations = []
            
            if analysis_type == 'descriptive':
                results = self._descriptive_analysis(df)
                visualizations = self._create_descriptive_charts(df)
            elif analysis_type == 'correlation':
                results = self._correlation_analysis(df)
                visualizations = self._create_correlation_charts(df)
            elif analysis_type == 'trend':
                results = self._trend_analysis(df)
                visualizations = self._create_trend_charts(df)
            elif analysis_type == 'clustering':
                results = self._clustering_analysis(df)
                visualizations = self._create_clustering_charts(df)
            
            # Generate insights
            insights = self._generate_insights(results, analysis_type)
            
            # Save result
            analysis = DataAnalysis.objects.create(
                name=f"{analysis_type.title()} Analysis",
                analysis_type=analysis_type,
                input_data=data,
                results=results,
                visualizations=visualizations,
                insights=insights
            )
            
            result = {
                'analysis_type': analysis_type,
                'results': results,
                'visualizations': visualizations,
                'insights': insights,
                'analysis_id': analysis.id
            }
            
            self.complete_request(json.dumps(result))
            return result
            
        except Exception as e:
            self.complete_request("", str(e))
            raise
    
    def _descriptive_analysis(self, df):
        """Perform descriptive statistical analysis."""
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        
        results = {
            'summary': df.describe().to_dict(),
            'missing_values': df.isnull().sum().to_dict(),
            'data_types': df.dtypes.astype(str).to_dict(),
            'shape': df.shape,
            'columns': list(df.columns)
        }
        
        if len(numeric_cols) > 0:
            results['numeric_summary'] = {
                'mean': df[numeric_cols].mean().to_dict(),
                'median': df[numeric_cols].median().to_dict(),
                'std': df[numeric_cols].std().to_dict(),
                'min': df[numeric_cols].min().to_dict(),
                'max': df[numeric_cols].max().to_dict()
            }
        
        return results
    
    def _correlation_analysis(self, df):
        """Perform correlation analysis."""
        numeric_df = df.select_dtypes(include=[np.number])
        
        if numeric_df.shape[1] < 2:
            return {'error': 'Need at least 2 numeric columns for correlation analysis'}
        
        correlation_matrix = numeric_df.corr()
        
        return {
            'correlation_matrix': correlation_matrix.to_dict(),
            'high_correlations': self._find_high_correlations(correlation_matrix)
        }
    
    def _trend_analysis(self, df):
        """Perform trend analysis."""
        # Simple trend analysis - can be enhanced
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        
        trends = {}
        for col in numeric_cols:
            values = df[col].dropna()
            if len(values) > 1:
                # Calculate simple linear trend
                x = np.arange(len(values))
                slope = np.polyfit(x, values, 1)[0]
                trends[col] = {
                    'slope': slope,
                    'trend': 'increasing' if slope > 0 else 'decreasing' if slope < 0 else 'stable',
                    'change_rate': slope / values.mean() if values.mean() != 0 else 0
                }
        
        return {'trends': trends}
    
    def _clustering_analysis(self, df):
        """Perform clustering analysis."""
        numeric_df = df.select_dtypes(include=[np.number])
        
        if numeric_df.shape[1] < 2:
            return {'error': 'Need at least 2 numeric columns for clustering'}
        
        # Normalize data
        normalized_data = (numeric_df - numeric_df.mean()) / numeric_df.std()
        
        # Perform K-means clustering
        kmeans = KMeans(n_clusters=min(3, len(normalized_data)), random_state=42)
        clusters = kmeans.fit_predict(normalized_data)
        
        return {
            'n_clusters': kmeans.n_clusters,
            'cluster_centers': kmeans.cluster_centers_.tolist(),
            'cluster_labels': clusters.tolist(),
            'inertia': kmeans.inertia_
        }
    
    def _find_high_correlations(self, corr_matrix, threshold=0.7):
        """Find high correlations in correlation matrix."""
        high_corr = []
        for i in range(len(corr_matrix.columns)):
            for j in range(i+1, len(corr_matrix.columns)):
                corr_value = corr_matrix.iloc[i, j]
                if abs(corr_value) > threshold:
                    high_corr.append({
                        'var1': corr_matrix.columns[i],
                        'var2': corr_matrix.columns[j],
                        'correlation': corr_value
                    })
        return high_corr
    
    def _create_descriptive_charts(self, df):
        """Create descriptive analysis charts."""
        charts = []
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        
        for col in numeric_cols[:5]:  # Limit to 5 charts
            # Histogram
            fig = px.histogram(df, x=col, title=f'Distribution of {col}')
            charts.append({
                'type': 'histogram',
                'data': fig.to_dict(),
                'title': f'Distribution of {col}'
            })
        
        return charts
    
    def _create_correlation_charts(self, df):
        """Create correlation analysis charts."""
        numeric_df = df.select_dtypes(include=[np.number])
        
        if numeric_df.shape[1] < 2:
            return []
        
        # Correlation heatmap
        corr_matrix = numeric_df.corr()
        fig = px.imshow(
            corr_matrix,
            title='Correlation Heatmap',
            color_continuous_scale='RdBu'
        )
        
        return [{
            'type': 'heatmap',
            'data': fig.to_dict(),
            'title': 'Correlation Heatmap'
        }]
    
    def _create_trend_charts(self, df):
        """Create trend analysis charts."""
        charts = []
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        
        for col in numeric_cols[:3]:  # Limit to 3 charts
            fig = px.line(df, y=col, title=f'Trend of {col}')
            charts.append({
                'type': 'line',
                'data': fig.to_dict(),
                'title': f'Trend of {col}'
            })
        
        return charts
    
    def _create_clustering_charts(self, df):
        """Create clustering analysis charts."""
        numeric_df = df.select_dtypes(include=[np.number])
        
        if numeric_df.shape[1] < 2:
            return []
        
        # Use PCA for visualization if more than 2 dimensions
        if numeric_df.shape[1] > 2:
            pca = PCA(n_components=2)
            pca_data = pca.fit_transform(numeric_df)
            x_col, y_col = 'PC1', 'PC2'
            plot_data = pd.DataFrame(pca_data, columns=[x_col, y_col])
        else:
            plot_data = numeric_df
            x_col, y_col = numeric_df.columns[0], numeric_df.columns[1]
        
        # Add cluster labels if available
        if hasattr(self, '_clustering_results'):
            plot_data['cluster'] = self._clustering_results['cluster_labels']
            fig = px.scatter(
                plot_data, x=x_col, y=y_col, color='cluster',
                title='Clustering Results'
            )
        else:
            fig = px.scatter(
                plot_data, x=x_col, y=y_col,
                title='Data Points'
            )
        
        return [{
            'type': 'scatter',
            'data': fig.to_dict(),
            'title': 'Clustering Results'
        }]
    
    def _generate_insights(self, results, analysis_type):
        """Generate insights from analysis results."""
        insights = []
        
        if analysis_type == 'descriptive':
            if 'numeric_summary' in results:
                for col, stats in results['numeric_summary']['mean'].items():
                    insights.append(f"Average {col}: {stats:.2f}")
        
        elif analysis_type == 'correlation':
            if 'high_correlations' in results:
                for corr in results['high_correlations'][:3]:
                    insights.append(
                        f"Strong correlation ({corr['correlation']:.2f}) between "
                        f"{corr['var1']} and {corr['var2']}"
                    )
        
        elif analysis_type == 'trend':
            if 'trends' in results:
                for col, trend in results['trends'].items():
                    insights.append(
                        f"{col} shows a {trend['trend']} trend "
                        f"(slope: {trend['slope']:.3f})"
                    )
        
        elif analysis_type == 'clustering':
            if 'n_clusters' in results:
                insights.append(f"Data grouped into {results['n_clusters']} clusters")
                insights.append(f"Clustering quality (inertia): {results['inertia']:.2f}")
        
        return insights


class AIServiceManager:
    """Manager class for all AI services."""
    
    def __init__(self):
        self.sentiment_service = SentimentAnalysisService()
        self.text_gen_service = TextGenerationService()
        self.data_analysis_service = DataAnalysisService()
    
    def get_available_services(self):
        """Get list of available AI services."""
        return AIService.objects.filter(is_active=True)
    
    def get_service_usage_stats(self, user=None, days=30):
        """Get usage statistics for AI services."""
        from datetime import timedelta
        
        end_date = timezone.now().date()
        start_date = end_date - timedelta(days=days)
        
        usage_stats = AIUsage.objects.filter(
            date__range=[start_date, end_date]
        )
        
        if user:
            usage_stats = usage_stats.filter(user=user)
        
        return usage_stats
    
    def get_recent_requests(self, user=None, limit=10):
        """Get recent AI requests."""
        requests = AIRequest.objects.all()
        
        if user:
            requests = requests.filter(user=user)
        
        return requests[:limit] 