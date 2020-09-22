from rest_framework import serializers
from books.models import Publisher, Book, Author, Warehouse, WarehouseBook, Image

# from users.models import Account, Address, Cart, CartBook


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ["name", "address", "phone", "url", "last_update"]


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ["name", "phone", "address", "last_update"]


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
            "title",
            "author",
            "book_cover",
            "publisher",
            "category",
            "format",
            "isbn",
            "year",
            "price",
            "last_update",
        ]


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ["book", "book_cover", "last_update"]


# class AccountSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Account
#         fields = ['firstname', 'lastname', 'email', ]