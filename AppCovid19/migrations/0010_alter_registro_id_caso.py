# Generated by Django 3.2.7 on 2021-10-15 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCovid19', '0009_auto_20211015_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registro',
            name='id_caso',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]