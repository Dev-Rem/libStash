from django.contrib import admin
from .models import Post, Comment, Image
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "account", 'is_active', 'date', )

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("post", "comment", 'is_active', 'date')


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ("post", "image", 'date', )
