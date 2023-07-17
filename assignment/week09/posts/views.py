from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

# Function Based View
def function_view(request):
    print(f'request.method: {request.method}')
    if request.method == "GET":
        print(f'request.GET: {request.GET}')
    if request.method == "POST":
        print(f'request.POST: {request.POST}')
    return render(request, 'aboutme.html')

# Class Based View
class class_view(ListView):
    model = Post
    template_name = 'diary.html'