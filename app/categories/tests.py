from django.test import TestCase
from django.urls.base import reverse

from products.tests import BaseTestCase
from categories.models import Category


class CategoryViewsTestCase(BaseTestCase):
    def test_destroy_fails(self):
        self.assertEqual(Category.objects.count(), 3)
        response = self.client.delete(reverse('category-detail', args=[self.category.id]))
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()[0], "You can't delete category with related products")
        self.assertEqual(Category.objects.count(), 3)

    def test_destroy_success(self):
        self.assertEqual(Category.objects.count(), 3)
        category = Category.objects.create(name='new test category')
        self.assertEqual(Category.objects.count(), 4)

        response = self.client.delete(reverse('category-detail', args=[category.id]))
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Category.objects.count(), 3)

