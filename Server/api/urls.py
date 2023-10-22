from django.urls import path
from . import views


app_name = 'api'  # Это устанавливает пространство имен для приложения

urlpatterns = [
    path('products/', views.get_products, name='get_products'),
    path('sold-products/', views.get_sold_products, name='get_sold_products'),
    path('login/', views.loging_user, name='login'),
    path('register/', views.register_user, name='register'),
]
