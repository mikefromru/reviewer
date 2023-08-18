from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
# Create your models here.

class CustomUser(AbstractUser):

    username = None
    '''    
    username = models.CharField(
        _('username'),
        max_length=150,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[AbstractUser.username_validator],
        error_messages={'unique': _('User with this username already exists')},
        null=True,
        blank=True,
    )
    '''

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


    USERNAME_FIELD = "email"
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []
