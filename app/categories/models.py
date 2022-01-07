from django.db import models


class Category(models.Model):
    name = models.CharField()

    def __str__(self):
        return f'Category: {self.name}'

