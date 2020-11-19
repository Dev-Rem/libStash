from django.http import Http404
from django.contrib.auth.tokens import default_token_generator
from api.serializers import AddressSerializer, BookInCartSerializer, CartSerializer 
from rest_framework.response import Response
from rest_framework import status, generics, permissions,viewsets
from djoser.conf import settings
from djoser import signals, utils
from djoser.compat import get_user_email
from djoser.views import UserViewSet
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from libStash import settings as project_settings
from users.models import Account, Address
from djoser.serializers import UserSerializer
CACHE_TTL = getattr(project_settings, 'CACHE_TTL')


# Create your views here.

class AddressListView(generics.ListCreateAPIView):
    """
    GET: Returns all address instances associated with the logged in user
    POST: Create new address object.
    """

    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'unique_id'

    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(CACHE_TTL))
    def list(self, request, *args, **kwargs):
        address = Address.objects.filter(account=request.user).order_by('-last_update')
        serializer = AddressSerializer(address, many=True)
        return Response(serializer.data)


    def create(self, request, *args, **kwargs):
        serializer = AddressSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['account'] = request.user
            serializer.save()
            return Response({'status': 'Address Created'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AddressUpdateView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET: Returns an address instance
    PUT: Updates the address instance
    """

    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'unique_id'

    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(CACHE_TTL))
    def retrieve(self, request, *args, **kwargs):
        address = Address.objects.get(account=request.user, pk=kwargs['unique_id'])
        serializer = AddressSerializer(address)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        address = Address.objects.get(account=request.user, pk=kwargs['unique_id'])
        serializer = AddressSerializer(address, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'Address Updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def destroy(self, request, *args, **kwargs):
        address = Address.objects.get(account=request.user, pk=kwargs['unique_id'])
        address.delete()
        return Response({'status': 'Address Deleted'})    

class UserViewSet(UserViewSet):
    serializer_class = UserSerializer
    queryset = Account.objects.all()
    permission_classes = settings.PERMISSIONS.user
    token_generator = default_token_generator
    lookup_field = 'unique_id'
    
    def perform_create(self, serializer):
        user = serializer.save()
        cart = Cart.objects.create(account=user, is_active=True)
        cart.save()
        signals.user_registered.send(
            sender=self.__class__, user=user, request=self.request
        )

        context = {"user": user}
        to = [get_user_email(user)]
        if settings.SEND_ACTIVATION_EMAIL:
            settings.EMAIL.activation(self.request, context).send(to)
        elif settings.SEND_CONFIRMATION_EMAIL:
            settings.EMAIL.confirmation(self.request, context).send(to)

