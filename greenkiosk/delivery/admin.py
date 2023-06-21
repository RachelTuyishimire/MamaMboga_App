from django.contrib import admin
from .models import Delivery

# Register your models here.
class DeliveryAdmin(admin.ModelAdmin):
    list_display = ("name", "phoneNumber", "address", "delivery_time", "is_delivered")


admin.site.register(Delivery, DeliveryAdmin)
