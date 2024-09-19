from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
# 자체 유저 모델 제작을 어떻게 해야 할까?

# 커스텀 유저 모델 설정
# JSON 데이터 형식과 맞추기 위해 다음과 같이 설정
class User(AbstractUser):
    # 이미 AbstractUser에 존재하는 디폴트 필드는 제외
    # username = models.CharField(max_length=30, unique=True)
    nickname = models.CharField(max_length=255, blank=True, null=True)
    # 당장 필요한 필드가 아니라서 일단 보류
    # email = models.EmailField(max_length=254, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    money = models.IntegerField(blank=True, null=True)
    salary = models.IntegerField(blank=True, null=True)
    # 리스트 데이터 저장을 위해 Text 형태로 저장
    financial_products = models.TextField(blank=True, null=True)
    
    # superuser fields
    # is_active = models.BooleanField(default=True)
    # is_staff = models.BooleanField(default=False)
    # is_superuser = models.BooleanField(default=False)
    USERNAME_FIELD = 'username'


# Adapter 커스터마이징
from allauth.account.adapter import DefaultAccountAdapter

# 얻은 정보들을 바탕으로 유저객체를 생성하여 저장하는 클래스
class CustomAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
        """
        Saves a new `User` instance using information provided in the
        signup form.
        """
        from allauth.account.utils import user_email, user_field, user_username
        data = form.cleaned_data
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        # email = data.get("email")
        username = data.get("username")
        nickname = data.get("nickname")
        age = data.get("age")
        money = data.get("money")
        salary = data.get("salary")
        financial_product = data.get("financial_products")

        # user_email(user, email)
        user_username(user, username)
        if first_name:
            user_field(user, "first_name", first_name)
        if last_name:
            user_field(user, "last_name", last_name)
        if nickname:
            user_field(user, "nickname", nickname)
        if age:
            user.age = age
        if money:
            user.money = money
        if salary:
            user.salary = salary
        if financial_product:
            financial_products = user.financial_products.split(',')
            financial_products.append(financial_product)
            if len(financial_products) > 1:
                financial_products = ','.join(financial_products)
            user_field(user, "financial_products", financial_products)
        if "password1" in data:
            user.set_password(data["password1"])
        else:
            user.set_unusable_password()
        self.populate_username(request, user)
        if commit:
            # Ability not to commit makes it easier to derive from this adapter by adding
            user.save()
        return user

