from django.urls import path, include

from . import views

from rest_framework import routers

router = routers.DefaultRouter()
router.register('players', views.PlayerViewSet)
router.register('places', views.PlaceViewSet)

urlpatterns = [
    path("", include(router.urls))
]
