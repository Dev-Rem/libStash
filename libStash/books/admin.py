from django.contrib import admin
from .models import Book, Image, Author, Publisher

# Register your models here.

admin.site.register(Book)
admin.site.register(Image)
admin.site.register(Author)
admin.site.register(Publisher)
