from django.db import models
from django.utils.translation import gettext_lazy as _
import datetime, uuid
from phone_field import PhoneField
from users.models import Account

# Create your models here.


class Publisher(models.Model):
    name = models.CharField(verbose_name="Publisher name", max_length=150)
    address = models.TextField(verbose_name="Address", max_length=200)
    email = models.EmailField(verbose_name="Email", blank=True)
    publisher_url = models.URLField()
    unique_id = models.UUIDField(
        default=uuid.uuid4, editable=False, db_index=True, unique=True
    )
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{ self.name }"


class Author(models.Model):
    name = models.CharField(verbose_name="Author name", max_length=150, null=False)
    email = models.EmailField(verbose_name="Email", blank=True)
    address = models.TextField(verbose_name="Address", max_length=150)
    bio = models.TextField("Biography", null=True, blank=True)
    unique_id = models.UUIDField(
        default=uuid.uuid4, editable=False, db_index=True, unique=True
    )
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
    author = models.ManyToManyField(Author, related_name="book_author")
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, default=None)
    category = models.CharField(
        verbose_name="Category", max_length=5, choices=Categories.choices
    )
    format = models.CharField(
        verbose_name="Format", max_length=7, choices=Formats.choices
    )
    isbn = models.CharField(verbose_name="ISBN", max_length=13)
    year = models.IntegerField(
        _("year"), choices=YEAR_CHOICES, default=datetime.datetime.now().year
    )
    price = models.IntegerField(verbose_name="Price", default=0)
    unique_id = models.UUIDField(
        default=uuid.uuid4, editable=False, db_index=True, unique=True
    )
    last_update = models.DateTimeField("Last Update", auto_now=True)

    def __str__(self):
        return self.title


class Warehouse(models.Model):
    address = models.TextField(verbose_name="Address", max_length=200)
    phone = PhoneField(verbose_name="Phone number", blank=True)
    unique_id = models.UUIDField(
        default=uuid.uuid4, editable=False, db_index=True, unique=True
    )
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.address}"


class WarehouseBook(models.Model):
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    count = models.IntegerField(verbose_name="Book count", default=0)
    unique_id = models.UUIDField(
        default=uuid.uuid4, editable=False, db_index=True, unique=True
    )
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.book}, {self.count}"


class BookImage(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    image = models.ImageField(verbose_name="Image")
    unique_id = models.UUIDField(
        default=uuid.uuid4, editable=False, db_index=True, unique=True
    )
    last_update = models.DateTimeField(auto_now=True)


class BookComment(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, null=True, on_delete=models.CASCADE)
    comment = models.TextField(verbose_name="Comment")
    unique_id = models.UUIDField(
        default=uuid.uuid4, editable=False, db_index=True, unique=True
    )
    date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return self.comment


class Cart(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    is_active = models.BooleanField(verbose_name="State", default=False)
    unique_id = models.UUIDField(
        default=uuid.uuid4, editable=False, db_index=True, unique=True
    )
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Cart for " + str(self.account)


class BookInCart(models.Model):
    cart = models.ForeignKey(
        Cart, on_delete=models.CASCADE, related_name="item_in_cart"
    )
    book = models.ForeignKey(
        Book, on_delete=models.CASCADE, related_name="book_in_cart"
    )
    quantity = models.IntegerField(verbose_name="Book count", default=0)
    unique_id = models.UUIDField(
        default=uuid.uuid4, editable=False, db_index=True, unique=True
    )
    amount = models.IntegerField(verbose_name="Book unit amount", default=0)
    last_update = models.DateTimeField(auto_now=True)
