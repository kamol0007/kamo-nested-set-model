from django.db import models
from nested.models import NestedModel


# Create your models here.
class Category(NestedModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True, related_name='products')
    price = models.FloatField()
    stock = models.IntegerField()
    description = models.TextField()

    class Meta:
        db_table = 'product'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['id']
