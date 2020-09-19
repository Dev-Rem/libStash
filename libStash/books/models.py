from django.db import models
from django.utils.translation import gettext_lazy as _
import datetime
import uuid
from phone_field import PhoneField


# Create your models here.


class Publisher(models.Model):
    name = models.CharField(max_length=150)
    address = models.TextField(max_length=200)
    phone = PhoneField(blank=True, help_text="Contact phone number")
    url = models.URLField()


class Author(models.Model):
    name = models.CharField(max_length=150, null=False)
    phone = PhoneField(blank=True, help_text="Contact phone number")
    address = models.CharField(max_length=150)


class Book(models.Model):
    class Categories(models.TextChoices):
        THRILLER = "THR", _("Thriller")
        FANTASY = "FNSY", _("Fantasy")
        ROMANCE = "RMCE", _("Romance")
        ADVENTURE = "AVTRE", _("Adventure")

    YEAR_CHOICES = []
    for year in range(1980, (datetime.datetime.now().year + 1)):
        YEAR_CHOICES.append((year, year))

    class Formats(models.TextChoices):
        E_BOOK = "E-BK", _("E-Book")
        HARD_COVER = "HD-CVR", _("Hardcover")
        PAPER_BACK = "PPR-BCK", _("Paperback")

    title = models.CharField(max_length=150)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, default=None)
    category = models.CharField(max_length=5, choices=Categories.choices)
    format = models.CharField(max_length=7, choices=Formats.choices)
    isbn = models.CharField(max_length=13)
    year = models.IntegerField(
        _("year"), choices=YEAR_CHOICES, default=datetime.datetime.now().year
    )
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Image(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    book_cover = models.ImageField(upload_to="images/")
    last_update = models.DateTimeField(auto_now=True)


class Warehouse(models.Model):
    # uuid = uuid.uuid4().hex[:6].upper()
    # code = models.AutoField()
    address = models.TextField(max_length=200)
    phone = PhoneField(blank=True, help_text="Contact phone number")


class WarehouseBook(models.Model):
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    count = models.IntegerField()
