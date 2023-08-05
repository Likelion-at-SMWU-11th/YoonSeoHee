from django.db import models

class Blog(models.Model):
    title = models.CharField(verbose_name='제목', max_length=30) # 최대 길이 명시
    content = models.TextField(verbose_name='내용')
    created_at = models.DateTimeField(verbose_name='작성일', auto_now_add=True)