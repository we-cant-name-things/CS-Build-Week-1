from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('canada_adv.urls')),
    url('registration/', include('rest_auth.registration.urls')),
    path('', include('rest_auth.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]

