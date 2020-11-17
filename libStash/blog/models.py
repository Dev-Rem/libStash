from django.db import models
import uuid
from users.models import Account
from books.models import Book
from libStash import settings
# Create your models here.

class Post(models.Model):
    title = models.CharField('Ttile',max_length=200, unique=True )
    content = models.TextField('Content')
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, db_index=True, unique=True)
    is_active = models.BooleanField('Is Active',default=True)
    account = models.ForeignKey(Account, null=True, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)
    book = models.ForeignKey(Book, null=True, blank=True, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, null=True, on_delete=models.CASCADE)
    comment = models.TextField(verbose_name='Comment', blank=True)
    is_active = models.BooleanField(verbose_name='Is Active', default=True)
    likes = models.ManyToManyField( Account, related_name="like_comment", blank=True)
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, db_index=True, unique=True)
    date = models.DateTimeField( auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.comment

class Image(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True, blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(verbose_name='Image', upload_to='images/')
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, db_index=True, unique=True)
    date = models.DateTimeField( auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.image}"