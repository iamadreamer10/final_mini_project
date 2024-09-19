# final_pjt_back/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/articles/', include('articles.urls')),
    path('api/v1/accounts/', include('accounts.urls')),
    path('api/v1/exchange_rates/', include('exchange_rates.urls')),
    # path('accounts/', include('accounts.urls')),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),

    path('api/v1/financial_products/', include('financial_products.urls')),
]
