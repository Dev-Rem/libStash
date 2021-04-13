from django.contrib import admin
from dashboard.models import Warehouse, WarehouseBook

# Register your models here.


@admin.register(WarehouseBook)
class WarehouseBookAdmin(admin.ModelAdmin):
    list_display = ("warehouse", "book", "count")


@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    list_display = ("address", "phone")