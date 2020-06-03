from abc import ABC

from rest_framework.permissions import IsAuthenticated


class BaseUserContextABCView(ABC):
    permission_classes = [
        IsAuthenticated
    ]

    def get_queryset(self):
        raise NotImplementedError

    def get_serializer_context(self):
        return {"user": self.request.user}
