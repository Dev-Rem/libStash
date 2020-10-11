from rest_framework import serializers
from books.models import *
from users.models import *
from djoser.serializers import UserSerializer as BaseUserSerializer

class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = [ "id", "name", "address", "phone", "publisher_url"]

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = [ "id", "name", "phone", "address"]

class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = [
            "id",
            "title",
            "category",
            "format",
            "isbn",
            "year",
            "price"
        ]

class BookDetailSerializer(serializers.ModelSerializer):

    author = AuthorSerializer(read_only=True)
    publisher = PublisherSerializer(read_only=True)

    class Meta:
        model = Book
        fields = [
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

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = [ "id", "book", "book_cover"]

class BookInCartSerializer(serializers.ModelSerializer):
    book = BookSerializer(read_only=True)
    class Meta:
        model = BookInCart
        fields = ["id", "book", "count"]

class CartSerializer(serializers.ModelSerializer):
    item_in_cart = BookInCartSerializer(many=True)

    class Meta:
        model = Cart
        fields = ["id", "account", "item_in_cart", "is_active"]

class AddToCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookInCart
        fields = ['book', 'count']

class BookReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = BookReview
        fields = ['account', 'comment', 'date']

class AddressSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Address
        fields = ["id", "address1", "address2", "zip_code", "country"]

class UserSerializer(BaseUserSerializer):
    class Meta:
        model = Account
        fields = ['id', 'firstname', 'lastname', 'email']



