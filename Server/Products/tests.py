from decimal import Decimal
from django.test import TestCase
from django.core.exceptions import ValidationError
from datetime import date, timedelta
from .models import Product, SoldProduct


class ProductManagerTestCase(TestCase):
    def test_create_new_product(self):
        """
        Тест на создание нового продукта.
        """
        product = Product.objects.create_new_product("Test Product", Decimal("9.99"), "Test Category")
        self.assertEqual(product.name, "Test Product")
        self.assertEqual(product.price, Decimal("9.99"))
        self.assertEqual(product.category, "Test Category")

    def test_create_new_product_invalid_data(self):
        """
        Тест на обработку недопустимых данных при создании продукта.
        """
        with self.assertRaises(ValidationError):
            Product.objects.create_new_product("", Decimal("9.99"), "Test Category")

    def test_update_product_price(self):
        """
        Тест на обновление цены продукта.
        """
        product = Product.objects.create_new_product("Test Product", Decimal("9.99"), "Test Category")
        updated_product = Product.objects.update_product_price(product.id, Decimal("14.99"))
        self.assertEqual(updated_product.price, Decimal("14.99"))

    def test_update_product_price_invalid_data(self):
        """
        Тест на обработку недопустимых данных при обновлении цены продукта.
        """
        product = Product.objects.create_new_product("Test Product", Decimal("9.99"), "Test Category")
        with self.assertRaises(ValidationError):
            Product.objects.update_product_price(product.id, Decimal("-1.00"))


class SoldProductTestCase(TestCase):
    def test_create_sold(self):
        """
        Тест создания продажи с менеджером `create_sold`.
        """
        product = Product.objects.create_new_product("Test Product", Decimal("9.99"), "Test Category")
        sale_date = date.today()  # Используем текущую дату
        sold_product = SoldProduct.objects.create_sold(product, sale_date, 5, "Category 1")

        self.assertEqual(sold_product.product, product)
        self.assertEqual(sold_product.sale_date, sale_date)
        self.assertEqual(sold_product.quantity_sold, 5)
        self.assertEqual(sold_product.category, "Category 1")
        self.assertEqual(sold_product.sales_amount, Decimal("49.95"))

    def test_filter_by_category(self):
        """
        Тест фильтрации проданных продуктов по категории.
        """
        product1 = Product.objects.create_new_product("Product 1", Decimal("10.00"), "Category A")
        product2 = Product.objects.create_new_product("Product 2", Decimal("20.00"), "Category B")

        SoldProduct.objects.create_sold(product1, date.today(), 5, "Category A")
        SoldProduct.objects.create_sold(product2, date.today(), 3, "Category B")

        category_a_sales = SoldProduct.objects.filter_by_category("Category A")
        category_b_sales = SoldProduct.objects.filter_by_category("Category B")

        self.assertEqual(category_a_sales.count(), 1)
        self.assertEqual(category_b_sales.count(), 1)

    # def test_filter_by_sale_date(self):
    #     """
    #     Тест фильтрации проданных продуктов по дате продажи.
    #     """
    #     product1 = Product.objects.create_new_product("Product 1", Decimal("10.00"), "Category A")
    #
    #     # Создайте записи продаж с уникальными датами продажи
    #     sale_date_1 = date(2023, 1, 15)
    #     sale_date_2 = date(2023, 1, 16)
    #     sale_date_3 = date(2023, 1, 17)
    #
    #     SoldProduct.objects.create_sold(product1, sale_date_1, 5, "Category A")
    #     SoldProduct.objects.create_sold(product1, sale_date_2, 3, "Category A")
    #     SoldProduct.objects.create_sold(product1, sale_date_3, 4, "Category A")
    #
    #     # Фильтруйте по уникальным датам
    #     sales_on_15th = SoldProduct.objects.filter_by_sale_date(sale_date_1)
    #     sales_on_16th = SoldProduct.objects.filter_by_sale_date(sale_date_2)
    #
    #     self.assertEqual(sales_on_15th.count(), 1)
    #     self.assertEqual(sales_on_16th.count(), 1)

    def test_filter_by_date_range(self):
        """
        Тест фильтрации проданных продуктов по диапазону дат.
        """
        product1 = Product.objects.create_new_product("Product 1", Decimal("10.00"), "Category A")

        SoldProduct.objects.create_sold(product1, date.today(), 5, "Category A")
        SoldProduct.objects.create_sold(product1, date.today(), 3, "Category A")
        SoldProduct.objects.create_sold(product1, date.today(), 4, "Category A")

        sales_in_range = SoldProduct.objects.filter_by_date_range(date.today(), date.today())

        self.assertEqual(sales_in_range.count(), 3)
