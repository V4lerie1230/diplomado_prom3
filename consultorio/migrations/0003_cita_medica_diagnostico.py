# Generated by Django 4.0.4 on 2022-05-17 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultorio', '0002_cita_medica_fecha'),
    ]

    operations = [
        migrations.AddField(
            model_name='cita_medica',
            name='diagnostico',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
