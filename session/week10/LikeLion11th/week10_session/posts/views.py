from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404, HttpResponse, JsonResponse
from django.views.generic import ListView

from .forms import PostBasedForm, PostCreateForm, PostUpdateForm, PostDetailForm
from .models import Post
from .serializers import PostModelSerializer, PostListSerializer, CommentListModelSerializer

from django.contrib.auth.decorators import login_required

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import api_view, action
from rest_framework import generics, status

# 게시글 목록 + 생성
class PostListCreateView(generics.ListAPIView, generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def create(self, request, *args, **kwars):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # self.perform_create(serializer)
        # 작성자 (로그인 성공했을 때 생성자 저장)
        if request.user.is_authenticated:
            serializer.save(writer=request.user)
        else: # 생성자 없이 저장
            serializer.save()

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)        


# 게시글 상세 + 수정 + 삭제
class PostRetrieveUpdateView(generics.RetrieveAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer

# # 게시글 수정
# class PostUpdateView(generics.UpdateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostListSerializer

class PostListViewSet(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer

# ViewSet
class PostModelViewSet(ModelViewSet):
    queryset=Post.objects.all()
    # serializer_class = PostModelSerializer
    serializer_class = PostListSerializer

    @action(detail=True, methods=['get'])
    def get_comment_all(self, request, pk = None):
        post = self.get_object()
        comment_all = post.comment_set.all()
        serializer = CommentListModelSerializer(comment_all, many=True)
        return Response(serializer.data)

@api_view()
def calculator(request):
    num1=request.GET.get('num1', 0)
    num2=request.GET.get('num2', 0)
    operators=request.GET.get('operators')

    if operators=='^': # +는 url 규정상 안됨
        result=int(num1)+int(num2)
    elif operators=='-':
        result=int(num1)-int(num2)
    elif operators=='*':
        result=int(num1)*int(num2)
    elif operators=='/':
        result=int(num1)/int(num2)
    else:
        result=0

    data={
        'type':'FBW',
        'result':result
    }

    return Response(data)


# 11주차 세션
def index(request):
    post_list = Post.objects.all().order_by('-created_at') # Post 모델에 있는 객체 전부 불러오기
    context = {
        'post_list' : post_list,
    }
    return render(request, 'index.html', context)

def post_list_view(request):
    post_list = Post.objects.all() # Post 모델에 있는 객체 전부 불러오기
    # post_list = Post.objects.filter(writer=request.user) # Post.writer가 현재 로그인 사용자인 데이터 조회
    context = { # Post 객체를 리스트 형태로 담기
        'post_list':post_list,
    }
    return render(request, 'posts/post_list.html', context)

def post_detail_view(request, id):
    try:
        post = Post.objects.get(id=id)
    except Post.DoesNotExist: # 존재하지 않는 게시글을 조회할 경우
        return redirect('index') # index.html로 redirect
    post = Post.objects.get(id=id)
    context = {
        'post' : post,
        'form' : PostDetailForm(),
    }
    return render(request, 'posts/post_detail.html', context)

@login_required
def post_create_view(request):
    if request.method == 'GET':
        return render(request, 'posts/post_form.html')
    else:
        image = request.FILES.get('image')
        content = request.POST.get('content')
        Post.objects.create( # image, content 데이터를 담은 Post 객체 만들어서 저장
            image = image,
            content = content,
            writer = request.user
        )
        return redirect('index')

def post_create_form_view(request):
    if request.method=="GET":
        form = PostCreateForm()
        context = {'form' : form}
        return render(request, 'posts/post_form2.html', context)
    else:
        form = PostCreateForm(request.POST, request.FILES)

        if form.is_valid():
            Post.objects.create( #image, content 데이터를 담은 Post 객체 만들어서 저장
            image=form.cleaned_data['image'], # 유효성 검사
            content=form.cleaned_data['content'],
            writer=request.user
            )
        else: # 잘못들어오면 화면이 움직이지 않음
            return redirect('post:post-create')
        return redirect('index')

@login_required
def post_update_view(request, id):

    # post = Post.objects.get(id=id) # 데이터 조회
    post = get_object_or_404(Post, id=id, writer=request.user) # id가 없을 경우 Page not found

    if request.method == "GET":
        context = { 'post' : post }
        return render(request, 'posts/post_form.html', context)
    elif request.method == "POST":
        new_image = request.FILES.get('image')
        content = request.POST.get('content')
        if new_image:
            post.image.delete()
            post.image = new_image
        post.content = content
        post.save()
        return redirect('posts:post-detail', post.id)

@login_required
def post_delete_view(request, id):
    post = get_object_or_404(Post, id=id)
    #post = get_object_or_404(Post,id=id, writer=request.user) # 데이터 조회
    if request.user != post.writer: # 사용자 확인
        raise Http404("잘못된 접근입니다.")
    
    if request.method == "GET": # 데이터 조회해서 넘겨줌
        context = { 'post' : post }
        return render(request, 'posts/post_confirm_delete.html', context)
    else:
        post.delete()
        return redirect('index') # 삭제를 했으므로 다시 index로
    

class class_view(ListView):
    model = Post
    template_name = 'cbv_view.html'

def url_view(request):
    data = {'code': '001', 'msg': 'OK'}
    return HttpResponse('<h1>url_views</h1>')

def url_parameter_view(request, username):
    print(f'url_parameter_view()')
    print(f'username: {username}')
    print(f'request.GET: {request.GET}')
    return HttpResponse(username)

def function_view(request):
    print(f'request.method: {request.method}')

    if request.method == "GET":
        print(f'request.GET: {request.GET}')
    elif request.method == 'POST':
        print(f'request.POST: {request.POST}')
    return render(request, 'view.html')