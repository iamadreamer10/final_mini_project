from django.urls import path
from . import views

urlpatterns = [
    # 게시글 목록 조회 / 생성
    path('', views.article_list),
    # 게시글 조회 / 수정 / 삭제
    path('<int:article_pk>/', views.article_detail),

]
