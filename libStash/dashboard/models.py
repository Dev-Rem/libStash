import uuid

from django.db import models
from phone_field import PhoneField

from books.models import Book

# Create your models here.


class Warehouse(models.Model):
    address = models.TextField(verbose_name="Address", max_length=200)
    phone = PhoneField(verbose_name="Phone number", blank=True)
    unique_id = models.UUIDField(
        default=uuid.uuid4, editable=False, db_index=True, unique=True
    )
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "warehouse"

    def __str__(self):
        return f"{self.address}"


class WarehouseBook(models.Model):
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    count = models.IntegerField(verbose_name="Book count", default=0)
    unique_id = models.UUIDField(
        default=uuid.uuid4, editable=False, db_index=True, unique=True
    )
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "warehouse_book"

    def __str__(self):
        return f"{self.book}, {self.count}"
