from typing import Optional
from django.views.decorators.cache import cache_page
from Products.models import Product, SoldProduct
from .serializers import ProductSerializer, SoldProductSerializer, ApiKeySerializer
import logging
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import UserSerializer
from django.contrib.auth import login, authenticate
import os
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import ApiKey
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes, permission_classes
from .authentication import ApiKeyAuthentication

# Создайте каталог для хранения лог-файлов
log_directory = 'logs'
os.makedirs(log_directory, exist_ok=True)

# Настройка логгирования в файлы
logging.basicConfig(
    filename=os.path.join(log_directory, 'api.log'),
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] [%(name)s]: %(message)s'
)
logger = logging.getLogger(__name__)


@authentication_classes([ApiKeyAuthentication, SessionAuthentication, BasicAuthentication])
@api_view(['GET'])
@permission_classes([IsAuthenticated])
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
@permission_classes([IsAuthenticated])
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
    product_id: Optional[str] = request.query_params.get('product')

    # Создаем объект QuerySet для фильтрации проданных продуктов
    sold_products = SoldProduct.objects

    if product_id:
        sold_products = sold_products.filter(product_id)
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


@api_view(['POST'])
@permission_classes([AllowAny])
@csrf_exempt
def loging_user(request):
    """
    Аутентифицирует и выполняет вход пользователя.

    Parameters:
        request (Request): HTTP-запрос с данными пользователя для аутентификации.

    Returns:
        Response: HTTP-ответ с данными пользователя, если аутентификация успешна,
        или ошибкой, если аутентификация не удалась.
    """
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            logger.info(f'Пользователь {user.username} успешно вошел в систему.')
            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)

        logger.error('Ошибка при аутентификации пользователя: неверный логин или пароль.')
        return Response({'error': 'Неверный логин или пароль'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
@permission_classes([AllowAny])
@csrf_exempt
def register_user(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            login(request, user)
            logger.info(f'Зарегистрирован новый пользователь с именем {user.username}.')
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        logger.error(f'Ошибка при регистрации нового пользователя: {serializer.errors}')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CreateApiKey(APIView):
    @classmethod
    def post(cls, request):
        api_key = ApiKey()
        api_key.save()
        serializer = ApiKeySerializer(api_key)
        return Response(serializer.data, status=status.HTTP_201_CREATED)