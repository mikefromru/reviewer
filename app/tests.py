from django.test import TestCase
from .models import UserFile
from django.contrib.auth import get_user_model
from django.test import Client
from django.urls import reverse

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

    def test_count_users(self):
        count = User.objects.all().count()
        self.assertEquals(count, 2)

    # Check authenticated user permission
    def test_get_main_page(self):
        self.client.login(email='admin@gmail.com', password='admin')
        response = self.client.get(reverse('file-list'))
        self.assertEquals(response.status_code, 200)

