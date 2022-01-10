import django_filters
from rest_framework import viewsets

from products.models import Product
from products.serializers import ProductCreateSerializer, ProductListSerializer


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

