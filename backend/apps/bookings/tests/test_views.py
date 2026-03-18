from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from apps.rooms.models import Room

User = get_user_model()

class BookingViewTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="test", password="123456")
        self.token = Token.objects.create(user=self.user)

        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token.key}")

        self.room = Room.objects.create(name="Suite", price=200, capacity=2)

    def test_create_booking(self):
        response = self.client.post("/api/bookings/", {
            "room": self.room.id,
            "check_in": "2026-03-20",
            "check_out": "2026-03-25"
        })

        self.assertEqual(response.status_code, 201)
