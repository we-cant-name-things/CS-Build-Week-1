from django.db import models


# Create your models here.


class Place(models.Model):
    state = models.CharField(max_length=30, blank=False)
    city = models.CharField(max_length=30, blank=False)
    location = models.CharField(max_length=30, blank=False)
    food_available = models.IntegerField(blank=False)
    water_available = models.IntegerField(blank=False)


class Player(models.Model):
    food = models.IntegerField()
    water = models.IntegerField()
    current_place = models.ForeignKey(Place, on_delete=models.PROTECT)
