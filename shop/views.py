from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.viewsets import ModelViewSet
from shop.models import Product
from .filters import ProductFilter
from .serializers import ProductSerializer


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


