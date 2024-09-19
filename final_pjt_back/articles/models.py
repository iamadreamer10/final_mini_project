# articles/models.py
from django.db import models
from django.conf import settings
from financial_products.models import DepositProducts, SavingProducts

class Article(models.Model):
    # 참조 대상1 : Custom User Model
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # 참조 대상2 : Financial_Product Model
    deposit = models.ForeignKey(DepositProducts, to_field='fin_prdt_cd', on_delete=models.CASCADE, null=True)
    saving = models.ForeignKey(SavingProducts, to_field='fin_prdt_cd', on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
