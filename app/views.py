from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import logout
from . forms import RegisterForm, LoginForm
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
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
    success_message = 'Вы успешно зарегистрировались. Можете войти на сайт!'

    def form_valid(self, form):
        """If the form is valid, send an email and then save the form."""
        # return HttpResponse('fuck you motherfucker')
        # send_mail(
        #     "Subject here",
        #     "Here is the message.",
        #     "from@example.com",
        #     ["to@example.com"],
        #     fail_silently=False,
        # )
        # return super(BookingRequestView, self).form_valid(form)
        return super(RegisterForm, self).form_valid(form)

class UserLogoutView(LogoutView):
    next_page = reverse_lazy('login') 