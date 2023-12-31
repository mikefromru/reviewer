from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from datetime import datetime

from django.conf import settings

from pathlib import Path
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
import os


class CustomUser(AbstractUser):

    username = models.CharField(max_length=50, blank=True, null=True, unique=True)

    email = models.EmailField(
        _('email adress'), 
        validators=[AbstractUser.username_validator],
        error_messages={'unique': _('User with this Email adress already exists')},
        unique=True,
        )

    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active."
            "Unselect this instead of deleting accounts."

        )
    )

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

def upload_path(instance, filename):
    return f'{instance.user}/{filename}'

class UserFile(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    file = models.FileField(upload_to=upload_path, validators=[FileExtensionValidator(allowed_extensions=['py'])], null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, blank=True)
    modified = models.DateTimeField(auto_now=True, blank=True)
    changed = models.BooleanField(default=False)

    def __str__(self) -> str:
        return str(self.file).split('/')[-1]
