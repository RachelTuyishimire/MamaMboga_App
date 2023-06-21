from django.contrib import admin
from .models import Available_products

# Register your models here.
class Available_productsAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "price_per_quantity", "available_quantity", "condition","shipping_cost", "taxes")

admin.site.register(Available_products, Available_productsAdmin)
