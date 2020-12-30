import stripe
from rest_framework.utils import json
from rest_framework.response import Response
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.generic.base import TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect, render
from django.urls import reverse
from django.core import serializers
from users.models import  Account
from books.models import Cart, BookInCart, Book
from decouple import config

# Create your views here.

stripe.api_key = config('STRIPE_SECRET_KEY')

class IndexPageView(TemplateView):
    template_name = 'index.html'


class SuccessView(TemplateView):
    template_name = 'success.html'


class CancelledView(TemplateView):
    template_name = 'cancelled.html'

def get_total(request):
    if request.method == 'GET':
        account = Account.objects.get(email=request.user)
        cart = Cart.objects.get(account=account)
        cart_items = BookInCart.objects.filter(cart=cart)
        cart_items_list = [cart_items.values()]
        print(cart_items_list)
        total = 0
        for item in cart_items_list:
            sub_total = item['fields']['quantity'] * item['fields']['amount']
            total += sub_total
        
        return HttpResponse(serializers.serialize('json', cart_items))

@csrf_exempt
def create_checkout_session(request):
    if request.method == 'GET':
        domain_url = config('DOMAIN_URL')
        try:     
            account = Account.objects.get(email=request.user)   
            if type(account.stripe_id) == str:
                customer = stripe.Customer.retrieve(account.stripe_id)
            else:
                customer = stripe.Customer.create(
                    email = request.user,
                    name = f'{request.user.firstname} {request.user.lastname}',
                )

                account.stripe_id = customer.id
                account.save()
            checkout_session = stripe.checkout.Session.create(
                success_url=domain_url + 'success?session_id={CHECKOUT_SESSION_ID}',
                cancel_url=domain_url + 'cancelled/',
                payment_method_types=['card'],
                customer=customer,
                mode='payment',

            )
            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as e:
            return JsonResponse({'error': str(e)})

@csrf_exempt
def stripe_config(request):
    if request.method == 'GET':
        stripe_config = {'publicKey': config('STRIPE_PUBLISHABLE_KEY')}
        return JsonResponse(stripe_config, safe=False)



@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    event = None

    try:
        event = stripe.Event.construct_from(
        json.loads(payload), stripe.api_key
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)

    # Handle Stripe events
    if event.type == 'payment_intent.succeeded':
        payment_intent = event.data.object 
        print('PaymentIntent was successful!')
    elif event.type == 'payment_method.attached':
        payment_method = event.data.object 
        print('PaymentMethod was attached to a Customer!')
    elif event.type == 'checkout.session.completed':
        payment_method = event.data.object 
        print('Payment checkout complete!')
    else:
        print('Unhandled event type {}'.format(event.type))

    return HttpResponse(status=200)
