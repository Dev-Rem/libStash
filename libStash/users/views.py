from users.serializers import AddressSerializer, UserSerializer
from users.models import Account, Address
from books.serializers import CartSerializer, BookInCartSerializer
from books.models import Cart
from libStash.settings.base import SENDGRID_API_KEY, DEFAULT_FROM_EMAIL

from permission import IsOwner

from decouple import config
from django.contrib.auth.tokens import default_token_generator
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from django.template.loader import render_to_string

from djoser import signals, utils
from djoser.conf import settings
from djoser.views import UserViewSet

from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_201_CREATED,
    HTTP_200_OK,
    HTTP_204_NO_CONTENT,
)
from rest_framework.response import Response


CACHE_TTL = int(config("CACHE_TTL"))


# Create your views here.


class AddressCreateView(CreateAPIView):
    """POST: Create new address object."""

    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = AddressSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data["account"] = request.user
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class AddressUpdateView(RetrieveUpdateDestroyAPIView):
    """
    GET: Returns an address instance
    PUT: Updates the address instance
    DELETE: Delete an address instance
    """

    serializer_class = AddressSerializer
    permission_classes = [IsOwner]
    lookup_field = "unique_id"

    def get_queryset(self):
        return Address.objects.get(acccount=self.request.user)

    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(CACHE_TTL))
    def retrieve(self, request, *args, **kwargs):
        try:
            address = self.get_queryset()
            serializer = AddressSerializer(address)
            return Response(serializer.data, status=HTTP_200_OK)
        except Exception:
            return Response(status=HTTP_404_NOT_FOUND)

    def update(self, request, *args, **kwargs):
        address = self.get_queryset()
        serializer = AddressSerializer(address, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        try:
            address = self.get_queryset()
            address.delete()
            return Response(status=HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response(e, status=HTTP_400_BAD_REQUEST)


class UserViewSet(UserViewSet):

    serializer_class = UserSerializer
    queryset = Account.objects.all()
    permission_classes = settings.PERMISSIONS.user
    token_generator = default_token_generator
    lookup_field = "unique_id"
