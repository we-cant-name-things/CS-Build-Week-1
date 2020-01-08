from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .models import Player, Place

from django.views.decorators.csrf import csrf_exempt



# This is for tree nodes when the player moves to a new city
class City:
    def __init__(self, state, city, left, right, previous):
        self.state = state
        self.city = city
        self.left = left
        self.right = right
        self.previous = previous

@csrf_exempt
@api_view(["GET"])
def player(request):
    email = request.data['email']
    player_data = Player.objects.get(email=email)
    return JsonResponse({"email": player_data.current_place.city})
