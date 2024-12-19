from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Post


# Create your tests here.


class PostAPITestCase(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='testuser', password='password')
        self.client.login(username='testuser', password='password')

    def test_create_post(self):
        data = {'title': 'Test Post', 'content': 'This is a test'}
        response = self.client.post('/api/posts', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
