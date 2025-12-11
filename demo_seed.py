from django.contrib.auth.models import User
from portfolio.models import Profile, Skill, Project, BlogPost, Contact
from django.utils.text import slugify

# Get or create user
user, _ = User.objects.get_or_create(username='aviyank', defaults={'email': 'aviyank123@gmail.com'})

# Profile
profile, _ = Profile.objects.get_or_create(
    user=user,
    defaults={
        'title': 'AI/ML Engineer',
        'bio': 'Passionate about AI, ML, and web development.',
        'location': 'New York',
        'email': 'aviyank123@gmail.com',
        'github_url': 'https://github.com/aviyank',
        'linkedin_url': 'https://linkedin.com/in/aviyank',
        'twitter_url': 'https://twitter.com/aviyank',
    }
)

# Skills
skill1, _ = Skill.objects.get_or_create(name='Python', category='programming', proficiency=9, icon='fab fa-python')
skill2, _ = Skill.objects.get_or_create(name='Django', category='framework', proficiency=8, icon='fab fa-python')
skill3, _ = Skill.objects.get_or_create(name='PostgreSQL', category='database', proficiency=7, icon='fas fa-database')
skill4, _ = Skill.objects.get_or_create(name='AWS', category='cloud', proficiency=6, icon='fab fa-aws')
skill5, _ = Skill.objects.get_or_create(name='TensorFlow', category='ai_ml', proficiency=7, icon='fas fa-brain')

# Project
project, _ = Project.objects.get_or_create(
    title='AI Portfolio Website',
    defaults={
        'description': 'A portfolio site with AI-powered features.',
        'short_description': 'Portfolio with AI features.',
        'status': 'completed',
        'featured': True,
    }
)
project.technologies.set([skill1, skill2, skill3, skill4, skill5])
project.save()

# BlogPost
blog, _ = BlogPost.objects.get_or_create(
    title='Welcome to My AI Portfolio',
    slug=slugify('Welcome to My AI Portfolio'),
    defaults={
        'content': 'This is my first blog post about building an AI-powered portfolio.',
        'excerpt': 'Building an AI-powered portfolio.',
        'author': user,
        'published': True,
    }
)
blog.tags.set([skill1, skill2, skill5])
blog.save()

# Contact
Contact.objects.get_or_create(
    name='John Doe',
    email='john@example.com',
    subject='Hello',
    message='Just wanted to say hi!'
)

print('Demo content created.') 