from rest_framework import serializers
from Products.models import Product, SoldProduct
from user.models import User


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class SoldProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = SoldProduct
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
