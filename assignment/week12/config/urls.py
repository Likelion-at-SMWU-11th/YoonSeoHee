"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from demos.views import *

router = routers.DefaultRouter()
router.register('demos', PostViewSet, basename='demos')

# post list : GET, POST method
post_list = PostViewSet.as_view({
    'get' : 'list',
    'post' : 'create'
})

# post detail : GET, PUT, DELETE method
post_detail = PostViewSet.as_view({
    'get' : 'retrieve',
    'put' : 'update',
    'delete' : 'destroy'
})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('post/', post_list),
    path('post/<int:pk>', post_detail),
]
