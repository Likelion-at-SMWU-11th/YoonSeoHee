from rest_framework.serializers import ModelSerializer
from .models import Post, Comment

class PostModelSerializer(ModelSerializer):
    class Meta:
        model=Post
        fields='__all__'
        #fields=['id', 'writer', 'content']

# 리스트 형태로 보여줌
class PostListSerializer(PostModelSerializer): # 위 클래스를 상속받음
    class Meta(PostModelSerializer.Meta):
        fields = [ 'id',
                  'image',
                  'content',
                  'created_at',
                  'writer',
        ]

        depth=1 # 필드 모든 속성이 나옴 -> 댓글 기능 구현할 때 개발하기 수월

class PostRetrieveSerializer(PostModelSerializer):
    class Meta(PostModelSerializer.Meta):
        depth=1


# 게시판 생성
class PostCreateSerializer(PostModelSerializer):
    class Meta(PostModelSerializer.Meta):
        fields = [
            'image',
            'content',
        ]

class CommentListModelSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'