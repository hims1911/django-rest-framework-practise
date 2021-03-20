from django.test import TestCase
from .models import User
# Create your tests here.
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from django.urls import reverse



'''
    Unit test Case For registing User
'''
class AccountsTest(APITestCase):

    create_url = reverse('create_user')
    login_url = reverse('login')
    
    def test_create_user(self):
        """
        Ensure we can create a new user and a valid token is created with it.
        """
        data = {
                'email': 'foobar@example.com',
                'password': 'Password@123',
                'pincode': '444605',
                'name': 'himanshu Sharma',
                'mobile': "8412027866"
                }

        response = self.client.post(self.create_url , data, format='json')
        user = User.objects.latest('id')
        token = Token.objects.get(user=user)
        self.assertEqual(response.data['token'], token.key)
    
    def test_login(self):
        data = {
            "email" : "foobar@example.com",
            "password" : "Password@123"
        }

        user = User.objects.create(**{
                'email': 'foobar@example.com',
                'pincode': '444605',
                'name': 'himanshu Sharma',
                'mobile': '8412027866',
                'is_active' : True,
                })
        user.set_password('Password@123')
        user.save()

        response = self.client.post(self.login_url, data, format='json')

        token = Token.objects.get(user=user)

        self.assertEqual(response.data['token'], token.key)
        self.assertEqual(response.status_code, 200)


