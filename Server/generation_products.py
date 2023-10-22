import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "FastReportsServer.settings")

import django
django.setup()

import random
from Products.models import SoldProduct, Product
from faker import Faker
from django.core.exceptions import ObjectDoesNotExist
from decimal import Decimal
from datetime import datetime

# Инициализация Django
django.setup()

# Инициализация Faker
fake = Faker()

def generate_sales():
    products = Product.objects.all()

    for i in range(100):
        product = random.choice(products)  # Выбираем случайный продукт
        year = 2023
        month = random.randint(1, 12)
        day = random.randint(1, 28)  # Учтите февраль и високосные годы
        hour = random.randint(0, 23)
        minute = random.randint(0, 59)
        second = random.randint(0, 59)

        sale_date = datetime(year, month, day, hour, minute, second)
        quantity_sold = random.randint(1, 10)  # Генерируем случайное количество проданных товаров

        try:
            existing_product = Product.objects.get(name=product.name)
            category = existing_product.category
        except ObjectDoesNotExist:
            raise ObjectDoesNotExist("Отсутствие продукта")

        sales_amount = Decimal(existing_product.price) * Decimal(quantity_sold)

        SoldProduct.objects.create(
            product=existing_product,
            sale_date=sale_date,
            quantity_sold=quantity_sold,
            category=category,
            sales_amount=sales_amount
        )
        print(f'SoldProduct for product "{existing_product.name}" created successfully')


if __name__ == "__main__":
    generate_sales()
