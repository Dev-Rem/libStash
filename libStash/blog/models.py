from django.db import models
import uuid
from users.models import Account
from libStash import settings
# Create your models here.

class Post(models.Model):
    title = models.CharField('Ttile',max_length=200, unique=True )
    content = models.TextField('Content')
    likes = models.ManyToManyField( Account, related_name="like_post", blank=True, default=0)
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, db_index=True, unique=True)
    is_active = models.BooleanField('Is Active',default=True)
    account = models.ForeignKey(Account, null=True, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title

class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image = models.ImageField(verbose_name='Image')
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, db_index=True, unique=True)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.image

class PostComment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, null=True, on_delete=models.CASCADE)
    comment = models.TextField(verbose_name='Comment')
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, db_index=True, unique=True)
    date = models.DateTimeField( auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.comment
