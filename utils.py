from canada_adv.serializers import PlayerSerializer


def my_jwt_response_handler(token, player=None, request=None):
    """
    all this is doing is adding a new ‘player’ field with the players’s serialized data when a token is generated.
     this is going to be our new default JWT response handler.
    """
    return {
        'token': token,
        'player': PlayerSerializer(player, context={'request': request}).data
    }