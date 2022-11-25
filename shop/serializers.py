from rest_framework import serializers
from .models import Product, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        ordering = ('name',)
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        index_together = (('id', 'slug'),)
