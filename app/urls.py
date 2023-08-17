from django.urls import path
from . import views

urlpatterns = [
    path('', views.foo, name='index'),
    path('register/', views.signup, name='signup'),
]