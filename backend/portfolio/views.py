from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.db.models import Q
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from itertools import groupby
from operator import attrgetter
import feedparser
from datetime import datetime
import requests

from .models import Profile, Skill, Project, Experience, Education, Contact, BlogPost, ResearchProject
from .forms import ContactForm, ProjectForm, BlogPostForm


def home(request):
    """Home page view."""
    profile = Profile.objects.first()
    featured_projects = Project.objects.filter(featured=True)[:3]
    recent_projects = Project.objects.filter(status='completed')[:6]
    research_projects = ResearchProject.objects.all()[:3]
    skills = Skill.objects.all()
    # Group skills by category
    skills = sorted(skills, key=attrgetter('category'))
    grouped_skills = {}
    for category, items in groupby(skills, key=attrgetter('category')):
        grouped_skills[category] = list(items)
    import os
    avatars_dir = os.path.join('backend', 'media', 'avatars')
    try:
        media_avatars = os.listdir(avatars_dir)
    except Exception:
        media_avatars = []
    context = {
        'profile': profile,
        'featured_projects': featured_projects,
        'recent_projects': recent_projects,
        'research_projects': research_projects,
        'skills': skills,
        'grouped_skills': grouped_skills,
        'media_avatars': media_avatars,
    }
    return render(request, 'portfolio/home.html', context)


def about(request):
    """About page view."""
    profile = Profile.objects.first()
    experiences = Experience.objects.all()
    education = Education.objects.all()
    skills = Skill.objects.all()
    
    context = {
        'profile': profile,
        'experiences': experiences,
        'education': education,
        'skills': skills,
    }
    return render(request, 'portfolio/about.html', context)


class ProjectListView(ListView):
    """Project list view."""
    model = Project
    template_name = 'portfolio/projects.html'
    context_object_name = 'projects'
    paginate_by = 9
    
    def get_queryset(self):
        queryset = Project.objects.all()
        search = self.request.GET.get('search')
        category = self.request.GET.get('category')
        status = self.request.GET.get('status')
        
        if search:
            queryset = queryset.filter(
                Q(title__icontains=search) |
                Q(description__icontains=search) |
                Q(technologies__name__icontains=search)
            ).distinct()
        
        if category:
            queryset = queryset.filter(technologies__category=category)
        
        if status:
            queryset = queryset.filter(status=status)
        
        return queryset

    def get_github_projects(self, limit=6):
        url = 'https://api.github.com/users/Aviyank/repos'
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            repos = response.json()
        except Exception:
            repos = []
        projects = []
        for repo in repos[:limit]:
            projects.append({
                'title': repo['name'],
                'description': repo['description'] or '',
                'url': repo['html_url'],
                'language': repo.get('language', ''),
                'stars': repo.get('stargazers_count', 0),
                'source': 'github',
                'created_at': repo.get('created_at', ''),
                'updated_at': repo.get('updated_at', ''),
            })
        return projects

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Local projects
        local_projects = list(self.get_queryset())
        local_projects_dicts = [{
            'title': p.title,
            'description': p.short_description or p.description,
            'url': p.live_url or p.github_url or '',
            'language': ', '.join([s.name for s in p.technologies.all()]),
            'stars': '',
            'source': 'local',
            'object': p,
            'created_at': p.created_at,
            'updated_at': p.updated_at,
        } for p in local_projects]
        # GitHub projects
        github_projects = self.get_github_projects()
        # Merge and sort (by updated date if available)
        def get_sort_key(proj):
            return proj.get('updated_at') or proj.get('created_at')
        all_projects = local_projects_dicts + github_projects
        all_projects_sorted = sorted(all_projects, key=get_sort_key, reverse=True)
        context['all_projects'] = all_projects_sorted
        # Add research projects
        context['research_projects'] = ResearchProject.objects.all()
        context['search'] = self.request.GET.get('search', '')
        context['category'] = self.request.GET.get('category', '')
        context['status'] = self.request.GET.get('status', '')
        context['skills'] = Skill.objects.all()
        return context


class ProjectDetailView(DetailView):
    """Project detail view."""
    model = Project
    template_name = 'portfolio/project_detail.html'
    context_object_name = 'project'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['related_projects'] = Project.objects.filter(
            technologies__in=self.object.technologies.all()
        ).exclude(id=self.object.id)[:3]
        return context


