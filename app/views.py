from django.shortcuts import render
from django.http import HttpResponse
from . forms import SignUpForm

def foo(request):
    return HttpResponse('Hellow World')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Welcome a new user')
    else:
        form = SignUpForm()
        return render(request, 'auth/signup.html', {'form': form})

