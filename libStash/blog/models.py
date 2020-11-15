from django.db import models
import uuid
from users.models import Account
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True )
    content = models.TextField()
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, db_index=True, unique=True)
    account = models.ForeignKey(Account, null=True, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField(null=True)
    is_active = models.BooleanField(default=True)
    likes = models.ManyToManyField(Account, related_name="like_comment", blank=True)
    date = models.DateTimeField( auto_now_add=True)


class Image(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images/", null=True)
    date = models.DateTimeField(auto_now_add=True)
