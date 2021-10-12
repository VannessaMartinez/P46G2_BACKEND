# Generated by Django 3.2.8 on 2021-10-12 17:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('id_caso', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_notificacion', models.DateField()),
                ('fecha_reporte', models.DateField()),
                ('fecha_sintomas', models.DateField()),
                ('fecha_diagnostico_lab', models.DateField()),
                ('edad', models.IntegerField()),
                ('unidad_de_medida_edad', models.IntegerField()),
                ('sexo', models.CharField(max_length=5, verbose_name='Sexo')),
                ('grupo_etnico', models.CharField(max_length=30, verbose_name='Grupo_etnico')),
                ('pertenencia_etnica', models.IntegerField(verbose_name='Pertenencia_etnica')),
                ('fecha_recuperacion', models.DateField()),
                ('tipo_recuperacion', models.CharField(max_length=20, verbose_name='Tipo_de_recuperacion')),
            ],
        ),
        migrations.CreateModel(
            name='Ubicacion',
            fields=[
                ('codigoDivipolaMunicipio', models.IntegerField(primary_key=True, serialize=False)),
                ('codigo_iso_pais', models.IntegerField(default=0)),
                ('nombre_pais', models.CharField(max_length=30, verbose_name='Nombre_del_pais')),
                ('codigo_divipola_departamento', models.IntegerField(default=0)),
                ('nombre_departamento', models.CharField(max_length=30, verbose_name='Nombre_del_departamento')),
                ('nombre_municipio', models.CharField(max_length=30, verbose_name='Nombre_del_municipio')),
            ],
        ),
        migrations.CreateModel(
            name='Seguimiento_de_cambios',
            fields=[
                ('id_evolucion', models.AutoField(primary_key=True, serialize=False)),
                ('ubicacion_caso', models.CharField(max_length=30, verbose_name='Ubicacion_caso')),
                ('estado', models.CharField(max_length=20, verbose_name='Estado')),
                ('tipo_contagio', models.CharField(max_length=20, verbose_name='Tipo_de_contagio')),
                ('recuperado', models.CharField(max_length=20, verbose_name='Recuperado')),
                ('fecha_muerte', models.DateField()),
                ('id_del_caso_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppCovid19.registro')),
            ],
        ),
        migrations.AddField(
            model_name='registro',
            name='codigo_divipola_municipio_fk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppCovid19.ubicacion'),
        ),
    ]
