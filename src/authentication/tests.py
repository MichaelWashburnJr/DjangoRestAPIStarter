from django.contrib.auth.models import User
from django.core import mail
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.test import APITestCase

class AuthenticationTestCase(APITestCase):

    def setUp(self):
        self.user_password = 'Password!'
        self.user = User.objects.create_user(email='test123@test.com', username='test123@test.com', password=self.user_password)

    def test_registration(self):
        """
        Ensure we can register new users.
        """
        url = reverse('rest_register')
        data = {
            'password1': 'Password!',
            'password2': 'Password!',
            'email': 'test@test.com'
        }
        self.assertEqual(User.objects.count(), 1)
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)

        # Test that one message has been sent.
        self.assertEqual(len(mail.outbox), 1)

    def test_login(self):
        """Make sure we can login to an account."""
        email = 'test@test.com'
        password = 'Password!'
        User.objects.create_user(username=email, email=email, password=password)

        url = reverse('rest_login')
        data = {
            'email': email,
            'password': password
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['user']['email'], email)

    def test_logout(self):
        """Verifies the user can logout properly."""
        url = reverse('rest_login')
        data = {
            'email': self.user.email,
            'password': self.user_password
        }
        response = self.client.post(url, data, format='json')

        url = reverse('rest_logout')
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)