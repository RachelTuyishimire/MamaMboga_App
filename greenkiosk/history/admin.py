from django.contrib import admin
from .models import History

# Register your models here.
class HistoryAdmin(admin.ModelAdmin):
    list_display = ("event", "entity", "date", "user_name", "notes")

admin.site.register(History, HistoryAdmin)
