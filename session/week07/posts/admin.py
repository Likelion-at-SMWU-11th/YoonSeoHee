from django.contrib import admin
from .models import Post, Comment

class CommentInline(admin.TabularInline): #StackedInline 세로로
    model = Comment
    min_num = 3
    max_num = 5
    verbose_name = '댓글'
    verbose_name_plural = '댓글'

@admin.register(Post)
class PostModeAdmin(admin.ModelAdmin):
    list_display = ['id', 'image', 'contentn', 'created_at', 'view_count', 'writer']
    #list_editable = ['contentn', 'writer']
    list_filter = ['created_at',]
    search_fields = ['id', 'writer__username'] # FK이기 때문에 _ 두개
    search_help_text = '게시판번호, 작성자 검색이 가능합니다'
    inlines = [CommentInline,]
    
    actions = ['make_published']
    
    def make_published(modeladmin, request, queryset):
        for item in queryset:
            item.contentn = '운영규칙 위반으로 인한 게시글 삭제 처리'
            item.save()
admin.site.register(Comment) # 모델을 보기 위해 등록