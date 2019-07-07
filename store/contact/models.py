from django.db import models
from accounts.models import User
# Create your models here.


class Contact(models.Model):
    contact_email = models.EmailField(null=False)
    subject = models.CharField(max_length=100, null=False)
    content = models.CharField(max_length=255, null=False)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    admin = models.ForeignKey(User, on_delete=models.CASCADE, related_name='admin')
    date = models.DateTimeField(auto_now=False, auto_now_add=True, null=True)

    class Meta:
        db_table = 'Contact'

    def __str__(self):
        return self.sender.username
