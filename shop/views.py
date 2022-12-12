from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.viewsets import ModelViewSet
from .serializers import ProductSerializer, OrderSerializer, ReviewSerializer, \
    ProductCollectionSerializer
from django_filters import rest_framework as filters
from .models import Product, Order, Item, Review, ProductCollection, OrderStatusChoices


class ProductFilter(filters.FilterSet):
    """Фильтры для товаров."""

    price_from = filters.NumberFilter(field_name='price', lookup_expr="gte")
    price_to = filters.NumberFilter(field_name='price', lookup_expr="lte")
    name = filters.CharFilter(lookup_expr='icontains')
    description = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Product
        fields = ('name', 'description', 'price_from', 'price_to',)


class OrderFilter(filters.FilterSet):
    """Фильтры для заказов."""

    status = filters.ChoiceFilter(choices=OrderStatusChoices.choices)
    price_from = filters.NumberFilter(field_name='total_price', lookup_expr="gte")
    price_to = filters.NumberFilter(field_name='total_price', lookup_expr="lte")
    products = filters.CharFilter()
    created_at = filters.DateFromToRangeFilter()
    updated_at = filters.DateFromToRangeFilter()

    class Meta:
        model = Order
        fields = ('status', 'price_from', 'price_to', 'products', 'created_at', 'updated_at',)


class ReviewFilter(filters.FilterSet):
    """Фильтры для отзывов."""

    creator = filters.NumberFilter()
    product = filters.NumberFilter()
    created_at = filters.DateFromToRangeFilter()

    class Meta:
        model = Review
        fields = ('creator', 'product', 'created_at',)


class IsOwnerOrAdmin(permissions.BasePermission):
    """Класс разрешений для владельца объекта"""

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True
        return obj.creator == request.user


class ProductViewSet(ModelViewSet):
    """ViewSet для товара."""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filterset_class = ProductFilter

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [IsAdminUser()]
        if self.action in ["list", "retrieve"]:
            return [AllowAny()]
        return []


class OrderViewSet(ModelViewSet):
    """ViewSet для заказа"""
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filterset_class = OrderFilter

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create"]:
            return [IsAuthenticated()]
        if self.action in ["list"]:
            return [IsAdminUser()]
        if self.action in ["retrieve", "update", "partial_update", "destroy"]:
            return [IsOwnerOrAdmin()]
        return []


class ReviweViewSet(ModelViewSet):
    """ViewSet для отзывов."""
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    filterset_class = ReviewFilter

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create"]:
            return [IsAuthenticated()]
        if self.action in ["update", "partial_update", "destroy"]:
            return [IsOwnerOrAdmin()]
        return []


class ProductCollectionViewSet(ModelViewSet):
    """ViewSet для подборок"""
    queryset = ProductCollection.objects.all()
    serializer_class = ProductCollectionSerializer

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [IsAdminUser()]
        if self.action in ["list", "retrieve"]:
            return [AllowAny()]
        return []
