from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

from apps.menu.models import FoodItem

User = get_user_model()


class OrderViewTests(APITestCase):

    def setUp(self):
        # Create user
        self.user = User.objects.create_user(
            username="testuser",
            password="123456"
        )

        # Create token
        self.token = Token.objects.create(user=self.user)

        # Authenticate requests
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token.key}")

        # Create food items
        self.food1 = FoodItem.objects.create(name="Burger", price=500)
        self.food2 = FoodItem.objects.create(name="Pizza", price=800)

    # ✅ 1. Test order creation (happy path)
    def test_create_order(self):

        data = {
            "items": [
                {"food_item": self.food1.id, "quantity": 2},
                {"food_item": self.food2.id, "quantity": 1}
            ]
        }

        response = self.client.post("/api/orders/", data, format="json")

        self.assertEqual(response.status_code, 201)
        self.assertIn("total", response.data)

        # Expected total = (2 × 500) + (1 × 800) = 1800
        self.assertEqual(response.data["total"], 1800)

    # ❌ 2. Test invalid food item
    def test_create_order_with_invalid_item(self):

        data = {
            "items": [
                {"food_item": 999, "quantity": 1}  # invalid ID
            ]
        }

        response = self.client.post("/api/orders/", data, format="json")

        self.assertEqual(response.status_code, 400)

    # ❌ 3. Test missing items
    def test_create_order_without_items(self):

        data = {}

        response = self.client.post("/api/orders/", data, format="json")

        self.assertEqual(response.status_code, 400)

    # 🔐 4. Test unauthorized access
    def test_create_order_without_authentication(self):

        self.client.credentials()  # remove token

        data = {
            "items": [
                {"food_item": self.food1.id, "quantity": 1}
            ]
        }

        response = self.client.post("/api/orders/", data, format="json")

        self.assertEqual(response.status_code, 401)


    # 5. Prevent price manipulation
    def test_total_cannot_be_manipulated(self):

    data = {
        "items": [
            {"food_item": self.food1.id, "quantity": 2}
        ],
        "total": 1  # malicious attempt
    }

    response = self.client.post("/api/orders/", data, format="json")

    # System should ignore client total and calculate its own
    self.assertEqual(response.status_code, 201)
    self.assertNotEqual(response.data["total"], 1)

