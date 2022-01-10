from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from products.models import Product


class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'is_removed', 'is_published', 'categories')

    def validate(self, data):
        categories_len = len(data['categories']) # Because there is no case when categories is not passed

        if categories_len > 10:
            raise ValidationError("You can't assign more than ten categories")
        if categories_len < 2:
            data['is_published'] = False
        return data


class ProductListSerializer(ProductCreateSerializer):
    categories = serializers.SlugRelatedField(many=True, slug_field='name', read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'is_removed', 'is_published', 'categories')

