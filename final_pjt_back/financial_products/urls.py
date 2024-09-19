# financial_products.urls
from django.urls import path
from . import views

urlpatterns = [
    # 추천 알고리즘
    path('recommend_age/', views.recommend_age),
    path('recommend_money/', views.recommend_money),
    path('recommend_salary/', views.recommend_salary),
    # 예금
    path('save_deposits/', views.save_deposits),
    path('get_deposits/', views.deposit_list),
    path('get_deposits_options/', views.deposit_option_list),
    # 적금
    path('save_savings/', views.save_savings),
    path('get_savings/', views.saving_list),
    path('get_savings_options/', views.saving_option_list),

    path('get_product_detail/<str:fin_prdt_cd>/', views.get_product_detail),
    path('put_product/', views.put_product),
]