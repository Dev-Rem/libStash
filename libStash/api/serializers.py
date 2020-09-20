from rest_framework import serializers
from books.models import Publisher, Book, Author, Warehouse, WarehouseBook, Image


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


# class WarehouseSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Warehouse
#         fields = ["address", "phone", 'last_update']


# class WarehouseBookSerilizer(serializers.ModelSerializer):
#     class meta:
#         model = WarehouseBook
#         fields = ["warehouse", "book", "count", 'last_update']
