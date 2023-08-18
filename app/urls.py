from django.urls import path
from . import views

urlpatterns = [
    path('', views.foo, name='index'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.RegisterForm.as_view(), name='register'),
]