from django.db import models
from rest_framework.permissions import IsAuthenticated


# Create your models here.
class Menu(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()

    def __str__(self):
        return self.title


class MenuItem(models.Model):
    permission_classes = [IsAuthenticated]
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()

    def __str__(self):
        return f'{self.title}: {str(self.price)}'


class Booking(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField()
    booking_date = models.DateField()

    def __str__(self):
        return self.name