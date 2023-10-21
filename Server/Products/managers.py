from django.db import models
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from decimal import Decimal, InvalidOperation
from django.utils import timezone


class ProductManager(models.Manager):
    def create_new_product(self, name: str, price: Decimal, category: str) -> models.Model:
        """
        Создает новый продукт и сохраняет его в базе данных.

        :param name: Название нового продукта.
        :param price: Цена нового продукта.
        :param category: Категория нового продукта
        :return: Созданный объект продукта.
        :raises ValidationError: Если название пустое, цена меньше или равна нулю или формат цены недопустим.
        """

        if not name:
            raise ValidationError("Product name cannot be empty")

        try:
            price = Decimal(price)
            if price <= 0:
                raise ValidationError("Price must be greater than zero")
        except (ValueError, InvalidOperation):
            raise ValidationError("Invalid price format")

        product = self.create(name=name, price=price, category=category)
        return product

    def delete_product(self, product_id: int) -> bool:
        """
        Удаляет продукт с указанным идентификатором из базы данных.

        :param product_id: Идентификатор продукта для удаления.
        :return: True в случае успешного удаления, False если запись не найдена.
        """
        try:
            product = self.get(pk=product_id)
            product.delete()
            return True
        except ObjectDoesNotExist:
            return False

    def get_top_selling_products(self, limit: int = 10) -> models.QuerySet:
        """
        Возвращает топ продаваемых продуктов с ограничением на количество.

        :param limit: Максимальное количество возвращаемых продуктов (по умолчанию 10).
        :return: QuerySet с топ продаваемых продуктов.
        """
        return self.order_by('-sales_count')[:limit]

    def calculate_total_price(self) -> Decimal:
        """
        Вычисляет общую стоимость продуктов в базе данных.

        :return: Общая стоимость продуктов.
        """
        total_price = self.aggregate(total_price=models.Sum(models.F('price') * models.F('quantity')))
        return total_price['total_price']

    def update_product_price(self, product_id: int, new_price: Decimal) -> models.Model:
        """
        Обновляет цену продукта с указанным идентификатором.

        :param product_id: Идентификатор продукта для обновления цены.
        :param new_price: Новая цена для продукта.
        :return: Обновленный объект продукта.
        :raises ValidationError: Если новая цена меньше или равна нулю.
        :raises ValidationError: Если продукт с указанным идентификатором не найден.
        """
        if new_price <= 0:
            raise ValidationError("Price must be greater than zero")

        try:
            product = self.get(pk=product_id)
            product.price = new_price
            product.save()
            return product
        except ObjectDoesNotExist:
            raise ValidationError("Product not found")


class SoldProductManager(models.Manager):
    def get_sold_products(self) -> models.QuerySet:
        """
        Получает список всех проданных продуктов.
        :return: QuerySet с объектами SoldProduct.
        """

        return self.all()

    def filter_by_category(self, category: str) -> models.QuerySet:
        """
        Фильтрует проданные продукты по категории.

        :param category: Категория для фильтрации.
        :return: QuerySet с объектами SoldProduct, отфильтрованными по категории.
        """

        return self.filter(category=category)

    def filter_by_sale_date(self, sale_date: timezone.date) -> models.QuerySet:
        """
        Фильтрует проданные продукты по дате продажи.

        :param sale_date: Дата продажи для фильтрации.
        :return: QuerySet с объектами SoldProduct, отфильтрованными по дате продажи.
        """
        return self.filter(sale_date=sale_date)

    def filter_by_date_range(self, start_date: timezone.date, end_date: timezone.date) -> models.QuerySet:
        """
        Фильтрует проданные продукты по диапазону дат.

        :param start_date: Начальная дата диапазона.
        :param end_date: Конечная дата диапазона.
        :return: QuerySet с объектами SoldProduct, отфильтрованными по диапазону дат.
        """

        return self.filter(sale_date__range=[start_date, end_date])

    def create_sold(self, product, sale_date, quantity_sold, category):
        """
        Создает новую запись о продаже продукта и сохраняет её в базе данных.

        :param product: Продукт, проданный в рамках записи.
        :param sale_date: Дата продажи.
        :param quantity_sold: Количество проданных товаров.
        :param category: Категория проданного товара.
        :return: Созданный объект SoldProduct.
        """

        sales_amount = Decimal(product.price) * Decimal(quantity_sold)
        sold_product = self.create(product=product,
                                   sale_date=sale_date,
                                   quantity_sold=quantity_sold,
                                   category=category,
                                   sales_amount=sales_amount)
        return sold_product
