from django.urls import path
from . import views

urlpatterns = [
    path('', views.FileListView.as_view(), name='file-list'),
    path('file/<int:pk>/detail/', views.FileDetailView.as_view(), name='file-detail'),

    # path('file/<int:pk>/edit/', views.FileEditView.as_view(), name='file-edit'),
    path('file/<int:pk>/edit/', views.edit_file, name='file-edit'),

    path('file/<int:pk>/delete/', views.FileDeleteView.as_view(), name='file-delete'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    path('register/', views.RegisterForm.as_view(), name='register'),
]