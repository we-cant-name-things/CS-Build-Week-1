from .models import Player

from rest_framework import viewsets

from .serializers import PlayerSerializer, PlayerSerializerWithToken
from django.http import HttpResponseRedirect
from rest_framework import permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView


class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer



@api_view(['GET'])
def current_player(request):
    """
    Determine the current player by their token, and return their data.
    This view will be used anytime the user revisits the site, reloads the page, 
    or does anything else that causes React to forget its state. 
    React will check if the user has a token stored in the browser, and if a token is found, 
    it’ll make a request to this view. 
    """
    
    serializer = PlayerSerializer(request.user)  #might need to fix this line regarding using request.user
    return Response(serializer.data)


class PlayerList(APIView):
    """
    Create a new player. It's called 'PlayerList' because normally we'd have a get
    method here too, for retrieving a list of all Player objects.
    """

    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = PlayerSerializerWithToken(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)