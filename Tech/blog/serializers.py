from rest_framework import serializers
from .models import BlogPost

class BlogPostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.id')

    class Meta:
        model = BlogPost
        fields = "__all__"
        read_only_fields = ("author", "created_at", "updated_at")
