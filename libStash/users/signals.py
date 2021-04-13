from django.db.models.signals import post_save
from django.dispatch import receiver

from users.models import Account
from books.models import Cart


@receiver([post_save], sender=Account)
def create_cart(sender, instance, created, **kwargs):
    if created:
        Cart.objects.create(account=instance)
        
