from django_filters import rest_framework as filters
from shop.models import Product

class ProductFilter(filters.FilterSet):
    """Фильтры для товаров."""

    price_from= filters.NumberFilter(field_name='price', lookup_expr="gte")
    price_to= filters.NumberFilter(field_name='price', lookup_expr="lte")
    name = filters.CharFilter(lookup_expr='icontains')
    description = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Product
        fields = ('name', 'description', 'price_from', 'price_to',)
