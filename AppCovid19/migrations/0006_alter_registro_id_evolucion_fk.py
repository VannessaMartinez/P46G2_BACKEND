# Generated by Django 3.2.8 on 2021-10-15 06:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AppCovid19', '0005_alter_registro_id_evolucion_fk'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registro',
            name='id_evolucion_fk',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='AppCovid19.seguimiento_de_cambios'),
        ),
    ]
