from django.test import TestCase
from rest_framework.test import APIClient

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User

class AuthenticationTestCase(APITestCase):

    def test_registration(self):
        """
        Ensure we can register new users.
        """
        url = reverse('rest_register')
        data = {
        	'username': 'test',
        	'password1': 'Password!',
        	'password2': 'Password!',
        	'email': 'test@email.com'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, 'test')
