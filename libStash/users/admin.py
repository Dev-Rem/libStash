from django.contrib import admin
from .models import Address, Cart, CartBook
from django.contrib.auth.admin import UserAdmin

# Register your models here.


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ("user", "address1", "address2", "zip_code", "country")


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ("user",)


@admin.register(CartBook)
class CartBookAdmin(admin.ModelAdmin):
    list_display = ("cart", "book", "count")
