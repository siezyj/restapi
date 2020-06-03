from typing import Dict

from rest_framework import serializers

from apps.products.models.product import Product

from .predefined_model_serializer import PredefinedModelSerializer


class ProductForOrderSerializer(PredefinedModelSerializer):
    """
    Serilizer for creating Product when order is uploading.
    In this case we want get Product insted of create it. That is why unique valdiator
    is disabled for name.
    """

    class Meta:
        model = Product
        fields = ["name"]
        extra_kwargs = {
            "name": {"validators": []},
        }

    @staticmethod
    def create_for_order_upload(validated_data: Dict) -> Product:
        """
        Objects are predefinded in admin panel. 
        We want to get them not create new one.
        """
        return Product.objects.get(name=validated_data["name"])


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["name"]