from rest_framework import serializers
from books.models import Publisher, Book, Author, Warehouse, WarehouseBook, Image
from users.models import Account, Address, Cart, BookInCart


class PublisherSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Publisher
        fields = ["url", "name", "address", "phone", "url", "last_update"]


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = ["url", "name", "phone", "address", "last_update"]


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
            "url",
            "title",
            "author",
            "book_cover",
            "publisher",
            "category",
            "format",
            "isbn",
            "year",
            "price",
        ]


class ImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Image
        fields = ["url", "book", "book_cover", "last_update"]


class AccountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Account
        fields = ["url", "firstname", "lastname", "email"]


class AddressSerializer(serializers.HyperlinkedModelSerializer):
    model = Address
    fields = ["url", "address1", "address2", "zip_code", "country"]


class CartSerializer(serializers.HyperlinkedModelSerializer):
    model = Cart
    fields = ["url", "user"]


class BookInCartSerializer(serializers.HyperlinkedModelSerializer):
    model = BookInCart
    fields = ["url", "cart", "book", "count"]
