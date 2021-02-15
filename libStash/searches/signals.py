from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from django_elasticsearch_dsl.registries import registry


@receiver(post_save)
def update_document(sender, **kwargs):
    """
    Make update to document when changes are made to the Post model.
    """

    app_label = sender._meta.appo_label
    model_name = sender._meta.model_name
    instance = kwargs["instance"]

    """
    Update all Post documents if users.Account is being updated
    users.Account instance is the admin use that created the blog post.
    """
    if app_label == "blogs":
        if model_name == "account":
            instances = instance.post.all()
            for _instance in instances:
                registry.update(_instance)