from .models import Player, Place

from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import PlayerSerializer, PlaceSerializer
from rest_framework.decorators import action


class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

    @action(methods=['get'], detail=False)
    def player(self, request):
        email = request.data['email']
        query = self.get_queryset().get(email=email)
        serializer = self.get_serializer_class()(query)
        return Response(serializer.data)


class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer

    # @action(methods=['get'], detail=False)
    # def player(self, request):
    #     email = request.data['email']
    #     query = self.get_queryset().get(email=email)
    #     serializer = self.get_serializer_class()(query)
    #     return Response(serializer.data)
