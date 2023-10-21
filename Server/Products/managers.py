from django.db import models
from django.core.exceptions import ObjectDoesNotExist, ValidationError


class ProductManager(models.Manager):
    def create_new_product(self, name, price):
        """
        Создает новый продукт и сохраняет его в базе данных.

        :param name: Название нового продукта.
        :param price: Цена нового продукта.
        :return: Созданный объект продукта.
        :raises ValidationError: Если название пустое или цена меньше или равна нулю.
        """
        if not name:
            raise ValidationError("Product name cannot be empty")
        if price <= 0:
            raise ValidationError("Price must be greater than zero")

        product = self.create(name=name, price=price)
        return product

    def delete_product(self, product_id):
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

    def get_top_selling_products(self, limit=10):
        """
        Возвращает топ продаваемых продуктов с ограничением на количество.

        :param limit: Максимальное количество возвращаемых продуктов (по умолчанию 10).
        :return: QuerySet с топ продаваемых продуктов.
        """
        return self.order_by('-sales_count')[:limit]

    def calculate_total_price(self):
        """
        Вычисляет общую стоимость продуктов в базе данных.

        :return: Общая стоимость продуктов.
        """
        total_price = self.aggregate(total_price=models.Sum(models.F('price') * models.F('quantity')))
        return total_price['total_price']

    def update_product_price(self, product_id, new_price):
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
