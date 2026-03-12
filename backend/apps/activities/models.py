from django.db import models

# Create your models here.
class Activity(models.Model):

    name = models.CharField(max_length=200)

    description = models.TextField()

    price = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )

    duration = models.IntegerField()

    capacity = models.IntegerField()

    image = models.ImageField(upload_to="activities/")

    def __str__(self):
        return self.name
