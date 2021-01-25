import json

import stripe
from books.models import Book, BookInCart, Cart
from decouple import config
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.views.generic.base import TemplateView
from users.models import Account

# Create your views here.

stripe.api_key = config("STRIPE_SECRET_KEY")


class IndexView(TemplateView):
    template_name = "index.html"


class SuccessView(TemplateView):
    template_name = "success.html"


class CancelledView(TemplateView):
    template_name = "cancelled.html"


# calculate order total
@csrf_exempt
def get_amount(request):
    if request.method == "GET":
        total = 0
        account = Account.objects.get(email=request.user)
        cart = Cart.objects.get(account=account)
        cart_items = BookInCart.objects.filter(cart=cart)
        serialized_data = serializers.serialize("json", cart_items)
        objects = json.loads(serialized_data)
        for item in objects:
            sub_total = item["fields"]["quantity"] * item["fields"]["amount"]
            total += sub_total
        return total * 100


@csrf_exempt
def checkout(request):
    if request.method == "GET":
        domain_url = config("DOMAIN_URL")
        try:
            item_amount = get_amount(request)
            account = Account.objects.get(email=request.user)
            if account.stripe_id == None:
                customer = stripe.Customer.create(
                    email=account.email,
                    name=f"{account.firstname} {account.lastname}",
                )
                account.stripe_id = customer.id
                account.save()
            else:
                customer = stripe.Customer.retrieve(account.stripe_id)
            checkout_session = stripe.checkout.Session.create(
                client_reference_id=request.user.unique_id
                if request.user.is_authenticated
                else None,
                success_url=domain_url
                + "payment/success?session_id={CHECKOUT_SESSION_ID}",
                cancel_url=domain_url + "payment/cancelled/",
                payment_method_types=["card"],
                customer=customer.id,
                mode="payment",
                line_items=[
                    {
                        "name": "LibStash test payment",
                        "amount": int(item_amount),
                        "quantity": 1,
                        "currency": "usd",
                    }
                ],
            )
            return JsonResponse({"sessionId": checkout_session["id"]})
        except Exception as e:
            return JsonResponse({"error": str(e)})


@csrf_exempt
def stripe_config(request):
    if request.method == "GET":
        stripe_config = {"publicKey": config("STRIPE_PUBLISHABLE_KEY")}
        return JsonResponse(stripe_config, safe=False)


@csrf_exempt
def stripe_webhook(request):
    endpoint_secret = config("STRIPE_ENDPOINT_SECRET")
    payload = request.body.decode("utf-8")
    sig_header = request.META["HTTP_STRIPE_SIGNATURE"]
    event = None

    try:
        event = stripe.Webhook.construct_event(payload, sig_header, endpoint_secret)
    except ValueError as e:
        # Invalid payload
        print("invalid payload")
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        print("invalid signature")
        return HttpResponse(status=400)

    # Handle the checkout.session.completed event and delete cart items
    if event["type"] == "checkout.session.completed":
        payload = json.loads(payload)
        account = Account.objects.get(
            unique_id=payload["data"]["object"]["client_reference_id"]
        )
        cart = Cart.objects.get(account=account)
        cart_items = BookInCart.objects.filter(cart=cart)
        cart_items.delete()
    return HttpResponse(status=200)
