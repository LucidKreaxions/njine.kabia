from django.db import models
from apps.users.models import User
from apps.orders.models import Order
from apps.bookings.models import RoomBooking


class Payment(models.Model):

    PAYMENT_METHODS = [
        ("mpesa", "M-Pesa"),
        ("card", "Card"),
    ]

    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("completed", "Completed"),
        ("failed", "Failed"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    order = models.ForeignKey(
        Order,
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )

    booking = models.ForeignKey(
        RoomBooking,
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )

    amount = models.DecimalField(max_digits=10, decimal_places=2)

    payment_method = models.CharField(
        max_length=20,
        choices=PAYMENT_METHODS
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="pending"
    )

    transaction_id = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment {self.id}"
