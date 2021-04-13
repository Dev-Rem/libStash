from users.models import Account, Address

from rest_framework import serializers

from djoser.serializers import UserSerializer as BaseUserSerializer


class AddressSerializer(serializers.ModelSerializer):

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
    class Meta:
        model = Account
        fields = ["unique_id", "firstname", "lastname", "email"]


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ["unique_id", "firstname", "lastname", "email"]
