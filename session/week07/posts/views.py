from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from django.views.generic import ListView
from .models import Post

def index(request):
    return render(request, 'index.html')

def post_list_view(request):
    return render(request, 'posts/post_list.html')

def post_detail_view(request, id):
    return render(request, 'posts/post_detail.html')

def post_create_view(request):
    return render(request, 'posts/post_form.html')

def post_update_view(request, id):
    return render(request, 'posts/post_update.html')

def post_delete_view(request, id):
    return render(request, 'posts/post_confirm_delete.html')

class class_view(ListView): # CBV
    model = Post
    template_name = 'cbv_view.html'

# Create your views here.
def url_view(request): # FBV
    data = {'code' : '001', 'msg' : 'OK'}
    return HttpResponse('<h1>url_views</h1>')

def url_parameter_view(request, username):
    print('url_paramter_view()')
    print(f'username: {username}')
    print(f'request.GET: {request.GET}') # Query parameter
    return HttpResponse(username) #username 응답

def function_view(request):
    print(f'request.method: {request.method}')
    if request.method == "GET":
        print(f'request.GET: {request.GET}')
    if request.method == "POST": 
        print(f'request.POST: {request.POST}')
    return render(request, 'view.html')

""" def url_view(request):
    return HttpResponse('url.view') """