def test_filter_rooms_by_capacity(self):
    response = self.client.get("/api/rooms/?capacity=2")
    self.assertEqual(response.status_code, 200)
