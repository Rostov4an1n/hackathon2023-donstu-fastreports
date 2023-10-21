from rest_framework import serializers
from Products.models import Product, SoldProduct


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class SoldProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = SoldProduct
        fields = '__all__'
