from rest_framework import viewsets
from rest_framework.exceptions import ValidationError

from categories.models import Category
from categories.serializers import CategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def perform_destroy(self, instance):
        if instance.products.exists():
            raise ValidationError("You can't delete category with related products")
        return super().perform_destroy(instance)

