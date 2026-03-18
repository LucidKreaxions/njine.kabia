from rest_framework.test import APITestCase
from django.urls import reverse

class AuthTests(APITestCase):

    def test_register_user(self):
        response = self.client.post(reverse("register"), {
            "username": "stephen",
            "password": "123456"
        })

        self.assertEqual(response.status_code, 201)

    def test_login_user(self):
        self.client.post(reverse("register"), {
            "username": "stephen",
            "password": "123456"
        })

        response = self.client.post(reverse("login"), {
            "username": "stephen",
            "password": "123456"
        })

        self.assertEqual(response.status_code, 200)
        self.assertIn("token", response.data)
