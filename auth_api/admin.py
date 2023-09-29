from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.utils.translation import gettext_lazy as _ 

from .models import User

class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (_("Personal info"), {"fields": ("name", "phone", "password")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("phone", "password1", "password2"),
            },
        ),
    )

    list_display = ("phone", "name", "is_staff")
    list_filter = ("is_staff", "is_superuser", "is_active")
    search_fields = ("phone", "name")
    ordering = ("-date_joined",)
    filter_horizontal = []

admin.site.register(User, UserAdmin)

