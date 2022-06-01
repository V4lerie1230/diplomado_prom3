from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy, reverse
from django.shortcuts import render

from .models import Partidos, Profesor, Jugador

# Create your views here.

def numero_de_partidos(request):
    partidos = Partidos.objects.all()

    context = {
        "numero_de_partidos": len(partidos)
    }
    return render(request, 'numero_de_partidos.html', context)


def get_profesor_list(request):
    profesores = Profesor.objects.all()

    context = {
        'profesores': profesores
    }
    return render(request, 'profesores_list.html', context)


class JugadorListView(ListView):
    model = Jugador
    context_object_name = 'jugador_list'
    template_name = 'jugador_list.html'


class JugadorDetailView(DetailView):
    model = Jugador

class JugadorCreateView(CreateView):
    model = Jugador
    fields = ['nombre', 'apellido', 'fecha_de_nacimiento']
    # success_url = reverse_lazy('consultorio:lista-jugadores')

    def get_success_url(self):
        return reverse('consultorio:detalle-jugador', kwargs={'pk': self.object.pk})


class JugadorUpdateView(UpdateView):
    model = Jugador
    fields = ['nombre', 'apellido', 'fecha_de_nacimiento']
    success_url = reverse_lazy('consultorio:lista-jugadores')


class JugadorDeleteView(DeleteView):
    model = Jugador
    success_url = reverse_lazy('consultorio:lista-jugadores')
