from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from posts.views import url_view, url_parameter_view, function_view, index
from posts.views import class_view

from rest_framework import routers
from posts.views import *

router=routers.DefaultRouter()
router.register('posts', PostModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('calculator/', calculator, name='calculator'),
    # Function Based View
    path('url/', url_view),
    path('url/<str:username>/', url_parameter_view),
    path('fbv/', function_view),
    # Class Based View
    path('cbv/', class_view.as_view()), # as_view: 진입 메소드

    #path('', index, name='index'),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    # path('posts/', include('posts.urls', namespace='posts')),
    
    # # 게시물 목록 + 생성
    # path('posts/', PostListCreateView.as_view(), name='post-list-create'),
    # # 게시물 상세 + 수정 + 삭제
    # path('posts/<int:pk>/', PostRetrieveUpdateView.as_view(), name='post-detail'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)