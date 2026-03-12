from django.db import models
from apps.users.models import User

# Create your models here.
class Payment(models.Model):

    PAYMENT_METHODS = (
        ("mpesa", "M-Pesa"),
        ("card", "Card"),
    )

    STATUS = (
        ("pending", "Pending"),
        ("success", "Success"),
        ("failed", "Failed"),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    amount = models.DecimalField(max_digits=10, decimal_places=2)

    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHODS)

    status = models.CharField(max_length=20, choices=STATUS)

    transaction_id = models.CharField(max_length=200)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.transaction_id)
