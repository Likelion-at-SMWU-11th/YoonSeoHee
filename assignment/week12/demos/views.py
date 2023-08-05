from rest_framework import viewsets
from .serializer import BlogSerializer
from .models import Blog

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer