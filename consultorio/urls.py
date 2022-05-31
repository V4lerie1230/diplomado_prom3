from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from consultorio import views

app_name = 'consultorio'
urlpatterns = [
    path('', TemplateView.as_view(template_name="home.html"), name="home"),
    path('pacientes', TemplateView.as_view(template_name="pacientes.html"), name="pacientes"),
    path('medicos', TemplateView.as_view(template_name="medicos.html"), name="medicos"),
    path('especialidades', TemplateView.as_view(template_name="especialidades.html"), name="especialidades"),
    path('citas', views.numero_de_citas, name="numero_citas"),
    path('lista_doctores', views.get_doctores_list, name="lista-doctores"),
    path('lista_pacientes', views.PacienteListView.as_view(), name="lista-pacientes"),
    path('lista_pacientes/crear', views.PacienteCreateView.as_view(), name="crear-pacientes"),
    path('paciente/<int:pk>/', views.PacienteDetailView.as_view(), name='detalle-paciente'),
    path('paciente/<int:pk>/eliminar/', views.PacienteDeleteView.as_view(), name='eliminar-paciente'),
    path('paciente/<int:pk>/actualizar/', views.PacienteDeleteView.as_view(), name='actualizar-paciente'),

]