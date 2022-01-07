from django.db import models


class Product(models.Model):
    name = models.CharField()
    categories = models.ManyToManyField(
        'Category',
        on_delete=models.PROTECT,
        related_name='products'
    )
    category = models.CharField()
    price_min = models.PositiveIntegerField()
    price_max = models.PositiveIntegerField()
    is_published = models.BooleanField(default=False)
    is_removed = models.BooleanField(default=False)

    def __str__(self):
        return f'Product: {self.name}'

