from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from decimal import Decimal
from datetime import date
from Products.models import Product, SoldProduct


class ProductAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.product = Product.objects.create(name="Test Product", price=Decimal("9.99"), category="Test Category")
        self.sold_product = SoldProduct.objects.create(product=self.product, sale_date=date(2023, 1, 15), quantity_sold=5, category="Category 1")

    def test_get_products(self):
        response = self.client.get(reverse('get_products'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_sold_products(self):
        response = self.client.get(reverse('get_sold_products'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_filter_products_by_category(self):
        response = self.client.get(reverse('get_products'), {'category': 'Test Category'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['products']), 1)

    def test_filter_sold_products_by_category(self):
        response = self.client.get(reverse('get_sold_products'), {'category': 'Category 1'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['sold_products']), 1)

    # def test_filter_sold_products_by_sale_date(self):
    #     response = self.client.get(reverse('get_sold_products'), {'sale_date': '2023-01-15'})
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(len(response.data['sold_products']), 1)
