from django import forms
from django.contrib.auth import get_user_model
from . models import UserFile

from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
)

User = get_user_model()

class UploadFileForm(forms.ModelForm):

    file = forms.FileField(required=True)

    class Meta:
        model = UserFile
        fields = ('id', 'file')
        
class LoginForm(AuthenticationForm):
    ...

class RegisterForm(UserCreationForm):

    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
