from rest_framework import serializers
from books.models import Publisher, Book, Author, Warehouse, WarehouseBook, Image
from users.models import Account, Address, Cart, BookInCart


class PublisherSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Publisher
        fields = ["url", "id", "name", "address", "phone", "publisher_url"]


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = ["url", "id", "name", "phone", "address"]


class BookSerializer(serializers.HyperlinkedModelSerializer):
    author = AuthorSerializer(read_only=True)
    publisher = PublisherSerializer(read_only=True)

    class Meta:
        model = Book
        fields = [
            "url",
            "id",
            "title",
            "author",
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
        fields = ["url", "id", "book", "book_cover"]


class AddressSerializer(serializers.HyperlinkedModelSerializer):
    model = Address
    fields = ["url", "id", "address1", "address2", "zip_code", "country"]


class CartSerializer(serializers.HyperlinkedModelSerializer):
    model = Cart
    fields = ["url", "id", "user"]


class BookInCartSerializer(serializers.HyperlinkedModelSerializer):
    model = BookInCart
    fields = ["url", "id", "cart", "book", "count"]


class AccountSerializer(serializers.HyperlinkedModelSerializer):
    address = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Account
        fields = ["url", "id", "firstname", "lastname", "email", "address"]
