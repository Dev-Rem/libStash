from books.models import (
    Author,
    Book,
    BookComment,
    BookImage,
    BookInCart,
    Cart,
    Publisher,
    Warehouse,
    WarehouseBook,
)

from rest_framework.serializers import ModelSerializer, SlugRelatedField


class PublisherSerializer(ModelSerializer):
    class Meta:
        model = Publisher
        fields = ["unique_id", "name", "address", "email", "publisher_url"]


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = ["unique_id", "name", "email", "address"]


class BookImageSerializer(ModelSerializer):

    book = SlugRelatedField(slug_field="unique_id", read_only=True)

    class Meta:
        model = BookImage
        fields = ["unique_id", "book", "image"]


class BookCommentSerializer(ModelSerializer):

    account = SlugRelatedField(slug_field="unique_id", read_only=True)
    book = SlugRelatedField(slug_field="unique_id", read_only=True)

    class Meta:
        model = BookComment
        fields = ["unique_id", "book", "account", "comment", "date"]


class BookSerializer(ModelSerializer):

    author = AuthorSerializer(many=True, read_only=True)
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


class BookInCartSerializer(ModelSerializer):

    book = BookSerializer(required=False)

    class Meta:
        model = BookInCart
        fields = ["unique_id", "book", "quantity", "amount"]


class CartSerializer(ModelSerializer):

    account = SlugRelatedField(slug_field="unique_id", read_only=True)

    class Meta:
        model = Cart
        fields = ["unique_id", "account", "is_active"]
