from django.db import models

# Create your models here.
class Available_products(models.Model):
    name = models.CharField(max_length = 255)
    description = models.TextField()
    price_per_quantity = models.DecimalField(max_digits = 8, decimal_places = 2)
    available_quantity = models.PositiveIntegerField()
    condition = models.CharField(max_length = 255)
    shipping_cost =  models.DecimalField(max_digits = 8, decimal_places=2)
    taxes = models.DecimalField(max_digits = 8, decimal_places = 2)