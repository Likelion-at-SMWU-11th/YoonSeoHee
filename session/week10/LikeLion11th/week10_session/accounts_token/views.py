from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

@api_view(['POST'])
@permission_classes([AllowAny]) # 토큰없이 누구나 성공
def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request,
                        username = username,
                        password = password)
    
    if user: # 로그인 성공 시 토큰 반환
        token, _ = Token.objects.get_or_create(user=user)
        return Response ({'token' : token.key})
    else: # 로그인 실패시 401 에러 반환
        return Response(status=401)