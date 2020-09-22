from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, User
from books.models import Book
from datetime import date

# Create your models here.


class AccountManager(BaseUserManager):
    def create_user(self, firstname, lastname, email, password=None):
        if not firstname:
            raise ValueError("Please provide a valid  first name")
        if not lastname:
            raise ValueError("Please provide a valid last name")
        # if not username:
        #     raise ValueError("Please provide a valid user name")
        if not email:
            raise ValueError("Please provide a valid email address")

        user = self.model(
            firstname=firstname,
            # username=username,
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
            # username=username,
            email=self.normalize_email(email),
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True

        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    firstname = models.CharField(verbose_name="first name", max_length=200)
    lastname = models.CharField(verbose_name="last name", max_length=200)
    email = models.EmailField(verbose_name="email", max_length=100, unique=True)
    date_joined = models.DateTimeField(
        verbose_name="date joined", auto_now=False, auto_now_add=True
    )
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

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
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    address1 = models.CharField("Address line 1", max_length=1024)
    address2 = models.CharField("Address line 2", max_length=1024, blank=True)
    zip_code = models.CharField("ZIP / Postal code", max_length=12)
    country = models.CharField("Country", max_length=100)


class Cart(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    last_update = models.DateTimeField()


class CartBook(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    count = models.IntegerField()