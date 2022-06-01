from django.contrib import admin
from .models import Jugador, Profesor, Partidos

# Register your models here.
admin.site.register(Jugador)
admin.site.register(Profesor)
admin.site.register(Partidos)