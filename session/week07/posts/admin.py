from django.contrib import admin
from .models import Post
from .models import Comment

admin.site.register(Post)
admin.site.register(Comment) # 모델을 보기 위해 등록