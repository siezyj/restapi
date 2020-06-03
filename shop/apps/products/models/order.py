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


class OrderDetail(models.Model):
    product = models.ForeignKey(
        "Product",
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name="order_details",
    )

    order = models.ForeignKey(
        "Order",
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name="order_details",
    )
    
    quantity = models.BigIntegerField(default=1)