class BlogPostListView(ListView):
    """Blog post list view."""
    model = BlogPost
    template_name = 'portfolio/blog.html'
    context_object_name = 'posts'
    paginate_by = 6
    
    def get_queryset(self):
        return BlogPost.objects.filter(published=True)

    def get_medium_posts(self, limit=6):
        feed_url = 'https://medium.com/feed/@aviyank'
        feed = feedparser.parse(feed_url)
        posts = []
        for entry in feed.entries[:limit]:
            posts.append({
                'title': entry.title,
                'link': entry.link,
                'summary': entry.summary,
                'published': entry.published,
                'published_parsed': datetime(*entry.published_parsed[:6]),
                'author': entry.get('author', 'Medium'),
                'source': 'medium',
            })
        return posts

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Local posts
        local_posts = list(self.get_queryset())
        # Medium posts
        medium_posts = self.get_medium_posts()
        # Convert local posts to dicts for uniformity
        local_posts_dicts = [{
            'title': post.title,
            'link': post.get_absolute_url() if hasattr(post, 'get_absolute_url') else '',
            'summary': post.excerpt or post.content[:200],
            'published': post.published_at or post.created_at,
            'published_parsed': post.published_at or post.created_at,
            'author': post.author.get_full_name() if hasattr(post.author, 'get_full_name') else str(post.author),
            'source': 'local',
            'object': post,
        } for post in local_posts]
        # Merge and sort
        all_posts = local_posts_dicts + medium_posts
        all_posts_sorted = sorted(all_posts, key=lambda x: x['published_parsed'], reverse=True)
        context['all_posts'] = all_posts_sorted
        context['recent_posts'] = local_posts[:5]
        context['tags'] = Skill.objects.filter(blogpost__published=True).distinct()
        return context


class BlogPostDetailView(DetailView):
    """Blog post detail view."""
    model = BlogPost
    template_name = 'portfolio/blog_detail.html'
    context_object_name = 'post'
    
    def get_queryset(self):
        return BlogPost.objects.filter(published=True)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recent_posts'] = BlogPost.objects.filter(published=True).exclude(
            id=self.object.id
        )[:3]
        return context


def contact(request):
    """Contact page view."""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            messages.success(request, 'Thank you for your message! I will get back to you soon.')
            return redirect('contact')
    else:
        form = ContactForm()
    
    context = {
        'form': form,
    }
    return render(request, 'portfolio/contact.html', context)


@api_view(['POST'])
def contact_api(request):
    """API endpoint for contact form."""
    form = ContactForm(request.data)
    if form.is_valid():
        contact = form.save()
        return Response({
            'message': 'Message sent successfully!',
            'id': contact.id
        }, status=status.HTTP_201_CREATED)
    return Response({
        'errors': form.errors
    }, status=status.HTTP_400_BAD_REQUEST)


# Admin views (require login)
class ProjectCreateView(LoginRequiredMixin, CreateView):
    """Create new project."""
    model = Project
    form_class = ProjectForm
    template_name = 'portfolio/project_form.html'
    success_url = reverse_lazy('projects')
    
    def form_valid(self, form):
        messages.success(self.request, 'Project created successfully!')
        return super().form_valid(form)


class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    """Update existing project."""
    model = Project
    form_class = ProjectForm
    template_name = 'portfolio/project_form.html'
    success_url = reverse_lazy('projects')
    
    def form_valid(self, form):
        messages.success(self.request, 'Project updated successfully!')
        return super().form_valid(form)


class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    """Delete project."""
    model = Project
    success_url = reverse_lazy('projects')
    
    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Project deleted successfully!')
        return super().delete(request, *args, **kwargs)


class BlogPostCreateView(LoginRequiredMixin, CreateView):
    """Create new blog post."""
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'portfolio/blog_form.html'
    success_url = reverse_lazy('blog')
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, 'Blog post created successfully!')
        return super().form_valid(form)


class BlogPostUpdateView(LoginRequiredMixin, UpdateView):
    """Update existing blog post."""
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'portfolio/blog_form.html'
    success_url = reverse_lazy('blog')
    
    def form_valid(self, form):
        messages.success(self.request, 'Blog post updated successfully!')
        return super().form_valid(form)


class BlogPostDeleteView(LoginRequiredMixin, DeleteView):
    """Delete blog post."""
    model = BlogPost
    success_url = reverse_lazy('blog')
    
    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Blog post deleted successfully!')
        return super().delete(request, *args, **kwargs)


@login_required
def dashboard(request):
    """Admin dashboard."""
    total_projects = Project.objects.count()
    total_contacts = Contact.objects.count()
    unread_contacts = Contact.objects.filter(read=False).count()
    recent_contacts = Contact.objects.all()[:5]
    
    context = {
        'total_projects': total_projects,
        'total_contacts': total_contacts,
        'unread_contacts': unread_contacts,
        'recent_contacts': recent_contacts,
    }
    return render(request, 'portfolio/dashboard.html', context)


@api_view(['GET'])
def skills_api(request):
    """API endpoint for skills."""
    category = request.GET.get('category')
    if category:
        skills = Skill.objects.filter(category=category)
    else:
        skills = Skill.objects.all()
    
    data = [{
        'id': skill.id,
        'name': skill.name,
        'category': skill.category,
        'proficiency': skill.proficiency,
        'icon': skill.icon,
        'description': skill.description,
    } for skill in skills]
    
    return Response(data)


@api_view(['GET'])
def projects_api(request):
    """API endpoint for projects."""
    projects = Project.objects.all()
    data = [{
        'id': project.id,
        'title': project.title,
        'description': project.description,
        'short_description': project.short_description,
        'image': project.image.url if project.image else None,
        'github_url': project.github_url,
        'live_url': project.live_url,
        'status': project.status,
        'featured': project.featured,
        'technologies': [skill.name for skill in project.technologies.all()],
        'created_at': project.created_at,
    } for project in projects]
    
    return Response(data) 