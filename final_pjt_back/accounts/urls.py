from django.urls import path
from . import views

urlpatterns = [
    # 특정 사용자의 프로필 페이지
    # path('users/', views.users_list),
    path('profile/', views.profile),
    path('<int:user_id>/', views.get_user_info),
]