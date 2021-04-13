from django.contrib import admin

from .models import (
    Author,
    Book,
    BookComment,
    BookImage,
    BookInCart,
    Cart,
    Publisher,
)

# Register your models here.


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "isbn", "year")
    search_fields = ("title", "author", "isbn", "year")


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "address")
    search_fields = ("name",)


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ("name", "address", "email", "publisher_url")
    search_fields = ("name",)



@admin.register(BookComment)
class BookCommentAdmin(admin.ModelAdmin):
    list_display = ("book", "account", "comment", "date")


@admin.register(BookImage)
class BookImageAdmin(admin.ModelAdmin):
    list_display = (
        "book",
        "image",
    )


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ("account", "is_active")


@admin.register(BookInCart)
class BookInCartAdmin(admin.ModelAdmin):
    list_display = ("cart", "book", "quantity", "amount")
