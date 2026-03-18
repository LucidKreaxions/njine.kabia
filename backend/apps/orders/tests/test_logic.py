from rest_framework.test import APITestCase
from apps.menu.models import FoodItem

class OrderLogicTests(APITestCase):

    def setUp(self):
        self.item = FoodItem.objects.create(name="Burger", price=500)

    def test_order_total_calculation(self):
        response = self.client.post("/api/orders/", {
            "items": [
                {"food_item": self.item.id, "quantity": 2}
            ]
        }, format="json")

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["total"], 1000)
