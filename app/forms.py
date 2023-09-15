from django import forms
from django.core import validators
from django.core.exceptions import ValidationError

import pathlib

from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
)

from django.contrib.auth import authenticate, login

from django.contrib.auth import get_user_model
User = get_user_model()

from . models import UserFile
from django.core.validators import FileExtensionValidator
from django.core.exceptions import NON_FIELD_ERRORS

def validate_file_extension(value):
    if not value.name.endswith('.py'):
        raise ValidationError('Error message')

class UploadFileForm(forms.ModelForm):

    file = forms.FileField(required=True)

    class Meta:
        model = UserFile
        fields = ('id', 'file')

        # error_messages = {
        #     'name': {
        #         'message': 'you have to user'
        #     }
        # }

    # def clean(self):
    #     # super(UploadFileForm, self).clean()
    #     filename = self.cleaned_data.get('file')
    #     if pathlib.Path(str(filename)) != '.py':
    #         print('fuck it')
    #         # raise ValidationError('It must to be Python file')
    #    #return filename

        
class LoginForm(AuthenticationForm):
    ...

class RegisterForm(UserCreationForm):

    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
