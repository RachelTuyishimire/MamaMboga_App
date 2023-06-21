from django.db import models

# Create your models here.
class Signup(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    email = models.EmailField()
    phone_number = models.CharField(max_length = 20)
    password = models.CharField(max_length = 255)
    password_confirmation = models.CharField(max_length = 255)
