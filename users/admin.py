from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model

from allauth.account.models import EmailAddress

from . import forms

User = get_user_model()


class EmailAddressInline(admin.TabularInline):
    model = EmailAddress
    extra = 1


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    add_form = forms.UserCreationForm
    form = forms.UserChangeForm
    inlines = [
        EmailAddressInline,
    ]
