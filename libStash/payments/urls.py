from django.urls import path
from django.conf.urls import url
from payments.views import IndexPageView, stripe_config, create_checkout_session,SuccessView,CancelledView, get_total


urlpatterns = [
    # url paths

    path('', IndexPageView.as_view(), name='index'),
    path('config/', stripe_config, name='stripe-config'),
    path('checkout/', create_checkout_session),
    path('success/', SuccessView.as_view()), 
    path('cancelled/', CancelledView.as_view()), 
    path('get-total/', get_total, name='get-total')
]
