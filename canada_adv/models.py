from django.db import models


# Create your models here.
class Player(models.Model):
    food = models.IntegerField()
    water = models.IntegerField()


class Places(models.Model):
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    food_available = models.IntegerField()
    water_available = models.IntegerField()

