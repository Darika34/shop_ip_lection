from django.shortcuts import render
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from product.models import Product
from product.permissions import IsAuthor
from product.serializers import ProductSerializer


# Create your views here.

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            return (permissions.IsAuthenticated(), IsAuthor())
        return (permissions.IsAuthenticatedOrReadOnly(),)

