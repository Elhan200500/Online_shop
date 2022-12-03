from django.contrib.auth.models import User
from rest_framework import serializers

from shop.models import Product, Order


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


class ItemSerializer(serializers.ModelSerializer):
    """Serializer для позиции."""

    product = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(),
        required=True)

    class Meta:
        model = Item
        fields = ('product', 'quantity',)


class OrderSerializer(serializers.ModelSerializer):
    """Serializer для заказа."""

    creator = UseSerializer(read_only=True)
    positions = ItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ('id', 'creator', 'positions', 'status', 'total_price', 'created_at', 'updated_at',)

    def create(self, validated_data):
        """Метод создания заказа"""
        validated_data["creator"] = self.context["request"].user
        positions_data = validated_data.pop('positions')
        order = super().create(validated_data)

        raw_positions = []
        for position in positions_data:
            position = Item(order=order,
                            product=position["product"],
                            quantity=position["quantity"],
                            price=position["product"].price)
            raw_positions.append(position)
        Item.objects.bulk_create(raw_positions)
        return order

