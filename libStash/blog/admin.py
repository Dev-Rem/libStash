from django.contrib import admin
from .models import Post, Comment, Image
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", 'is_active', 'date', )

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("post", 'book', "comment", 'is_active', 'date')


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ("post", 'book', "image", 'date', )
