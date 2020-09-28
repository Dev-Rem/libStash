from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, User
from books.models import Book
from datetime import date

# Create your models here.


class AccountManager(BaseUserManager):
    def create_user(self, firstname, lastname, email, password, password2):
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
    firstname = models.CharField("First name", max_length=200)
    lastname = models.CharField("Last name", max_length=200)
    email = models.EmailField("Email", max_length=100, unique=True)
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
    address1 = models.CharField("Address line 1", max_length=1024)
    address2 = models.CharField("Address line 2", max_length=1024, blank=True)
    zip_code = models.CharField("ZIP / Postal code", max_length=12)
    country = models.CharField("Country", max_length=100)
    last_update = models.DateTimeField(auto_now=True)


class Cart(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    state = models.BooleanField("State", default=False)
    last_update = models.DateTimeField(auto_now=True)


class BookInCart(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    count = models.IntegerField("Book count", default=0)
    last_update = models.DateTimeField(auto_now=True)


class BookReview(models.Model):
    book = models.ForeignKey(Book, null=True, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, null=True, on_delete=models.CASCADE)
    comment = models.CharField(max_length=500, null=True)
    # reply = models.ForeignKey(
    #     "self", null=True, related_name="replies", on_delete=models.CASCADE
    # )
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now=False, auto_now_add=True)
