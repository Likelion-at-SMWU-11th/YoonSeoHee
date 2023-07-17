from django.db import models

# Create your models here.
class Post(models.Model):
    image = models.ImageField(verbose_name='이미지')
    contentn = models.TextField('내용')
    created_at = models.DateTimeField('작성일', auto_now_add=True)
    view_count = models.IntegerField('조회수', default=0)
    writer = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name='작성자', null=True, blank=True)