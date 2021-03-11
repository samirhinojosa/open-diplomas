from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext as _
from apps.core.models import User
from apps.core.forms import MyUserCreationForm, MyUserChangeForm


class MyUserAdmin(UserAdmin):
    """
    Django admin to Users (customizing authentication user)
    """
    add_form = MyUserCreationForm
    form = MyUserChangeForm
    model = User
    list_display = [
        "email", "first_name", "last_name", "is_staff"
    ]
    list_display_links = [
        "email"
    ]
    search_fields = [
        "email", "first_name", "last_name"
    ]
    fieldsets = [
        ("Access info", {
            "fields": ("email", "password")
        }),
        ("Personal info", {
            "fields": ("first_name", "last_name")
        }),
        ("Permissions", {
            "fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")
        }),
        ("Important dates", {
            "fields": ("last_login", "date_joined")
        }),
    ]
    add_fieldsets = [
        ("Access info", {
            "classes": ("wide",),
            "fields": ("email", "password1", "password2"),
        }),
    ]
    ordering = [
        "email"
    ]