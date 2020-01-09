from django.urls import path, include

from . import views

from rest_framework import routers

router = routers.DefaultRouter()
router.register('players', views.PlayerViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("player/", views.player_info),
    path("forward/", views.move_forward)
]
