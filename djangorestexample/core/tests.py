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
    
    def test_create_user(self):
        """
        Ensure we can create a new user and a valid token is created with it.
        """
        data = {
                'email': 'foobar@example.com',
                'password': 'Password@123',
                'pincode': '444605',
                'name': 'himanshu Sharma',
                "mobile": "8412027866"
                }

        response = self.client.post(self.create_url , data, format='json')
        user = User.objects.latest('id')
        token = Token.objects.get(user=user)
        self.assertEqual(response.data['token'], token.key)


'''
    Unit Test Case For Login User
'''