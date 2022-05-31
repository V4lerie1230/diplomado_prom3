from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy, reverse
from django.shortcuts import render

from .models import Cita_medica, Doctor, Paciente

# Create your views here.

def numero_de_citas(request):
    citas = Cita_medica.objects.all()

    context = {
        "numero_citas": len(citas)
    }
    return render(request, 'numero_citas_medicas.html', context)


def get_doctores_list(request):
    doctores = Doctor.objects.all()

    context = {
        'doctores': doctores
    }
    return render(request, 'doctor_list.html', context)


class PacienteListView(ListView):
    model = Paciente
    context_object_name = 'paciente_list'
    template_name = 'paciente_list.html'


class PacienteDetailView(DetailView):
    model = Paciente

class PacienteCreateView(CreateView):
    model = Paciente
    fields = ['nombre', 'apellido', 'fecha_de_nacimiento']
    # success_url = reverse_lazy('consultorio:lista-pacientes')

    def get_success_url(self):
        return reverse('consultorio:detalle-paciente', kwargs={'pk': self.object.pk})


class PacienteUpdateView(UpdateView):
    model = Paciente
    fields = ['nombre', 'apellido', 'fecha_de_nacimiento']
    success_url = reverse_lazy('consultorio:lista-pacientes')


class PacienteDeleteView(DeleteView):
    model = Paciente
    success_url = reverse_lazy('consultorio:lista-pacientes')
