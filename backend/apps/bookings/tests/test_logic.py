def test_prevent_double_booking(self):
    data = {
        "room": self.room.id,
        "check_in": "2026-03-20",
        "check_out": "2026-03-25"
    }

    self.client.post("/api/bookings/", data)
    response = self.client.post("/api/bookings/", data)

    self.assertEqual(response.status_code, 400)
