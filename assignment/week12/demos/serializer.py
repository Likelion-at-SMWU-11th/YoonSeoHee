from .models import Blog
from rest_framework import serializers

class BlogModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fiels = ['title', 'content']