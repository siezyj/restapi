from django.urls import include, path

from apps.products.views import (
    ProductRetrieveDestroyAPIView,
    ProductListCreateAPIView
)

urlpatterns = [

    path("product", ProductListCreateAPIView.as_view()),
    path("product/<str:pk>", ProductListCreateAPIView.as_view()),
]
