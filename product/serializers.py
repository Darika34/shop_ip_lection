from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from product.models import Product


class ProductSerializer(ModelSerializer):
    owner_email = serializers.ReadOnlyField(source='owner.email')
    owner = serializers.ReadOnlyField(source='owner.id')

    class Meta:
        model = Product
        fields = '__all__'
