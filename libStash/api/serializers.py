from rest_framework import serializers
from books.models import *
from users.models import *
from djoser.serializers import UserSerializer as BaseUserSerializer

class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = [ "unique_id", "name", "address", "email", "publisher_url"]

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = [ "unique_id", "name", "email", "address"]

class BookReviewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = BookReview
        fields = ['unique_id','account', 'comment', 'date']

class BookReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookReview
        fields = ['comment', 'date']

class BookSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Book
        fields = ['title', 'author', 'category', 'format', 'year', 'price', 'unique_id']

class BookDetailSerializer(serializers.ModelSerializer):

    author = AuthorSerializer(read_only=True)
    publisher = PublisherSerializer(read_only=True)

    class Meta:
        model = Book
        fields = [
            "unique_id",
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
        fields = ['book', 'book_cover', 'unique_id']

class BookInCartSerializer(serializers.ModelSerializer):
    book = BookSerializer(read_only=True)
    class Meta:
        model = BookInCart
        fields = ['cart','book', 'count', 'unique_id']

class CartSerializer(serializers.ModelSerializer):
    item_in_cart = BookInCartSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ["unique_id", "account", "item_in_cart", "is_active"]

class AddToCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookInCart
        fields = ['book', 'count']

class AddressSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Address
        fields = ["unique_id", 'account', "address1", "address2", "zip_code", "country"]

class UserSerializer(BaseUserSerializer):
    class Meta:
        model = Account
        fields = ['unique_id', 'firstname', 'lastname', 'email']

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['unique_id', 'firstname', 'lastname', 'email']

class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = ['address', 'phone', 'unique_id']

class WarehouseBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = WarehouseBook
        fields = ['warehouse', 'book', 'count', 'unique_id']

