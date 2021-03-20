from django.test import TestCase
from rest_framework.test import APITestCase
from core.models import User
from django.urls import reverse
from rest_framework.authtoken.models import Token
from author.models import AuthorBlog

class APIEndPointsTest(APITestCase):
    create_url = reverse('create_user')
    url = reverse('create-list-blog')
    delete_update_url = reverse('update-retrive-delete-blog', args=(1,))

    def setUp(self):
        data = {
            "email" : "foobar@example.com",
            "password" : "Password@123"
        }

        self.user = User.objects.create(**{
                'email': 'foobar@example.com',
                'pincode': '444605',
                'name': 'himanshu Sharma',
                'mobile': '8412027866',
                'is_active' : True,
                })
        self.user.set_password('Password@123')
        self.user.save()
        token = Token.objects.create(user=self.user)
        self.token_key = 'Token ' + token.key

        self.author = {
            "title": "document_checking",
            "body": "document_body",
            "summary": "document_summary",
            "created_at": "2021-03-20T09:27:42.780689Z",
            "document": "http://localhost:8000/document/PDF32000_2008_PBhBiMC.pdf",
            "artist": self.user.id
        }

        self.author = AuthorBlog.objects.create(**{
            "title": "document_checking",
            "body": "document_body",
            "summary": "document_summary",
            "created_at": "2021-03-20T09:27:42.780689Z",
            "document": "http://localhost:8000/document/PDF32000_2008_PBhBiMC.pdf",
            "artist": self.user
        })
        self.author.save()
        self.author_id = self.user.id

    def test_create_author_blog(self):
        payload = {
            'artist': self.user.id,
            'title': 'document_checking',
            'body': 'document_body',
            'summary': 'document_summary'
            }
        files=[
            ('document',('file',open('/home/paranoid/PDF32000_2008.pdf','rb'),'application/octet-stream'))
        ]
        response = self.client.post(self.url, data=payload, HTTP_AUTHORIZATION=self.token_key, files=files)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['artist'], payload['artist'])

    def test_show_list_blog(self):
        response = self.client.get(self.url,HTTP_AUTHORIZATION=self.token_key)
        self.assertEqual(response.data[0]['artist'], self.author_id)
        self.assertEqual(response.status_code, 200)

    def test_delete_the_blog(self):
        response = self.client.delete(self.delete_update_url, HTTP_AUTHORIZATION=self.token_key)
        self.assertEqual(response.status_code,204)
