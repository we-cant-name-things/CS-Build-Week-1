from .models import Player, map

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import PlayerSerializer


class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


@api_view(["GET"])
def player_info(request):
    player_data = Player.objects.values().get(email=request.data['email'])
    current_city = map.search_map(player_data['city'])
    if current_city == -1:
        return Response("Player City does not exit")
    elif current_city != -1:
        player_data['left'] = current_city.left.city
        player_data['right'] = current_city.right.city

    return Response(player_data)
