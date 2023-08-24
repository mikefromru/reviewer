from django import forms
from django.core import validators
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.contrib.auth import authenticate, login

from django.contrib.auth import get_user_model
User = get_user_model()

from . models import UserFile

class EditFileForm(forms.Form):

    # file = forms.CharField(widget=forms.Textarea)
    file = forms.Textarea()
    # file = forms.FileField()

    # class Meta:
        # model = UserFile
        # fields = ('id', 'file')

class LoginForm(AuthenticationForm):
    ...

class RegisterForm(UserCreationForm):

    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')

