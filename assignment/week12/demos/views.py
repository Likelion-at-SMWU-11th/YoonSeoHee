from rest_framework import viewsets
from rest_framework.decorators import api_view
from .serializer import PostSerializer
from .models import Post

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer