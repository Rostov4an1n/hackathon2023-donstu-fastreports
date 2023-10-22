from django.test import TestCase
from decimal import Decimal
from .models import Product, SoldProduct
from django.core.exceptions import ValidationError


class ProductManagerTestCase(TestCase):
    """
    Этот класс содержит тесты для управления продуктами.

    Методы:
        - test_create_new_product: Проверяет создание нового продукта.
        - test_create_new_product_invalid_data: Проверяет обработку недопустимых данных при создании продукта.
        - test_update_product_price: Проверяет обновление цены продукта.
        - test_update_product_price_invalid_data: Проверяет обработку недопустимых данных при обновлении цены продукта.
    """

    def test_create_new_product(self):
        """
        Тест на создание нового продукта.

        Создает новый продукт и проверяет, что его атрибуты установлены верно.
        """
        product = Product.objects.create_new_product("Test Product", Decimal("9.99"))
        self.assertEqual(product.name, "Test Product")
        self.assertEqual(product.price, Decimal("9.99"))

    def test_create_new_product_invalid_data(self):
        """
        Тест на обработку недопустимых данных при создании продукта.

        Проверяет, что создание продукта с пустым именем или отрицательной ценой вызывает исключение ValidationError.
        """
        with self.assertRaises(ValidationError):
            Product.objects.create_new_product("", Decimal("9.99"))
        with self.assertRaises(ValidationError):
            Product.objects.create_new_product("Test Product", Decimal("-1.00"))

    def test_update_product_price(self):
        """
        Тест на обновление цены продукта.

        Создает новый продукт, обновляет его цену и проверяет, что цена была успешно обновлена.
        """
        product = Product.objects.create_new_product("Test Product", Decimal("9.99"))
        updated_product = Product.objects.update_product_price(product.id, Decimal("12.99"))
        self.assertEqual(updated_product.price, Decimal("12.99"))

    def test_update_product_price_invalid_data(self):
        """
        Тест на обработку недопустимых данных при обновлении цены продукта.

        Проверяет, что обновление цены на неположительное значение или для несуществующего продукта вызывает исключение ValidationError.
        """
        product = Product.objects.create_new_product("Test Product", Decimal("9.99"))
        with self.assertRaises(ValidationError):
            Product.objects.update_product_price(product.id, Decimal("-1.00"))
        with self.assertRaises(ValidationError):
            Product.objects.update_product_price(999, Decimal("12.99"))

class SoldProductTestCase(TestCase):
    """
    Этот класс содержит тесты для продажи продуктов.

    Методы:
        - test_calculate_total_price: Проверяет вычисление общей стоимости продажи.
        - test_save_sales_amount: Проверяет автоматическое сохранение суммы продажи.
        - test_save_sales_amount_zero_quantity: Проверяет автоматическое сохранение суммы продажи при нулевом количестве продуктов.
        - test_save_sales_amount_negative_quantity: Проверяет автоматическое сохранение суммы продажи при отрицательном количестве продуктов.
    """

    def setUp(self):
        """
        Настроить начальные данные для тестов.

        Создает несколько продуктов для использования в других тестах.
        """
        self.product1 = Product.objects.create_new_product("Product 1", Decimal("10.00"))
        self.product2 = Product.objects.create_new_product("Product 2", Decimal("15.00"))

    def test_calculate_total_price(self):
        """
        Тест на вычисление общей стоимости продажи.

        Создает продажу и проверяет, что общая стоимость продажи правильно вычислена.
        """
        sale_product = SoldProduct.objects.create(
            product=self.product1,
            sale_date="2023-10-21",
            quantity_sold=5,
            category="Category 1"
        )
        self.assertEqual(sale_product.calculate_total_price(), Decimal("50.00"))

    def test_save_sales_amount(self):
        """
        Тест на автоматическое сохранение суммы продажи.

        Создает продажу и проверяет, что сумма продажи автоматически сохраняется при создании.
        """
        sale_product = SoldProduct.objects.create(
            product=self.product2,
            sale_date="2023-10-21",
            quantity_sold=3,
            category="Category 2"
        )
        self.assertEqual(sale_product.sales_amount, Decimal("45.00"))

    def test_save_sales_amount_zero_quantity(self):
        """
        Тест на автоматическое сохранение суммы продажи при нулевом количестве продуктов.

        Создает продажу с нулевым количеством продуктов и проверяет, что сумма продажи установлена в ноль.
        """
        sale_product = SoldProduct.objects.create(
            product=self.product2,
            sale_date="2023-10-21",
            quantity_sold=0,
            category="Category 2"
        )
        self.assertEqual(sale_product.sales_amount, Decimal("0.00"))

    def test_save_sales_amount_negative_quantity(self):
        """
        Тест на автоматическое сохранение суммы продажи при отрицательном количестве продуктов.

        Создает продажу с отрицательным количеством продуктов и проверяет, что сумма продажи установлена в ноль.
        """
        sale_product = SoldProduct.objects.create(
            product=self.product2,
            sale_date="2023-10-21",
            quantity_sold=-1,
            category="Category 2"
        )
        self.assertEqual(sale_product.sales_amount, Decimal("0.00"))
