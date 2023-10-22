from django.db import models
from decimal import Decimal
from .managers import ProductManager, SoldProductManager
from datetime import date  # Импортируем date из модуля datetime


class Product(models.Model):
    """
    Модель "Product" представляет продукт в приложении "Products".

    Поля:
    - name (CharField): Название продукта (максимальная длина 100 символов).
    - price (DecimalField): Цена продукта в десятичном формате.
    - category (CharField): Категория продукта (максимальная длина 150 символов).

    Методы:
    - __str__(self): Возвращает строковое представление объекта (название продукта).
    """

    def __str__(self):
        return self.name

    name = models.CharField(max_length=100, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    product_count = models.IntegerField(default=0)
    category = models.CharField(max_length=150, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ProductManager()


class SoldProduct(models.Model):
    """
    Модель "SoldProduct" представляет информацию о продажах продуктов.

    Поля:
    - product (ForeignKey): Ссылка на связанный продукт.
    - sale_date (DateField): Дата продажи.
    - quantity_sold (PositiveIntegerField): Количество проданных товаров.
    - category (CharField): Категория проданного товара (максимальная длина 50 символов).
    - sales_amount (DecimalField): Сумма продажи (автоматически вычисляется).

    Методы:
    - calculate_total_price(self): Вычисляет сумму продажи на основе цены продукта и количества.
    - save(self, *args, **kwargs): Переопределяет метод сохранения для автоматического вычисления суммы продажи.
    """

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='sold_products', null=True, blank=True)
    sale_date = models.DateTimeField(auto_now_add=True)
    quantity_sold = models.PositiveIntegerField()
    category = models.CharField(max_length=50, blank=True, default="Unknown")
    sales_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    objects = SoldProductManager()

    def calculate_total_price(self):
        """
        Вычисляет сумму продажи на основе цены продукта и количества.
        """
        return Decimal(self.product.price) * Decimal(self.quantity_sold)

    def save(self, *args, **kwargs):
        """
        Переопределяет метод сохранения для автоматического вычисления суммы продажи.
        """
        self.sales_amount = self.calculate_total_price()
        super().save(*args, **kwargs)
