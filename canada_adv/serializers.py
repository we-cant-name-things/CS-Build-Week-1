from rest_framework import serializers
from .models import Player, Place


class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Player
        fields = ['id', 'food', 'water', 'email', 'current_place']
        lookup_field = 'email'




class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ['state', 'city', 'location', 'food_available', 'water_available']
