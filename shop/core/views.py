from abc import ABC

from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from rest_framework import filters, generics
from rest_framework.permissions import IsAuthenticated

User = get_user_model()


class UsersABCView(ABC):
    permission_classes = [
        IsAuthenticated,
    ]

    def get_queryset(self):
        raise NotImplementedError

    def get_serializer_context(self):
        return {"user": self.request.user}


class UsersListAPIView(UsersABCView, generics.ListAPIView):
    def get_queryset(self):
        return User.objects.filter(is_active=True)