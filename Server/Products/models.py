from django.db import models
from decimal import Decimal
from .managers import ProductManager
from django.utils import timezone


class Product(models.Model):
    """
    Модель "Product" представляет продукт в приложении "Products".

    Поля:
    - name (CharField): Название продукта (максимальная длина 100 символов).
    - price (DecimalField): Цена продукта в десятичном формате.

    Методы:
    - __str__(self): Возвращает строковое представление объекта (название продукта).
    """

    def __str__(self):
        return self.name

    name = models.CharField(max_length=100, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    objects = ProductManager()
    category = models.CharField(max_length=150, default=None)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)


class SoldProduct(models.Model):
    """
    Модель "SoldProduct" представляет информацию о продажах продуктов.

    Поля:
    - product (ForeignKey): Ссылка на связанный продукт.
    - sale_date (DateField): Дата продажи.
    - quantity_sold (PositiveIntegerField): Количество проданных товаров.
    - category (CharField): Категория проданного товара.
    - sales_amount (DecimalField): Сумма продажи (автоматически вычисляется).

    Методы:
    - calculate_total_price(self): Вычисляет сумму продажи на основе цены продукта и количества.
    - save(self, *args, **kwargs): Переопределяет метод сохранения для автоматического вычисления суммы продажи.
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    sale_date = models.DateField(default=timezone.now)
    quantity_sold = models.PositiveIntegerField()
    category = models.CharField(max_length=50)
    sales_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def calculate_total_price(self):
        return Decimal(self.product.price) * Decimal(self.quantity_sold)

    def save(self, *args, **kwargs):
        self.sales_amount = self.calculate_total_price()
        super().save(*args, **kwargs)



