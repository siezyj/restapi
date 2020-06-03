from typing import Dict

from rest_framework import serializers

from apps.products.models.order import Order, OrderDetail
from apps.products.models.product import Product

from apps.products.serializers.product_serializer import (
    ProductForOrderSerializer
)

from core.serializers import (
    UserSerializer
)



class OrderDetailSerializer(serializers.ModelSerializer):
    product = ProductForOrderSerializer(
        required=False, allow_null=True
    )
    
    user = UserSerializer(read_only=True)


    class Meta:
        model = OrderDetail
        fields = ["quantity", "product", "order"]

    def validate(self, attrs):
        if  not Product.objects.filter(name=attrs["product"]["name"]).exists():
            raise serializers.ValidationError(f"Product don`t exsist")
        return super().validate(attrs)

    def create(self, validated_data: Dict) -> OrderDetail:
        product_data = validated_data.pop("product", None)

        validated_data[
            "product"
        ] = ProductForOrderSerializer.create_for_order_upload(
            product_data
        )

        return super().create(validated_data)

class OrderSerializer(serializers.ModelSerializer):
    order = OrderDetailSerializer(many=True)


    class Meta:
        model = Order
        fields = ["name", "user"]

    def validate(self, attrs):
        attrs["user"] = self.validate_user(self.context["user"])
        return super().validate(attrs)

