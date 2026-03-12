from django.db import models

# Create your models here.
class Category(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class FoodItem(models.Model):

    name = models.CharField(max_length=200)
    description = models.TextField()

    price = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )

    image = models.ImageField(upload_to="food/")

    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name
