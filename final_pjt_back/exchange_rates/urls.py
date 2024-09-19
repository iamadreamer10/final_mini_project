# financial_products.urls
from django.urls import path
from . import views

urlpatterns = [
    path('', views.exchange_rates),
]