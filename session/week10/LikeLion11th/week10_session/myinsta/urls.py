from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include, re_path

from posts.views import url_view, url_parameter_view, function_view, index
from posts.views import class_view
from posts.views import *

from rest_framework import routers
from rest_framework import permissions
from accounts_token.views import login_view

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License",)
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router=routers.DefaultRouter()
router.register('posts', PostModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),

    # # 게시물 목록 + 생성
    # path('posts/', PostListCreateView.as_view(), name='post-list-create'),
    
    # # 게시물 상세 + 수정 + 삭제
    # path('posts/<int:pk>/', PostRetrieveUpdateView.as_view(), name='post-detail'),
   
    # 토큰 인증 로그인 구현
    path('login/', login_view),

    # swagger
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

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
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)