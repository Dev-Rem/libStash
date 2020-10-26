from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from social_core.backends import stripe
from rest_framework.decorators import api_view
import stripe

# Create your views here.

stripe.api_key = 'sk_test_51HcX1oDC7msJ0hb4JqSnP0b5lH9nhPkn2bBSdgtmrjiCWZ7MhoW5jePPYHJe4BOs1kc8OQ30vcbGARYZlei2AntH00EZ98Dhco'

YOUR_DOMAIN = 'http://localhost:3000/checkout'

@api_view(['POST'])
def test_payment(request):
    test_payment_intent = stripe.PaymentIntent.create(
        amount=1000, currency='pln', 
        payment_method_types=['card'],
        receipt_email='test@example.com')
    return Response(status=status.HTTP_200_OK, data=test_payment_intent)

@api_view(['POST'])
def create_checkout_session(request):
    try:
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'unit_amount': 2000,
                        'product_data': {
                            'name': 'Stubborn Attachments',
                            'images': ['https://i.imgur.com/EHyR2nP.png'],
                        },
                    },
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=YOUR_DOMAIN + '?success=true',
            cancel_url=YOUR_DOMAIN + '?canceled=true',
        )
        return Response({'id': checkout_session.id})
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    pass