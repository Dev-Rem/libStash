from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
from django.utils.translation import gettext_lazy as _
import datetime, uuid
from phone_field import PhoneField


# Create your models here.




class Publisher(models.Model):
    name = models.CharField(verbose_name="Publisher name", max_length=150)
    address = models.TextField(verbose_name="Address", max_length=200)
    email = models.EmailField(verbose_name='Email', blank=True)
    publisher_url = models.URLField()
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, db_index=True, unique=True)
    last_update = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('publisher-detail', args=[str(self.id)])

    def __str__(self):
        return f"{ self.name }"


class Author(models.Model):
    name = models.CharField(verbose_name="Author name", max_length=150, null=False)
    email = models.EmailField(verbose_name='Email', blank=True)
    address = models.TextField(verbose_name="Address", max_length=150)
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, db_index=True, unique=True)
    last_update = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{ self.name }"


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

    title = models.CharField(verbose_name="Title", max_length=150)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, default=None)
    category = models.CharField(verbose_name="Category", max_length=5, choices=Categories.choices)
    format = models.CharField(verbose_name="Format", max_length=7, choices=Formats.choices)
    isbn = models.CharField(verbose_name="ISBN", max_length=13)
    year = models.IntegerField(
        _("year"), choices=YEAR_CHOICES, default=datetime.datetime.now().year
    )
    price = models.DecimalField(verbose_name="Price", max_digits=10, decimal_places=2, default=0)
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, db_index=True, unique=True)
    last_update = models.DateTimeField("Last Update",auto_now=True)

    def __str__(self):
        return self.title

class Image(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, default=None)
    book_cover = models.ImageField(verbose_name='Book cover', upload_to="images/")
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, db_index=True, unique=True)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.book.id}"

class Warehouse(models.Model):
    address = models.TextField(verbose_name="Address", max_length=200)
    phone = PhoneField(verbose_name="Phone number", blank=True, help_text="Contact phone number")
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, db_index=True, unique=True)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.address}"


class WarehouseBook(models.Model):
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    count = models.IntegerField(verbose_name="Book count", default=0)
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, db_index=True, unique=True)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.book}, {self.count}"
