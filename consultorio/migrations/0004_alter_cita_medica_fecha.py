# Generated by Django 4.0.4 on 2022-05-17 01:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultorio', '0003_cita_medica_diagnostico'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cita_medica',
            name='fecha',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]