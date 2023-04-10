from django.test import TestCase
from django.contrib.auth import get_user_model


class HomePageTest(TestCase):
    def test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
