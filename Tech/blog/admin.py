from django.contrib import admin
from .models import BlogPost


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'status', 'created_at', 'updated_at')
    list_filter = ('status', 'created_at', 'author')
    search_fields = ('title', 'content')
    readonly_fields = ('created_at', 'updated_at')

    # Auto-set author when admin creates a post
    def save_model(self, request, obj, form, change):
        if not obj.author:  # assign only when creating a new post
            obj.author = request.user
        super().save_model(request, obj, form, change)
