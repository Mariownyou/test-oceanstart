from django.db import models


class Category(models.Model):
    name = models.SlugField()

    def __str__(self):
        return str(self.name)

