from django.urls import include, path

urlpatterns = [
    path("upload/", include("apps.products.urls")),
    path("core/", include("core.urls")),
]
