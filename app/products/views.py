from rest_framework import viewsets, serializers
from rest_framework.exceptions import ValidationError

from products.models import Product


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def validate_categories(self, value):
        categories_count = len(value)
        if categories_count > 10:
            raise ValidationError("You can't assign more than ten categories")
        if categories_count < 2:
            raise ValidationError("You can't assign less than two categories")
        return value


class ProductListSerializer(serializers.HyperlinkedModelSerializer):
    price = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'name', 'categories', 'is_published', 'price']

    def get_price(self, instance):
        return f'{instance.price_min}-{instance.price_max}' # You specifically asked to return one field


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.filter(is_removed=False)

    def get_serializer_class(self):
        if self.action == 'list':
            return ProductListSerializer
        return ProductSerializer

