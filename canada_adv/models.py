from django.db import models


# Create your models here.
class Player(models.Model):
    food = models.IntegerField()
    water = models.IntegerField()
    current_location = models.CharField(max_length=30)


class Place(models.Model):
    state = models.CharField(max_length=30, blank=False)
    city = models.CharField(max_length=30, blank=False)
    location = models.CharField(max_length=30, blank=False)
    food_available = models.IntegerField(blank=False)
    water_available = models.IntegerField(blank=False)

