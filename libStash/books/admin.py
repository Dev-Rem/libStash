from django.contrib import admin
from .models import Book, Image, Author, Publisher, Warehouse, WarehouseBook

# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "isbn", "year")


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "address")


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ("book_cover",)


@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    list_display = ("address", "phone")


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ("name", "address", "phone", "url")


@admin.register(WarehouseBook)
class WarehouseBookAdmin(admin.ModelAdmin):
    list_display = ("warehouse", "book", "count")
