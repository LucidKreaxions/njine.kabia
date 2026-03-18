from rest_framework.test import APITestCase

class PaymentTests(APITestCase):

    def test_create_payment(self):
        response = self.client.post("/api/payments/", {
            "order": 1,
            "amount": 1000,
            "payment_method": "mpesa"
        })

        self.assertIn(response.status_code, [200, 201])
