from django.db import models

# Create your models here.
class History(models.Model):
    event = models.CharField(max_length = 255)
    entity = models.CharField(max_length = 255)
    date  = models.DateTimeField(auto_now_add = True)
    user_name = models.CharField(max_length = 255)
    notes = models.TextField()

