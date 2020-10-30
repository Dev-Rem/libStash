from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from .models import *


# Register your models here.

admin.site.unregister(Group)
@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = (
        "firstname",
        "lastname",
        "email",
        "date_joined",
        "last_login",
        "is_admin",
    )

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ("account", "address1", "address2", "zip_code", "country")


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ("account", "is_active")


@admin.register(BookInCart)
class BookInCartAdmin(admin.ModelAdmin):
    list_display = ("cart", "book", "count")


@admin.register(BookReview)
class BookReviewAdmin(admin.ModelAdmin):
    list_display = ("book", "account", "comment", "is_active", "date")
