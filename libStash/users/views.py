from api.serializers import (AddressSerializer, BookInCartSerializer,
                             CartSerializer, UserSerializer)
from books.models import Cart
from decouple import config
from django.contrib.auth.tokens import default_token_generator
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from djoser import signals, utils
from djoser.conf import settings
from djoser.views import UserViewSet
from rest_framework import generics, permissions, status, viewsets
from rest_framework.response import Response
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Email, Mail, Personalization, To
from users.models import Account, Address

CACHE_TTL = int(config("CACHE_TTL"))


# Create your views here.


class AddressListView(generics.ListCreateAPIView):
    """
    GET: Returns all address instances associated with the logged in user
    POST: Create new address object.
    """

    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = "unique_id"

    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(CACHE_TTL))
    def list(self, request, *args, **kwargs):
        address = Address.objects.get(account=request.user)
        serializer = AddressSerializer(address)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = AddressSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data["account"] = request.user
            serializer.save()
            return Response({"status": "Address Created"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AddressUpdateView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET: Returns an address instance
    PUT: Updates the address instance
    DELETE: Delete an address instance
    """

    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = "unique_id"

    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(CACHE_TTL))
    def retrieve(self, request, *args, **kwargs):
        address = Address.objects.get(
            account=request.user, unique_id=kwargs["unique_id"]
        )
        serializer = AddressSerializer(address)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        address = Address.objects.get(
            account=request.user, unique_id=kwargs["unique_id"]
        )
        serializer = AddressSerializer(address, data=request.data)
        if serializer.is_valid():
            message = Mail(
                from_email=config("DEFAULT_FROM_EMAIL"),
                to_emails=To(f"{request.user}"),
                subject="Address Update",
                html_content=f"<p> Hello {request.user}, your address was successful updated.</p>  <br> <p> From LibStash, we wish you a wonderful time on our web page.</p>",
            )
            try:
                sg = SendGridAPIClient(config("SENDGRID_API_KEY"))
                sg.send(message)
            except Exception as e:
                print(e)
            serializer.save()
            return Response({"status": "Address Updated"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        address = Address.objects.get(
            account=request.user, unique_id=kwargs["unique_id"]
        )
        address.delete()
        message = Mail(
            from_email=config("DEFAULT_FROM_EMAIL"),
            to_emails=To(f"{request.user}"),
            subject="Address Delete",
            html_content=f"<p> Hello {request.user}, it seems you deleted your shipping address. <br> We strongly advice that you add a shipping addres to your account to ensure safe delivevry of your orders.</p> <br> <p> From LibStash, we wish you a wonderful time on our web page.</p>",
        )
        try:
            sg = SendGridAPIClient(config("SENDGRID_API_KEY"))
            sg.send(message)
        except Exception as e:
            print(e)
        return Response({"status": "Address Deleted"})


class UserViewSet(UserViewSet):
    serializer_class = UserSerializer
    queryset = Account.objects.all()
    permission_classes = settings.PERMISSIONS.user
    token_generator = default_token_generator
    lookup_field = "unique_id"

    def perform_create(self, serializer):
        user_email = serializer.validated_data["email"]

        message = Mail(
            from_email=config("DEFAULT_FROM_EMAIL"),
            to_emails=To(f"{user_email}"),
            subject="Account registration complete",
            html_content=f"<p> Hello {user_email}, your account registration was successful.</p> <br> <p> From LibStash, we wish you a wonderful time on our web page.</p>",
        )
        try:
            sg = SendGridAPIClient(config("SENDGRID_API_KEY"))
            sg.send(message)
        except Exception as e:
            print(e)

        user = serializer.save()
        cart = Cart.objects.create(account=user, is_active=True)
        cart.save()

    def perform_update(self, serializer):
        super().perform_update(serializer)
        user = serializer.instance

        message = Mail(
            from_email=config("DEFAULT_FROM_EMAIL"),
            to_emails=To(f"{user}"),
            subject="Account Update",
            html_content=f"<p> Hello {user}, this mail is to inform you about your account information update.</p> <br> <p> From LibStash, we wish you a wonderful time on our web page.</p>",
        )
        try:
            sg = SendGridAPIClient(config("SENDGRID_API_KEY"))
            sg.send(message)
        except Exception as e:
            print(e)
