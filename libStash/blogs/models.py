import uuid

from django.db import models
from django.utils.translation import ugettext_lazy as _
from users.models import Account

# Create your models here.


class Post(models.Model):
    """A model for the creating blog posts."""

    title = models.CharField(_("title"), max_length=1024, unique=True)
    content = models.TextField(_("content"))
    likes = models.ManyToManyField(
        Account, related_name="like_post", blank=True, default=[0]
    )
    unique_id = models.UUIDField(
        _("unique id"), default=uuid.uuid4, editable=False, db_index=True, unique=True
    )
    is_active = models.BooleanField(_("Is Active"), default=True)
    account = models.ForeignKey(
        Account, null=True, on_delete=models.CASCADE, verbose_name=_("account")
    )
    date = models.DateTimeField(_("date"), auto_now_add=True)
    last_update = models.DateTimeField(_("last update"), auto_now=True)

    class Meta:
        db_table = "post"


class PostImage(models.Model):
    """A model for the Post images"""

    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="postImage", verbose_name=_("post")
    )
    image = models.ImageField(verbose_name=_("Image"))
    unique_id = models.UUIDField(
        _("unique id"), default=uuid.uuid4, editable=False, db_index=True, unique=True
    )
    date = models.DateTimeField(_("date"), auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "post_image"

    @property
    def post_indexing(self):
        """Post for indexing. Used in Elasticsearch indexing."""
        if self.post is not None:
            return self.post.id

    @property
    def image_indexing(self):
        """Post indexing. Used in Elasticsearch indexing."""
        if self.image is not None:
            return [{"id": self.id, "image": self.image.url}]


class PostComment(models.Model):
    """A model for the Post comments"""

    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="postComment",
        verbose_name=_("post"),
    )
    account = models.ForeignKey(
        Account, null=True, on_delete=models.CASCADE, verbose_name=_("account")
    )
    comment = models.TextField(verbose_name=_("comment"))
    unique_id = models.UUIDField(
        _("unique id"), default=uuid.uuid4, editable=False, db_index=True, unique=True
    )
    date = models.DateTimeField(_("date"), auto_now_add=True)
    last_update = models.DateTimeField(_("last update"), auto_now=True)

    class Meta:
        db_table = "post_comment"

    def __str__(self):
        return self.comment

    @property
    def post_indexing(self):
        """Post indexing. Used in Elasticsearch indexing."""
        if self.post is not None:
            return self.post.id

    @property
    def account_indexing(self):
        """Account indexing. Used in Elasticsearch indexing"""
        if self.account is not None:
            return self.account.id