from rest_framework import serializers
from .models import Player, Place


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['id', 'food', 'water', 'email', 'current_place']


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ['state', 'city', 'location', 'food_available', 'water_available']
