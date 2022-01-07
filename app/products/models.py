from django.db import models

from categories.models import Category


class Product(models.Model):
    name = models.CharField(max_length=100)
    categories = models.ManyToManyField(
        Category,
        related_name='products'
    )
    category = models.CharField(max_length=100)
    price_min = models.PositiveIntegerField()
    price_max = models.PositiveIntegerField()
    is_published = models.BooleanField(default=False)
    is_removed = models.BooleanField(default=False)

    def __str__(self):
        return f'Product: {self.name}'

