from django.db import models
from django.contrib.auth.models import User
from books.models import Book


# Create your models here.


class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address1 = models.CharField("Address line 1", max_length=1024)
    address2 = models.CharField("Address line 2", max_length=1024, blank=True)
    zip_code = models.CharField("ZIP / Postal code", max_length=12)
    country = models.CharField("Country", max_length=100)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class CartBook(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    count = models.IntegerField()