from django.contrib.auth.models import User
from rest_framework import serializers

from shop.models import Product


class UseSerializer(serializers.ModelSerializer):
    """Serializer для пользователя."""

    class Meta:
        model = User
        fields = ('id', 'username',)


class ProductSerializer(serializers.ModelSerializer):
    """Serializer для товара."""

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'created_at', 'updated_at',)


