from django.db import models
from accounts.models import Customer
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        db_table = "Category"

    def __str__(self):
        return self.name


class Product(models.Model):
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, related_name='products')
    product_name = models.CharField(max_length=60, null=False, unique=True)
    product_price = models.DecimalField(max_digits=7, decimal_places=2)
    product_quantity = models.IntegerField()
    product_description = models.CharField(max_length=150)
    product_image = models.ImageField(upload_to='img')

    class Meta:
        db_table = "Product"

    def __str__(self):
        return self.product_name







