from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.hashers import make_password

from django.conf import settings
from .validators import PhoneValidator

class UserManager(BaseUserManager):
    def _create_user(self, phone, **extra_fields):
        if not phone:
            raise ValueError("The given phone must be set")
        user = self.model(phone=phone, **extra_fields)
        user.save(using=self._db)
        return user

    def create_user(self, phone, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(phone, **extra_fields)

    def create_staff(self, phone, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(phone, **extra_fields)

    def create_superuser(self, phone,  **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(phone, **extra_fields)

class User(AbstractBaseUser):
    phone = models.CharField(
        _("phone"),
        max_length=10,
        unique=True,
        help_text=_(
            "Enter a valid Phone Number."
        ),
        validators = [PhoneValidator],
        error_messages={
            "unique": _("A user with that username already exists."),
        }
    )
    name = models.CharField(_("name"), max_length=150, blank=False)
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    is_superuser = models.BooleanField(
        _("superuser status"),
        default=False,
        help_text=_(
            "Designates that this user has all permissions without "
            "explicitly assigning them."
        ),
    )
    date_joined = models.DateTimeField(_("date_joined"), auto_now_add=True)
    password_created = models.DateTimeField(_('password_created'), auto_now=True)
    objects = UserManager()

    USERNAME_FIELD = 'phone'

    class Meta:
        ordering = ['-date_joined']
    
    def has_perm(self, perm, obj=None):
        return True
