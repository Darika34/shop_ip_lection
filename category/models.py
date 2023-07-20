from django.db import models
from django.utils.text import slugify
# Create your models here.
class Category(models.Model):
    slug = models.SlugField(max_length=50, primary_key=True,blank=True)
    name = models.CharField(max_length=150,unique=True)


    def save(self):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save()

    def __str__(self):
        return self.name

    #rewrite name
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categorys'