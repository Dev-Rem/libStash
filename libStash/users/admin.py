from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Account, Address, Cart, BookInCart
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

# Register your models here.


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""

    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Password confirmation", widget=forms.PasswordInput
    )

    class Meta:
        model = Account
        fields = ("firstname", "lastname", "email")

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class AccountAdmin(BaseUserAdmin):
    list_display = (
        "firstname",
        "lastname",
        "email",
        "date_joined",
        "last_login",
        "is_admin",
    )
    search_fields = ("firstname", "lastname", "email")
    readonly_fields = ("date_joined", "last_login")
    ordering = ("firstname",)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = (
        (None, {"fields": ("firstname", "lastname", "email", "password")}),
        ("Permissions", {"fields": ("is_active",)}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "firstname",
                    "lastname",
                    "email",
                    "password1",
                    "password2",
                ),
            },
        ),
    )


admin.site.register(Account, AccountAdmin)
admin.site.unregister(Group)


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ("account", "address1", "address2", "zip_code", "country")


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ("account", "state")


@admin.register(BookInCart)
class BookInCartAdmin(admin.ModelAdmin):
    list_display = ("cart", "book", "count")
