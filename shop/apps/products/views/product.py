from .abc import BaseUserContextABCView

from rest_framework import generics

from apps.products.serializers import ProductSerializer
from apps.products.models.product import Product


class ProductABCView(BaseUserContextABCView):
    serializer_class = ProductSerializer

class ProductListCreateAPIView(ProductABCView, generics.ListCreateAPIView):
    def get_queryset(self):
        return Product.objects.all()


class ProductRetrieveDestroyAPIView(
    ProductABCView, generics.RetrieveDestroyAPIView
):
    def get_queryset(self):
        return Product.objects.filter(id=self.kwargs["pk"])
