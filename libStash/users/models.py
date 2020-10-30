from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, User
from books.models import Book
from datetime import date
import uuid

# Create your models here.


class AccountManager(BaseUserManager):
    def create_user(self, firstname, lastname, email, password=None):
        if not firstname:
            raise ValueError("Please provide a valid  first name")
        if not lastname:
            raise ValueError("Please provide a valid last name")
        if not email:
            raise ValueError("Please provide a valid email address")

        user = self.model(
            firstname=firstname,
            lastname=lastname,
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, firstname, lastname, email, password):
        user = self.create_user(
            firstname=firstname,
            lastname=lastname,
            email=self.normalize_email(email),
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True

        user.save(using=self._db)
        return user

class Account(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    firstname = models.CharField(verbose_name="First name", max_length=200)
    lastname = models.CharField(verbose_name="Last name", max_length=200)
    email = models.EmailField(verbose_name="Email", max_length=100, unique=True)
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, db_index=True, unique=True)
    date_joined = models.DateTimeField(
        verbose_name="date joined", auto_now=False, auto_now_add=True
    )
    last_login = models.DateTimeField(verbose_name="Last login", auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    last_update = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["firstname", "lastname"]
    objects = AccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

class Address(models.Model):
    account = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        null=True,
        related_name="address",
    )
    address1 = models.CharField(verbose_name="Address line 1", max_length=1024)
    address2 = models.CharField(verbose_name="Address line 2", max_length=1024, blank=True)
    zip_code = models.CharField(verbose_name="ZIP / Postal code", max_length=12)
    city = models.CharField(verbose_name='City', max_length=1024, null=True, blank=True)
    country = models.CharField(verbose_name="Country", max_length=100)
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, db_index=True, unique=True)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Address for ' + str(self.account)

class Cart(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    is_active = models.BooleanField(verbose_name="State", default=False)
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, db_index=True, unique=True)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Cart for ' + str(self.account)

class BookInCart(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='item_in_cart')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='book_in_cart')
    count = models.IntegerField(verbose_name="Book count", default=0)
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, db_index=True, unique=True)
    last_update = models.DateTimeField(auto_now=True)

class BookReview(models.Model):
    book = models.ForeignKey(Book, null=True, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, null=True, on_delete=models.CASCADE)
    comment = models.CharField(verbose_name='Comment', max_length=500, null=True)
    is_active = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now=False, auto_now_add=True)
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, db_index=True, unique=True)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment