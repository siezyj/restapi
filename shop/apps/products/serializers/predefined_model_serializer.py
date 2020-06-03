from typing import Dict, Optional

from django.db import models
from rest_framework import serializers


class PredefinedModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Model
        fields = ["name"]
        extra_kwargs = {
            "name": {"validators": []},
        }

    def validate_name(self, name: str) -> Optional[str]:
        """
        Check that object exists in DB
        """
        if not self.Meta.model.objects.filter(name=name).exists():
            raise serializers.ValidationError(
                f"{self.Meta.model.__name__} not found in DB"
            )
        return name

    @staticmethod
    def create_for_order_upload(validated_data: Dict):
        raise NotImplementedError
