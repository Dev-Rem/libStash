from rest_framework import serializers
from books.models import Publisher, Book, Author, Warehouse, WarehouseBook, Image
from users.models import Account, Address, Cart, BookInCart, BookReview


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


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ["id", "address1", "address2", "zip_code", "country"]


class AccountSerializer(serializers.HyperlinkedModelSerializer):
    address = AddressSerializer(many=True, read_only=True)
    password = serializers.CharField(style={"input_type": "password"}, write_only=True)
    password_confirm = serializers.CharField(
        style={"input_type": "password"}, write_only=True
    )

    def create(self, validated_data):
        account = Account(
            firstname=self.validated_data["firstname"],
            lastname=self.validated_data["lastname"],
            email=self.validated_data["email"],
        )
        password = self.validated_data["password"]
        password_confirm = self.validated_data["password_confirm"]
        if password != password_confirm:
            raise serializers.ValidationError({"password": "Passwords must match"})
        account.set_password(validated_data["password"])
        account.save()
        cart = Cart.objects.create(account=account, state=True).save()
        return account

    class Meta:
        model = Account
        fields = [
            "url",
            "id",
            "firstname",
            "lastname",
            "email",
            "password",
            "password_confirm",
            "address",
        ]


class CartSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cart
        fields = ["url", "id", "account", "state"]


class BookInCartSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BookInCart
        fields = ["url", "id", "cart", "book", "count"]


class BookReviewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BookReview
        fields = ["url", "book", "account", "comment", "date"]
