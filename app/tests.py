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





    # def test_form_upload_file(self):
    #     form = UploadFileForm(data={
    #         'file': 

    #     })
    
    def test_upload_file(self):
        # filename_py = 'test_files/test_upload_file.py' 
        # file = SimpleUploadedFile(filename_py, b'file_content', content_type='text/plain')
        # payload = {'file': file}
        # response = self.client.post(reverse('file-upload'), data=payload, format='multipart', follow=True)
        # print(response.request['PATH_INFO'], ' <<<<<<')
        # self.assertEqual(response.status_code, 200)
        # print(response.request['PATH_INFO'], ' <<<<<<')

        # self.assertRedirects(response, 'app', status_code=200)
        # self.assertRedirects(response, 'app/file/upload/', status_code=200)

        # py_file = open('test_files/test_upload_file.py', 'rb')
        # response = self.client.post(reverse('file-upload'), file={'file': py_file}, follow=True)
        # print(response.request['PATH_INFO'], ' <<<<<<')
        # self.assertRedirects(response, reverse('file-upload'), status_code=200, fetch_redirect_response=False)

        # self.assertEqual(response.status_code, 200)
        pass


    def test_upload_file(self):
        filename_py = open('test_files/test_upload_file.txt', 'rb')
        file_dict = {'file': SimpleUploadedFile(filename_py.name, filename_py.read())}

        # files = {'file': open(filename_py, 'rb')}
        # with open(filename_py, 'rb') as file:
            # data = {'file': file.read()}

        # files = SimpleUploadedFile(filename_py, b'file_content', content_type='text/plain')
        # payload = {'file': file}
        # response = self.client.post(reverse('file-upload'), {'file': files})
        # print(files, ' <<<<<')
        form = UploadFileForm(files=file_dict)
        print(form.errors)
        # self.assertFormError(response, 'form', 'This field is required')
        self.assertTrue(form.is_valid())

        # self.assertEquals(form.errors['recipient'], [u"This field is required"])


        '''
        filename_py = 'test_files/test_upload_file.txt' 
        file_mock = mock.MagicMock(spec=File)
        file_mock.name = filename_py
        file_model = UserFile(file=file_mock)
        print(file_model.file.name, file_mock.name, ' <<<<<')
        self.assertEqual(file_model.file.name, file_mock.name)
        '''


        # filename_txt = 'test_files/test_upload_file.txt' 
        # with open(filename_py, 'rb') as file:
        #     file = file.read()

        # up = UserFile(file=file)
        # self.assertFalse(up)



        '''
            response = self.client.post(reverse('file-upload'), {'file': file})
            self.assertEqual(response.status_code, 200)
        # with open(file)
        '''





    #    data = {'file': filename_py}
    #    file = SimpleUploadedFile(filename_py, b'file_content', content_type='text/x-py')
    #    response = self.client.post(reverse('file-upload'), data=data, follow=True)
    #    self.assertRedirects(response, '/app/file/upload/', status_code=200)
    #    self.assertRedirects(response, expected_url=reverse('file-list'), status_code=302, target_status_code=200)

    #    self.assertRedirects(response, reverse('file-list'), status_code=200)
    #    self.assertEqual(response.status_code, 200)
