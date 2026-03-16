from django.db import models
from apps.rooms.models import Room
from apps.activities.models import Activity
from apps.users.models import User

# Create your models here.
class RoomBooking(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    room = models.ForeignKey(
        Room,
        on_delete=models.CASCADE
    )

    check_in = models.DateField() # room availability algorithm
    check_out = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)


class ActivityBooking(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    activity = models.ForeignKey(
        Activity,
        on_delete=models.CASCADE
    )

    date = models.DateField()

    participants = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
