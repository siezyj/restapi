from django.conf import settings
from django.db import models


class Order(models.Model):
    name = models.TextField(unique=False)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name="orders",
    )

    def __str__(self):
        return self.name
