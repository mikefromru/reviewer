from typing import Any
from django.db import models
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import logout
from . forms import RegisterForm, LoginForm
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from django.views import generic
from django.urls import reverse_lazy
from . models import UserFile
from . forms import EditFileForm
from django.http import HttpResponse
from django.views import View



def edit_file(request, pk):

    queryset = UserFile.objects.get(pk=pk)
    # '''
    with open('media/' + str(queryset), 'r') as f:
        # file_content = f.read()
        file_content = f.read()
    # '''

    # form = EditFileForm('file_content kekekeklsek kekekekek')
    # return render(request, 'app/file-edit.html', {'form': form})

    return render(request, 'app/file-edit.html', {'file_content': file_content})
    # return render(request, 'app/file-edit.html', {'file_content': file_content}, content_type='text/plain')
    # return HttpResponse(file_content, content_type='text/plain')



# class FileEditView(generic.UpdateView):
class FileEditView(View):

    # model = UserFile
    # form_class = EditFileForm
    # success_url = reverse_lazy('file-list')
    # template_name = 'app/file-edit.html'

    # fields = ['file']

    # def get_queryset(self):
        # return self.model.objects.filter(user=self.request.user)

    def get(self, request, pk):
        form = EditFileForm()
        return render(request, 'app/file-edit.html', {'form': form})




class FileListView(generic.ListView):
    
    model = UserFile
    template_name = 'app/file-list.html'

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)


class FileDetailView(generic.DetailView):

    model = UserFile
    template_name = 'app/file-detail.html'


class FileDeleteView(generic.DeleteView):

    model = UserFile
    success_url = reverse_lazy('file-list')
    template_name = 'app/file-detail.html'


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