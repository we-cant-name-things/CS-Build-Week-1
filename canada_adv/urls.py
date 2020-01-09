from django.urls import path, include

from . import views
from .views import current_player, PlayerList


from rest_framework import routers

router = routers.DefaultRouter()
router.register('players', views.PlayerViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path('current_user/', current_player),
    path('players/', PlayerList.as_view())
]
