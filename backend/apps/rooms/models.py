from django.db import models

# Create your models here.
class Room(models.Model):

    name = models.CharField(max_length=200)

    description = models.TextField()

    price_per_night = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )

    capacity = models.IntegerField()

    image = models.ImageField(upload_to="rooms/")

    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name
