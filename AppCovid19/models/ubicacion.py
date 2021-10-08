from django.db import models

class Ubicacion(models.Model):
    codigoDivipolaMunicipio       = models.BigAutoField(primary_key=True)
    codigo_iso_pais               = models.IntegerField(default=0)
    nombre_pais                   = models.CharField('Nombre_del_pais', max_length=30)
    codigo_divipola_departamento  = models.IntegerField(default=0)
    nombre_departamento           = models.CharField('Nombre_del_departamento', max_length=30)
    nombre_municipio              = models.CharField('Nombre_del_municipio', max_length=30)
