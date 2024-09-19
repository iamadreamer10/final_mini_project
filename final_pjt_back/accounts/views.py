from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from django.conf import settings
from django.shortcuts import get_object_or_404, get_list_or_404
from django.contrib.auth import get_user_model
from dj_rest_auth.registration.serializers import RegisterSerializer
from .serializers import CustomRegisterSerializer

# from .serializers import ArticleListSerializer, ArticleSerializer
# from .models import Article

# 유저 리스트 반환
# def users_list(request):
#     # if request.method == 'GET':
#     users = get_list_or_404(settings.AUTH_USER_MODEL)
#     serializer = CustomRegisterSerializer(users, many=True)
#     return Response(serializer.data)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def profile(request):
    # print(request.user.user_id)
    user = get_object_or_404(get_user_model(), username=request.user.username)
    # print(user)
    if request.method == 'GET':
        serializer = CustomRegisterSerializer(user)
        # print(serializer.data)
        return Response(serializer.data)
    
@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def get_user_info(request, user_id):
    user = get_object_or_404(get_user_model(), id=user_id)

    if request.method == 'GET':
        serializer = CustomRegisterSerializer(user)
        return Response(serializer.data)