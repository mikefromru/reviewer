from django.test import TestCase
from .models import UserFile
from django.contrib.auth import get_user_model
from django.test import Client
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile

from .forms import UploadFileForm
from django.core.files import File

from unittest import mock

User = get_user_model()

class TestUserFile(TestCase):

    def setUp(self):
        self.client = Client()
        self.user_1 = User.objects.create_user(
            id=1,
            username='username_admin',
            email='admin@gmail.com',
            password='admin',
        )

        self.user_2 = User.objects.create_user(
            id=2,
            username='valera',
            email='valera@gmail.com',
            password='valera',
        )

        self.client.login(email='admin@gmail.com', password='admin')

    def test_count_users(self):
        count = User.objects.all().count()
        self.assertEquals(count, 2)

    # Check authenticated user permission
    def test_get_main_page(self):
        response = self.client.get(reverse('file-list'))
        self.assertEquals(response.status_code, 200)

    def test_upload_allowed_file(self):
        filename_py = open('test_files/test_upload_file.py', 'rb')
        upload_file = {'file': SimpleUploadedFile(filename_py.name, filename_py.read())}
        form = UploadFileForm(files=upload_file)
        # print(form.errors)
        self.assertTrue(form.is_valid())

    def test_upload_not_allowed_file(self):
        filename_py = open('test_files/test_upload_file.txt', 'rb')
        upload_file = {'file': SimpleUploadedFile(filename_py.name, filename_py.read())}
        form = UploadFileForm(files=upload_file)
        self.assertFalse(form.is_valid())
