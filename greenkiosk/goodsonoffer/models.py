from django.db import models

# Create your models here.
class Offer(models.Model):
    name = models.CharField(max_length = 255)
    description = models.TextField()
    price = models.DecimalField(max_digits = 8, decimal_places=2)
    quantity = models.PositiveIntegerField()
    condition = models.CharField(max_length = 255)
    taxes = models.DecimalField(max_digits = 8, decimal_places = 2)
