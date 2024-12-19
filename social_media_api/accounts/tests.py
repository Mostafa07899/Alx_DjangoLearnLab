from django.test import TestCase
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model


# Create your tests here.

User = get_user_model()

class FollowFeatureTests(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='user1', password='password')
        self.user2 = User.objects.create_user(username='user2', password='password')
        self.client.login(username='user1', password='password')

    def test_follow_user(self):
        response = self.client.post(f'/accounts/follow/{self.user2.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(self.user2 in self.user1.following.all())

    def test_feed(self):
        pass

