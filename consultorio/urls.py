from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from consultorio import views

app_name = 'consultorio'
urlpatterns = [
    path('', TemplateView.as_view(template_name="home.html"), name="home"),
    path('jugadores', TemplateView.as_view(template_name="jugadores.html"), name="jugadores"),
    path('profesores', TemplateView.as_view(template_name="profesores.html"), name="profesores"),
    path('partidos', TemplateView.as_view(template_name="partidos.html"), name="partidos"),
    path('partidos_numerop', views.numero_de_partidos, name="numero_de_partidos"),
    path('lista_profesor', views.get_profesor_list, name="lista-profesores"),
    path('lista_jugador', views.JugadorListView.as_view(), name="lista-jugadores"),
    path('lista_jugadores/crear', views.JugadorCreateView.as_view(), name="crear-jugadores"),
    path('jugador/<int:pk>/', views.JugadorDetailView.as_view(), name='detalle-jugador'),
    path('jugador/<int:pk>/eliminar/', views.JugadorDeleteView.as_view(), name='eliminar-jugador'),
    path('jugador/<int:pk>/actualizar/', views.JugadorDeleteView.as_view(), name='actualizar-jugador'),

]