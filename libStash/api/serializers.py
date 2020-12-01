from rest_framework import serializers
from blog.models import Post,PostComment,PostImage
from books.models import Author,Book,Warehouse,WarehouseBook,Publisher, BookInCart,Cart,BookComment,BookImage
from users.models import Account,Address
from djoser.serializers import UserSerializer as BaseUserSerializer

# Serializer classes

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['unique_id', 'title', 'content', 'account', 'likes', 'date',]

class PostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImage
        fields = ['unique_id', 'post', 'image']

class PostCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostComment
        fields = ['unique_id', 'post', 'account', 'comment', 'date']

class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = [ "unique_id", "name", "address", "email", "publisher_url"]

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = [ "unique_id", "name", "email", "address"]

class BookSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Book
        fields = ['unique_id', 'title', 'author', 'category', 'format', 'year', 'price', ]

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

class BookImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookImage
        fields = ['unique_id', 'post', 'image']

class BookCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookComment
        fields = ['unique_id', 'post', 'account', 'comment', 'date']

class BookInCartSerializer(serializers.ModelSerializer):
    book = serializers.SlugRelatedField(read_only=True, slug_field='unique_id')
    class Meta:
        model = BookInCart
        fields = ['unique_id','book', 'count', ]

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ["unique_id", "account", "is_active"]

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
        fields = ['unique_id', 'address', 'phone', ]

class WarehouseBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = WarehouseBook
        fields = ['unique_id', 'warehouse', 'book', 'count', ]

