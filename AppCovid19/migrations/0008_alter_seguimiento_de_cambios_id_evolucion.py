# Generated by Django 3.2.7 on 2021-10-15 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCovid19', '0007_auto_20211015_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seguimiento_de_cambios',
            name='id_evolucion',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
