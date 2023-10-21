from django.urls import path
from . import views

urlpatterns = [
    # Маршруты для работы с продуктами
    path('products/', views.get_products, name='get_products'),

    # Маршруты для работы с проданными продуктами
    path('sold-products/', views.get_sold_products, name='get_sold_products'),
]
