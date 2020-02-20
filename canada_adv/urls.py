from django.urls import path, include

from . import api

from rest_framework import routers

router = routers.DefaultRouter()
router.register('users', api.UserInfoViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("user/", api.UserInfoViewSet),
    path("move/", api.move_city),
    path("map/", api.map_endpoint),
]
