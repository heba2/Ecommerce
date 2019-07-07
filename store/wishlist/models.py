from django.db import models
from accounts.models import User
from products.models import Product

# Create your models here.


class Wish (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True, auto_now=False)
    quantity = models.IntegerField()
    total = models.DecimalField(max_digits=8, decimal_places=2)


