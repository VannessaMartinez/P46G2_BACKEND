from django.db import models

class Seguimiento_de_cambios(models.Model):
    id_evolucion    = models.IntegerField(primary_key=True)
    ubicacion_caso  = models.CharField('Ubicacion_caso', max_length=30)
    estado          = models.CharField('Estado', max_length=20)
    tipo_contagio   = models.CharField('Tipo_de_contagio', max_length=20)
    recuperado      = models.CharField('Recuperado', max_length=20)
    fecha_muerte    = models.DateField(null=True)