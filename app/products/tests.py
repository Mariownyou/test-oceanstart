from django.test import TestCase, Client
from django.urls.base import reverse

from products.models import Product
from categories.models import Category


class ProductBaseTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.category_1 = Category.objects.create(name='category 1')
        cls.category_2 = Category.objects.create(name='category 2')
        cls.products = [Product.objects.create(
            id=i,
            name=f'test product {i}',
            price=1000 * i,
            is_published=True,
            is_removed=False,
        ) for i in range(10)]

        for product in cls.products:
            product.categories.set([cls.category_1, cls.category_2])
            product.save()

        cls.category = Category.objects.create(name='category 3')
        cls.product = cls.products[0]
        cls.product.categories.set([cls.category, cls.category_1, cls.category_2])
        cls.product.save()

    def setUp(self):
        self.client = Client()


class ProductModelTestCase(ProductBaseTestCase):
    pass


class ProductViewsTestCase(ProductBaseTestCase):
    def test_delete(self):
        self.assertEqual(Product.objects.count(), 10)
        response = self.client.delete(reverse('product-detail', args=[self.product.id]))
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Product.objects.count(), 10)
        self.product.refresh_from_db()
        self.assertEqual(self.product.is_removed, True)

class ProductFilterTestCase(ProductBaseTestCase):
    def test_name_filter(self):
        response = self.client.get(reverse('product-list'), {'name': 'test product 1'})
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertEqual(len(response_data), 1)
        self.assertEqual(response_data[0]['name'], 'test product 1')

    def test_category_name_filter(self):
        response = self.client.get(reverse('product-list'), {'categories__name': 'category 1'})
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertEqual(len(response_data), 10)
        self.assertIn('category 1', response_data[0]['categories'])

        response = self.client.get(reverse('product-list'), {'categories__name': 'category 3'})
        response_data = response.json()
        self.assertEqual(len(response_data), 1)
        self.assertIn('category 3', response_data[0]['categories'])

    def test_category_id_filter(self):
        response = self.client.get(reverse('product-list'), {'categories__id': self.category_1.id})
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertEqual(len(response_data), 10)
        self.assertIn('category 1', response_data[0]['categories'])

        response = self.client.get(reverse('product-list'), {'categories__id': self.category.id})
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertEqual(len(response_data), 1)
        self.assertIn('category 3', response_data[0]['categories'])

    def test_price_filter(self):
        response = self.client.get(reverse('product-list'), {'price__gt': 0, 'price__lt': 2000})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)

        response = self.client.get(reverse('product-list'), {'price__gt': 0, 'price__lt': 2001})
        self.assertEqual(len(response.json()), 2)

        response = self.client.get(reverse('product-list'), {'price__gt': -1, 'price__lt': 10001})
        self.assertEqual(len(response.json()), 10)

