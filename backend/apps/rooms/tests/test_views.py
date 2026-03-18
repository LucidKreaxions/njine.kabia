from rest_framework.test import APITestCase
from apps.rooms.models import Room

class RoomViewTests(APITestCase):

    def setUp(self):
        Room.objects.create(name="Deluxe", price=100, capacity=2)

    def test_list_rooms(self):
        response = self.client.get("/api/rooms/")
        self.assertEqual(response.status_code, 200)
