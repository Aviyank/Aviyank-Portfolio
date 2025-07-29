from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Contact, Project, BlogPost, Profile, Skill, Experience, Education


class ContactForm(forms.ModelForm):
    """Contact form."""
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Email'
            }),
            'subject': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Subject'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Your Message'
            }),
        }


class ProjectForm(forms.ModelForm):
    """Project form."""
    class Meta:
        model = Project
        fields = [
            'title', 'description', 'short_description', 'image',
            'github_url', 'live_url', 'technologies', 'status', 'featured'
        ]
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Project Title'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Project Description'
            }),
            'short_description': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Short Description (max 300 characters)'
            }),
            'github_url': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'GitHub Repository URL'
            }),
            'live_url': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'Live Demo URL'
            }),
            'technologies': forms.SelectMultiple(attrs={
                'class': 'form-control'
            }),
            'status': forms.Select(attrs={
                'class': 'form-control'
            }),
            'featured': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
        }


class BlogPostForm(forms.ModelForm):
    """Blog post form."""
    class Meta:
        model = BlogPost
        fields = [
            'title', 'slug', 'content', 'excerpt', 'image',
            'tags', 'published'
        ]
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Blog Post Title'
            }),
            'slug': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'URL Slug (e.g., my-blog-post)'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 10,
                'placeholder': 'Blog Post Content'
            }),
            'excerpt': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Brief excerpt (max 300 characters)'
            }),
            'tags': forms.SelectMultiple(attrs={
                'class': 'form-control'
            }),
            'published': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
        }


class ProfileForm(forms.ModelForm):
    """Profile form."""
    class Meta:
        model = Profile
        fields = [
            'title', 'bio', 'avatar', 'location', 'email', 'phone',
            'github_url', 'linkedin_url', 'twitter_url', 'website_url'
        ]
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Professional Title'
            }),
            'bio': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'About yourself'
            }),
            'location': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Location'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Email'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Phone Number'
            }),
            'github_url': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'GitHub Profile URL'
            }),
            'linkedin_url': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'LinkedIn Profile URL'
            }),
            'twitter_url': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'Twitter Profile URL'
            }),
            'website_url': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'Personal Website URL'
            }),
        }


class SkillForm(forms.ModelForm):
    """Skill form."""
    class Meta:
        model = Skill
        fields = ['name', 'category', 'proficiency', 'icon', 'description']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Skill Name'
            }),
            'category': forms.Select(attrs={
                'class': 'form-control'
            }),
            'proficiency': forms.Select(attrs={
                'class': 'form-control'
            }),
            'icon': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'FontAwesome Icon Class (e.g., fab fa-python)'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Skill Description'
            }),
        }


class ExperienceForm(forms.ModelForm):
    """Experience form."""
    class Meta:
        model = Experience
        fields = [
            'title', 'company', 'location', 'start_date', 'end_date',
            'current', 'description', 'technologies_used'
        ]
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Job Title'
            }),
            'company': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Company Name'
            }),
            'location': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Location'
            }),
            'start_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'end_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'current': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Job Description'
            }),
            'technologies_used': forms.SelectMultiple(attrs={
                'class': 'form-control'
            }),
        }


class EducationForm(forms.ModelForm):
    """Education form."""
    class Meta:
        model = Education
        fields = [
            'degree', 'institution', 'location', 'start_date', 'end_date',
            'current', 'description', 'gpa'
        ]
        widgets = {
            'degree': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Degree/Certification'
            }),
            'institution': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Institution Name'
            }),
            'location': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Location'
            }),
            'start_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'end_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'current': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Description'
            }),
            'gpa': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01',
                'min': '0',
                'max': '4',
                'placeholder': 'GPA (optional)'
            }),
        }


class UserRegistrationForm(UserCreationForm):
    """User registration form."""
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user 