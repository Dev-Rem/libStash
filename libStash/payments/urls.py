from django.urls import path
from payments.views import (CancelledView, IndexView, SuccessView, checkout,
                            stripe_config, stripe_webhook)

urlpatterns = [
    # url paths
    path("", IndexView.as_view(), name="index"),
    path("config/", stripe_config, name="stripe-config"),
    path("checkout/", checkout, name="checkout"),
    path("success/", SuccessView.as_view(), name="success"),
    path("cancelled/", CancelledView.as_view()),
    path("webhook/", stripe_webhook, name="webhook"),
]
