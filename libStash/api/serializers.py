""" Required imports"""
import json

from djoser.serializers import UserSerializer as BaseUserSerializer
from rest_framework.fields import SerializerMethodField
from rest_framework import serializers
from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
from rest_framework import serializers

from blogs.models import Post, PostComment, PostImage
from users.models import Account, Address
from books.models import (
    Author,
    Book,
    Warehouse,
    WarehouseBook,
    Publisher,
    BookInCart,
    Cart,
    BookComment,
    BookImage,
)


# Serializer classes


class PostSerializer(serializers.ModelSerializer):
    """
    Serializer for the Post model.
    """

    account = serializers.SlugRelatedField(slug_field="unique_id", read_only=True)

    class Meta:
        model = Post
        fields = [
            "unique_id",
            "title",
            "content",
            "account",
            "likes",
            "date",
        ]


class PostImageSerializer(serializers.ModelSerializer):
    """
    Serializer for the PostImage model.
    """

    post = serializers.SlugRelatedField(slug_field="unique_id", read_only=True)

    class Meta:
        model = PostImage
        fields = ["unique_id", "post", "image"]


class PostCommentSerializer(serializers.ModelSerializer):
    """
    Serializer for the PostComment model.
    """

    account = serializers.SlugRelatedField(slug_field="unique_id", read_only=True)
    post = serializers.SlugRelatedField(slug_field="unique_id", read_only=True)

    class Meta:
        model = PostComment
        fields = ["unique_id", "post", "account", "comment", "date"]


class PublisherSerializer(serializers.ModelSerializer):
    """
    Serializer for the Publisher model.
    """

    class Meta:
        model = Publisher
        fields = ["unique_id", "name", "address", "email", "publisher_url"]


class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for the Author model.
    """

    class Meta:
        model = Author
        fields = ["unique_id", "name", "email", "address"]


class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for the Book model.
    """

    author = serializers.SlugRelatedField(
        many=True, slug_field="unique_id", read_only=True
    )

    class Meta:
        model = Book
        fields = [
            "unique_id",
            "title",
            "category",
            "author",
            "format",
            "year",
            "price",
        ]


class BookDetailSerializer(serializers.ModelSerializer):

    """
    Serializer for getting a single Book instance.
    It makes user of the Book model.
    """

    author = serializers.SlugRelatedField(
        many=True, slug_field="unique_id", read_only=True
    )
    publisher = serializers.SlugRelatedField(slug_field="unique_id", read_only=True)

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
    """
    Serializer for the BookImage model.
    """

    class Meta:
        model = BookImage
        fields = ["unique_id", "post", "image"]


class BookCommentSerializer(serializers.ModelSerializer):
    """
    Serializer for the BookComment model.
    """

    account = serializers.SlugRelatedField(slug_field="unique_id", read_only=True)
    book = serializers.SlugRelatedField(slug_field="unique_id", read_only=True)

    class Meta:
        model = BookComment
        fields = ["unique_id", "book", "account", "comment", "date"]


class BookInCartSerializer(serializers.ModelSerializer):
    """
    Serializer for the BookInCart model.
    """

    book = serializers.SlugRelatedField(slug_field="unique_id", read_only=True)

    class Meta:
        model = BookInCart
        fields = ["unique_id", "book", "quantity", "amount"]


class CartSerializer(serializers.ModelSerializer):
    """
    Serializer for the Cart model.
    """

    account = serializers.SlugRelatedField(slug_field="unique_id", read_only=True)

    class Meta:
        model = Cart
        fields = ["unique_id", "account", "is_active"]


class AddressSerializer(serializers.ModelSerializer):
    """
    Serializer for the Address model.
    """

    account = serializers.SlugRelatedField(slug_field="unique_id", read_only=True)

    class Meta:
        model = Address
        fields = [
            "unique_id",
            "account",
            "address1",
            "address2",
            "zip_code",
            "city",
            "country",
        ]


class UserSerializer(BaseUserSerializer):
    """
    Serializer for overriding the djoser default UserSerializer.
    """

    class Meta:
        model = Account
        fields = ["unique_id", "firstname", "lastname", "email"]


class AccountSerializer(serializers.ModelSerializer):
    """
    Serializer for the Account model.
    """

    class Meta:
        model = Account
        fields = ["unique_id", "firstname", "lastname", "email"]


class WarehouseSerializer(serializers.ModelSerializer):
    """
    Serializer for the Warehouse model.
    """

    class Meta:
        model = Warehouse
        fields = ["unique_id", "address", "phone"]


class WarehouseBookSerializer(serializers.ModelSerializer):
    """
    Serializer for the WarehouseBook model.
    """

    book = serializers.SlugRelatedField(slug_field="unique_id", read_only=True)

    class Meta:
        model = WarehouseBook
        fields = [
            "unique_id",
            "warehouse",
            "book",
            "count",
        ]
