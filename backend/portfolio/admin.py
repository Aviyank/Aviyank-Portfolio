from django.contrib import admin
from django.utils.html import format_html
from .models import Profile, Skill, Project, Experience, Education, Contact, BlogPost, ResearchProject


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'location', 'email', 'created_at']
    list_filter = ['created_at', 'updated_at']
    search_fields = ['user__username', 'title', 'bio', 'location']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'proficiency', 'icon', 'created_at']
    list_filter = ['category', 'proficiency', 'created_at']
    search_fields = ['name', 'description']
    ordering = ['category', '-proficiency']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'featured', 'technologies_display', 'created_at']
    list_filter = ['status', 'featured', 'technologies', 'created_at']
    search_fields = ['title', 'description', 'short_description']
    filter_horizontal = ['technologies']
    readonly_fields = ['created_at', 'updated_at']
    
    def technologies_display(self, obj):
        return ", ".join([tech.name for tech in obj.technologies.all()[:3]])
    technologies_display.short_description = 'Technologies'


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['title', 'company', 'location', 'start_date', 'end_date', 'current']
    list_filter = ['current', 'start_date', 'end_date', 'technologies_used']
    search_fields = ['title', 'company', 'description']
    filter_horizontal = ['technologies_used']
    readonly_fields = ['created_at']


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['degree', 'institution', 'location', 'start_date', 'end_date', 'current', 'gpa']
    list_filter = ['current', 'start_date', 'end_date']
    search_fields = ['degree', 'institution', 'description']
    readonly_fields = ['created_at']


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'created_at', 'read']
    list_filter = ['read', 'created_at']
    search_fields = ['name', 'email', 'subject', 'message']
    readonly_fields = ['created_at']
    actions = ['mark_as_read', 'mark_as_unread']
    
    def mark_as_read(self, request, queryset):
        queryset.update(read=True)
    mark_as_read.short_description = "Mark selected messages as read"
    
    def mark_as_unread(self, request, queryset):
        queryset.update(read=False)
    mark_as_unread.short_description = "Mark selected messages as unread"


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'published', 'published_at', 'created_at']
    list_filter = ['published', 'published_at', 'created_at', 'tags']
    search_fields = ['title', 'content', 'excerpt']
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ['tags']
    readonly_fields = ['created_at', 'updated_at']
    actions = ['publish_posts', 'unpublish_posts']
    
    def publish_posts(self, request, queryset):
        queryset.update(published=True)
    publish_posts.short_description = "Publish selected blog posts"
    
    def unpublish_posts(self, request, queryset):
        queryset.update(published=False)
    unpublish_posts.short_description = "Unpublish selected blog posts" 

admin.site.register(ResearchProject) 