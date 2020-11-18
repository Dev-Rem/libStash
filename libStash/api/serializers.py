from rest_framework import serializers
from blog.models import Post,Comment,Image
from books.models import Publisher,Author,Book,Warehouse,WarehouseBook
from users.models import Account,Address,Cart,BookInCart
from djoser.serializers import UserSerializer as BaseUserSerializer

# Serializer classes

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['unique_id', 'title', 'content', 'account', 'is_active', 'date',]

class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = ['unique_id', 'post', 'book', 'account',  'comment', 'likes', 'is_active', 'date',]
        read_only_fields = ('post', 'book', 'account', 'likes','is_active' )

class ImageSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField('get_image_url')
    class Meta:
        model = Image
        fields = ['unique_id','book', 'post','image', 'image_url', 'date']
    def get_image_url(self, obj):
        return obj.image.url

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

class BookInCartSerializer(serializers.ModelSerializer):
    book = BookSerializer(read_only=True)
    class Meta:
        model = BookInCart
        fields = ['unique_id', 'cart','book', 'count', ]
        read_only_fields = ('cart')

class CartSerializer(serializers.ModelSerializer):
    item_in_cart = BookInCartSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ["unique_id", "account", "item_in_cart", "is_active"]

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

