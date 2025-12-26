from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_published', 'published_at')
    list_filter = ('is_published',)
    search_fields = ('title', 'excerpt', 'body')
    prepopulated_fields = {'slug': ('title',)}

    fieldsets = (
        (None, {'fields': ('title', 'slug', 'excerpt')}),
        ('Content', {'fields': ('body',)}),
        ('Publishing', {'fields': ('is_published', 'published_at')}),
    )
