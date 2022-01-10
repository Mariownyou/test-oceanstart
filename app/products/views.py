import django_filters
from rest_framework import viewsets, serializers
from rest_framework.exceptions import ValidationError

from products.models import Product


class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'is_removed', 'categories')
        read_only_fields = ('is_published',)

    def validate_categories(self, value):
        categories_count = len(value)
        self.is_published = True

        if categories_count > 10:
            raise ValidationError("You can't assign more than ten categories")
        if categories_count < 2:
            self.is_published = False
        return value


class ProductListSerializer(ProductCreateSerializer):
    categories = serializers.SlugRelatedField(many=True, slug_field='name', read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'is_removed', 'is_published', 'categories')


class ProductFilter(django_filters.FilterSet):
    price = django_filters.NumberFilter()
    price__gt = django_filters.NumberFilter(field_name='price', lookup_expr='gt')
    price__lt = django_filters.NumberFilter(field_name='price', lookup_expr='lt')

    class Meta:
        model = Product
        fields = ('name', 'categories__name', 'categories__id', 'is_published', 'is_removed')


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.filter(is_removed=False)
    search_fields = ('name')
    filterset_class = ProductFilter

    def get_serializer_class(self):
        if self.action in ('create', 'update', 'partial_update'):
            return ProductCreateSerializer
        return ProductListSerializer

    def perform_destroy(self, instance):
        '''Marks product as removed on delete'''
        instance.is_removed = True
        instance.save()

