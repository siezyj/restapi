from django.urls import include, path

from .views import UsersListAPIView

urlpatterns = [
    path("users", UsersListAPIView.as_view()),
]
