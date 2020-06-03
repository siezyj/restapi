from django.db import models


class Product(models.Model):
    name = models.TextField(unique=False)

    def __str__(self):
        return self.name
