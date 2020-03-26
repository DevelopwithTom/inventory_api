from rest_framework.test import APITestCase
# from django.urls import reverse
from core.models import Product


class ProductTest(APITestCase):

    def test_empty_products(self):
        link = '/inventory/product/'
        response = self.client.get(link)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(0, len(response.json()))

    def test_product_create(self):
        Product.objects.create(quantity=10, name='one', price=1.1)
        link = '/inventory/product/'
        response = self.client.get(link)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(1, len(response.json()))

    def test_product_delete(self):
        Product.objects.create(quantity=10, name='two', price=1.1).delete()
        link = '/inventory/product/'
        response = self.client.get(link)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(0, len(response.json()))
