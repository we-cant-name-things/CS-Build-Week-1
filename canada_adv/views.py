from .models import Player, map
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import PlayerSerializer
from django.core.exceptions import ObjectDoesNotExist
import random

places = ['gas_station', 'hotel', 'fast_food', 'bank', 'store']


def random_generator_pick_2(arr):
    arr_copy = arr[:]
    random_place_1 = random.choice(arr_copy)
    arr_copy.remove(random_place_1)
    random_place_2 = random.choice(arr_copy)
    return [random_place_1, random_place_2]


class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


@api_view(["GET"])
def player_info(request):
    try:
        player_data = Player.objects.values().get(email=request.data.get('email'))
        current_city = map.search_map(player_data.get('city'))
        if current_city == -1:
            return Response("Player City does not exit")
        elif current_city != -1:
            player_data['left'] = current_city.left.city if current_city.left else None
            player_data['right'] = current_city.right.city if current_city.right else None
            player_data['previous'] = current_city.previous.city if current_city.previous else None
        return Response(player_data)
    except ObjectDoesNotExist:
        return Response("Invalid email")


@api_view(["PUT"])
def move_forward(request):
    # email, next_city user chooses, food, water
    random_places = random_generator_pick_2(places)
    try:
        next_city = map.search_map(request.data.get('next_city'))

        left = next_city.left.city if next_city.left else None
        right = next_city.right.city if next_city.right else None
        previous = next_city.previous.city if next_city.previous else None

        player = Player.objects.get(email=request.data.get('email'))
        player.city = request.data.get('next_city')
        player.food = request.data.get('food')
        player.water = request.data.get('water')

        player.location = random_places[0]
        player.food_available = random.randint(1, 10)
        player.water_available = random.randint(1, 10)

        player.location_2 = random_places[1]
        player.food_available_2 = random.randint(1, 10)
        player.water_available_2 = random.randint(1, 10)


        player.save()

        player_data = Player.objects.values().get(email=request.data.get('email'))

        return Response(player_data)

    except ObjectDoesNotExist:
        return Response("Invalid email")
