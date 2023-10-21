from typing import Optional
from django.views.decorators.cache import cache_page
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from Products.models import Product, SoldProduct
from .serializers import ProductSerializer, SoldProductSerializer


@api_view(['GET'])
@permission_classes([AllowAny])
@cache_page(60 * 15)  # Кеширование на 15 минут
def get_products(request):
    """
    Получает список продуктов с возможностью фильтрации.

    Parameters:
        request (Request): HTTP-запрос с параметрами фильтрации.

    Returns:
        Response: HTTP-ответ с списком продуктов или ошибкой, если запрос не может быть обработан.
    """
    # Извлекаем параметры фильтрации из запроса
    category: Optional[str] = request.query_params.get('category')
    created_at: Optional[str] = request.query_params.get('created_at')
    updated_at: Optional[str] = request.query_params.get('updated_at')
    date_range: Optional[str] = request.query_params.get('date_range')

    # Предварительная фильтрация по категории
    products = Product.objects
    if category:
        products = products.filter(category=category)

    # Фильтрация по дате создания, если указана
    if created_at:
        products = products.filter(created_at__date=created_at)

    # Фильтрация по дате обновления, если указана
    if updated_at:
        products = products.filter(updated_at__date=updated_at)

    # Фильтрация по диапазону дат создания, если указан
    if date_range:
        start_date, end_date = map(str.strip, date_range.split(','))
        products = products.filter(created_at__range=[start_date, end_date])

    # Получение списка продуктов
    products = products.all()
    serializer = ProductSerializer(products, many=True)
    return Response({'products': serializer.data}, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([AllowAny])
@cache_page(60 * 15)
def get_sold_products(request):
    """
    Получает список проданных товаров с возможностью фильтрации.

    Parameters:
        request (Request): HTTP-запрос с параметрами фильтрации.

    Returns:
        Response: HTTP-ответ с списком проданных товаров или ошибкой, если запрос не может быть обработан.
    """
    # Извлекаем параметры фильтрации из запроса
    category: Optional[str] = request.query_params.get('category')
    sale_date: Optional[str] = request.query_params.get('sale_date')
    date_range: Optional[str] = request.query_params.get('date_range')

    # Создаем объект QuerySet для фильтрации проданных продуктов
    sold_products = SoldProduct.objects

    # Применяем фильтрацию по категории
    if category:
        sold_products = sold_products.filter(category=category)

    # Фильтрация по дате продажи, если указана
    if sale_date:
        sold_products = sold_products.filter(sale_date=sale_date)

    # Фильтрация по диапазону дат продажи, если указан
    if date_range:
        start_date, end_date = map(str.strip, date_range.split(','))
        sold_products = sold_products.filter(sale_date__range=[start_date, end_date])

    # Получение списка проданных продуктов
    sold_products = sold_products.all()
    serializer = SoldProductSerializer(sold_products, many=True)

    return Response({'sold_products': serializer.data}, status=status.HTTP_200_OK)
