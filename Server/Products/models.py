from django.db import models
from decimal import Decimal  # Импортируем Decimal из модуля decimal


class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Название продукта
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Цена продукта

    def __str__(self):
        return self.name


class SoldProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    sale_date = models.DateField()
    quantity_sold = models.PositiveIntegerField()
    category = models.CharField(max_length=50)

    # Поле для хранения суммы продажи
    sales_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def calculate_total_price(self):
        return Decimal(self.product.price) * Decimal(self.quantity_sold)

    def save(self, *args, **kwargs):
        self.sales_amount = self.calculate_total_price()
        super().save(*args, **kwargs)

