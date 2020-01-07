from django.contrib import admin

# Register your models here.
from .models import Player, Place

admin.site.register(Player)
admin.site.register(Place)

