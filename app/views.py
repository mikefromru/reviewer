from django.shortcuts import render, redirect
from django.contrib.auth import logout
from . forms import RegisterForm, LoginForm
from django.contrib.auth import views as auth_views
from django.views import generic
from django.urls import reverse_lazy

def foo(request):
    return render(request, 'app/index.html')

class LoginView(auth_views.LoginView):

    form_class = LoginForm
    template_name = 'auth/login.html'

class RegisterForm(generic.CreateView):

    form_class = RegisterForm
    template_name = 'auth/signup.html' 
    success_url = reverse_lazy('login')

def logout_view(request):
    logout(request)
    return redirect('/app/login')