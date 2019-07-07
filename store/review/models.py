from django.db import models
from accounts.models import User
from products.models import Product


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usersReviewing', null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='serviceReviewed', null=True)
    rating = models.PositiveIntegerField()
    comment = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.product.product_name + ' reviewed by ' + self.user.username

    class Meta:
        db_table = 'Reviews'


