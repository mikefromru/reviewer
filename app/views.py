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
from . forms import UploadFileForm
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


def edit_file(request, pk):
    queryset = UserFile.objects.get(pk=pk)
    with open('media/'+ str(request.user) + '/'  + str(queryset), 'r') as f:
        file_content = f.read()

    if request.method == 'GET':
        return render(request, 'app/file-edit.html', {'file_content': file_content, 'pk': pk})

    if request.method == 'POST':
        with open('media/'+ str(request.user) + '/'  + str(queryset), 'w') as f:
            update_file = request.POST['new']
            f.write(update_file)

        return redirect('file-list')
        # return HttpResponse(file, content_type='text/plain')

class UploadFileView(View):

    form_class = UploadFileForm
    template_name = 'app/file-upload.html'
    # success_url = reverse_lazy

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        print(request.FILES)
        if form.is_valid:
            new_file = UserFile(file=request.FILES['file'])
            new_file.user = request.user
            new_file.save()
            return redirect('file-list')
        else:
            return HttpResponse('Something went wrong !')

class FileListView(LoginRequiredMixin, generic.ListView):
    
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
