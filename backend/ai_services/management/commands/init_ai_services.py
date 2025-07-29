from django.core.management.base import BaseCommand
from ai_services.models import AIService


class Command(BaseCommand):
    help = 'Initialize AI services with default data'

    def handle(self, *args, **options):
        self.stdout.write('Initializing AI services...')
        
        # Create default AI services
        services_data = [
            {
                'name': 'Sentiment Analysis',
                'service_type': 'sentiment',
                'description': 'Analyze text sentiment using advanced NLP techniques and machine learning models.'
            },
            {
                'name': 'Text Generation',
                'service_type': 'text_gen',
                'description': 'Generate creative and contextual text using state-of-the-art language models.'
            },
            {
                'name': 'Data Analysis',
                'service_type': 'data_analysis',
                'description': 'Comprehensive data analysis with automated insights and visualizations.'
            },
            {
                'name': 'Image Generation',
                'service_type': 'image_gen',
                'description': 'Generate images from text descriptions using AI models.'
            },
            {
                'name': 'Code Generation',
                'service_type': 'code_gen',
                'description': 'Generate code snippets and functions based on natural language descriptions.'
            },
            {
                'name': 'Translation',
                'service_type': 'translation',
                'description': 'Translate text between multiple languages using neural machine translation.'
            }
        ]
        
        created_count = 0
        for service_data in services_data:
            service, created = AIService.objects.get_or_create(
                name=service_data['name'],
                defaults=service_data
            )
            if created:
                created_count += 1
                self.stdout.write(f'Created service: {service.name}')
            else:
                self.stdout.write(f'Service already exists: {service.name}')
        
        self.stdout.write(
            self.style.SUCCESS(f'Successfully initialized {created_count} AI services!')
        ) 