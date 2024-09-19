from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import ArticleListSerializer, ArticleSerializer
from .models import Article


# 게시글 리스트 조회 / 게시글 생성
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def article_list(request):
    if request.method == 'GET':
        articles = get_list_or_404(Article)
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        # print(request.data)
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

# 단일 게시글 조회
# 수정 / 삭제는 vue에서 구현해야 하는가??
@api_view(['GET', 'DELETE', 'PUT'])
@permission_classes([IsAuthenticated])
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    # 단일 게시글 조회
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    # 단일 게시글 삭제
    elif request.method == 'DELETE':
        if request.user == article.user:
            article.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
    # 단일 게시글 수정
    elif request.method == 'PUT':
        print(request)
        if request.user == article.user:
            serializer = ArticleSerializer(article, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)

