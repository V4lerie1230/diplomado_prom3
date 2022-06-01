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
        today = datetime.now(local_tz).date()
        birthday = self.fecha_de_nacimiento
        rd = rdelta.relativedelta(today, birthday)
        return rd.years

    def categoria(self):
        age = self.age()
        category = {
            18: "Cat J",
            19: "Cat J",
            20: "Cat A",
            21: "Cat A",
            22: "Cat C",
            23: "Cat C",
        }
        return category.get(age, "Cat No")


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