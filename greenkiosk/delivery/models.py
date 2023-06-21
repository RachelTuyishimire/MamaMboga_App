from django.db import models
# Create your models here.
class Delivery(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phoneNumber = models.CharField(max_length=20)
    delivery_time = models.DateTimeField(auto_now_add  = True)
    is_delivered = models.BooleanField(default=False)