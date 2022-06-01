from django.db import models
from datetime import datetime
from dateutil import relativedelta as rdelta
from tzlocal import get_localzone
# Create your models here.

class Jugador(models.Model):
    uniqueId = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_de_nacimiento = models.DateField()

    def __str__(self):
        return self.nombre

    def age(self):
        local_tz = get_localzone()
        now = datetime.now(local_tz)
        birthday = self.fecha_de_nacimiento
        rd = rdelta.relativedelta(now, birthday)
        if rd.years:
            name_year = 'años'
            name_months = 'meses'
            if rd.years == 1:
                name_year = 'año'

            if rd.months == 1:
                name_months = 'mes'

            return "{0.years} {name_year} {0.months} {name_months}".format(
                rd,
                name_year=name_year,
                name_months=name_months
            )

        else:
            name_months = 'meses'
            name_days = 'días'
            if rd.months == 1:
                name_months = 'mes'

            if rd.days == 1:
                name_days = 'día'
            return "{0.months}  {name_months}, {0.days} {name_days}".format(
                rd,
                name_months=name_months,
                name_days=name_days
            )


class Profesor(models.Model):
    uniqueId = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Partidos(models.Model):
    uniqueId = models.AutoField(primary_key=True)
    ubicacion = models.CharField(max_length=500)
    fecha = models.DateField(default=datetime.now)
    jugador_id = models.ForeignKey('Jugador', on_delete=models.CASCADE)
    profesor_id = models.ForeignKey('Profesor', on_delete=models.CASCADE)
    diagnostico = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return "{} - {} - {}".format(self.jugador_id, self.profesor_id, self.fecha)