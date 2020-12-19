import stripe
from django.shortcuts import redirect, render
from rest_framework.response import Response
from rest_framework import status
from social_core.backends import stripe
from rest_framework.decorators import api_view
from django.views.generic.base import TemplateView
from django.conf import settings
from django.http.response import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.utils import json
from decouple import config
from books.models import BookInCart, Cart
from stripe.api_resources import checkout

# Create your views here.

stripe.api_key = 'sk_test_51HcX1oDC7msJ0hb4JqSnP0b5lH9nhPkn2bBSdgtmrjiCWZ7MhoW5jePPYHJe4BOs1kc8OQ30vcbGARYZlei2AntH00EZ98Dhco'


class CheckoutView(TemplateView):
    template_name = 'checkout.html'

class SuccessView(TemplateView):
    template_name = 'success.html'

class CancelView(TemplateView):
    template_name = 'cancel.html'

@csrf_exempt
def stripe_config(request):
    if request.method == 'GET':
        stripe_config = {'publicKey': settings.STRIPE_PUBLISHABLE_KEY}
        return JsonResponse(stripe_config, safe=False)

@csrf_exempt
def create_checkout_session(request):
    if request.method == 'GET': 
        domain_url = config('DOMAIN_URL')
        stripe.api_key = settings.STRIPE_SECRET_KEY
        try:
            checkout_session = stripe.checkout.Session.create(
                success_url=domain_url + 'checkout/success/?session_id={CHECKOUT_SESSION_ID}',
                cancel_url=domain_url + 'checkout/cancel/',
                payment_method_types=['card'],
                mode='payment',
                line_items=[
                    {
                        'name': 'Book',
                        'quantity': 2,
                        'currency': 'usd',
                        'amount': '2000',
                    }
                ]
            )
            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as e:
            return JsonResponse({'error': str(e)})



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
