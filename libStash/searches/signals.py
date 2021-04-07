from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from django_elasticsearch_dsl.registries import registry


@receiver([post_save])
def update_document(sender, instance, **kwargs):
    model_name = sender._meta.model_name
    print(model_name)

    if model_name == "postimage":
        registry.update(instance)

    if model_name == "postcomment":
        registry.update(instance)


@receiver([post_delete])
def delete_document(sender, **kwargs):
    model_name = sender._meta.model_name
    instance = kwargs["instance"]
    print(model_name)

    if model_name == "postimage":
        registry.delete(instance)

    if model_name == "postcomment":
        registry.delete(instance)
