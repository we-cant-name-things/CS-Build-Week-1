from django.contrib import admin
from django.urls import path, include
from django.conf.urls import include

from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('canada_adv.urls')),
    path('token-auth/', obtain_jwt_token)
]
