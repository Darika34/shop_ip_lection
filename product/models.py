from django.db import models
from django.contrib.auth import get_user_model

from category.models import Category

# Create your models here.
User = get_user_model()
class Product(models.Model):
    STATUS_CHOICE = (
        ('in_stock', 'v nalichii'),
        ('out_of_stock', 'net v nalichii')
        # 'znachenie', 'oboznachenie'
    )
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='product')
    title = models.CharField(max_length=225)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images')
    price = models.DecimalField(max_digits=9, decimal_places=2)
    stock = models.CharField(choices=STATUS_CHOICE, max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'