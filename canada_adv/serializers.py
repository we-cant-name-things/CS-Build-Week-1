from rest_framework import serializers
from .models import Player


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['email', 'food', 'water',
                  'state', 'city',
                  'location', 'food_available', 'water_available',
                  'location_2', 'food_available_2', 'water_available_2']
