from django.contrib import admin
from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_featured', 'is_published', 'updated_at')
    list_filter = ('is_featured', 'is_published')
    search_fields = ('title', 'summary', 'body', 'tech_stack')
    prepopulated_fields = {'slug': ('title',)}
