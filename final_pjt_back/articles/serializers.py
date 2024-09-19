# articles/serializers.py
from rest_framework import serializers
from .models import Article
from accounts.models import User


class ArticleListSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('username',)
        
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = Article
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('user', )
