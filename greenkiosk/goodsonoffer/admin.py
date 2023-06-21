from django.contrib import admin
from .models import Offer

# Register your models here.
class OfferAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "price", "quantity", "condition", "taxes")

admin.site.register(Offer, OfferAdmin)
