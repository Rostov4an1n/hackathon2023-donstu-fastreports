from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from datetime import date
from Products.models import Product, SoldProduct  # Подключаем необходимые модели
from decimal import Decimal


class APITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_get_products(self):
        """
        Тест получения списка продуктов.

        Этот тест отправляет GET-запрос к API для получения списка продуктов.
        Должен возвращать HTTP 200 OK.
        """
        self.client.force_authenticate(user=self.user)

        response = self.client.get(reverse('api:get_products'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_sold_products(self):
        """
        Тест получения списка проданных продуктов.

        Этот тест отправляет GET-запрос к API для получения списка проданных продуктов.
        Должен возвращать HTTP 200 OK.
        """
        self.client.force_authenticate(user=self.user)

        response = self.client.get(reverse('api:get_sold_products'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_login_user(self):
        """
        Тест аутентификации и входа пользователя.

        Этот тест отправляет POST-запрос к API для аутентификации и входа пользователя.
        Должен возвращать HTTP 200 OK.
        """
        data = {'username': 'testuser', 'password': 'newpa5125@%!wqafrssword', 'email': 'tetstnawoitsnfg@gmail.com'}

        response = self.client.post(reverse('api:login_user'), data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_register_user(self):
        """
        Тест регистрации нового пользователя.

        Этот тест отправляет POST-запрос к API для регистрации нового пользователя.
        Должен возвращать HTTP 201 Created.
        """
        data = {'username': 'newuser', 'password': 'newpa5125@%!wqafrssword', 'email': 'asdpgiJ@gmail.com'}

        response = self.client.post(reverse('api:register_user'), data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_filter_sold_products_by_sale_date(self):
        """
        Тест фильтрации проданных продуктов по дате продажи.

        Этот тест создает проданные продукты с уникальной датой продажи, затем отправляет GET-запрос к API
        с параметром 'sale_date' для фильтрации. Должен возвращать HTTP 200 OK и список проданных продуктов.
        """
        self.client.force_authenticate(user=self.user)

        sale_date = date(2023, 1, 15)

        # Создайте продукт
        product1 = Product.objects.create_new_product("Product 1", Decimal("10.00"), "Category A")

        # Создайте записи продаж с уникальными датами продажи
        SoldProduct.objects.create_sold(product1, sale_date, 5, "Category A")
        SoldProduct.objects.create_sold(product1, sale_date, 3, "Category A")
        SoldProduct.objects.create_sold(product1, sale_date, 4, "Category A")

        response = self.client.get(reverse('api:get_sold_products') + f'?sale_date={sale_date}')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['sold_products']), 3)
