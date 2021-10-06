from django.db import models

from AppCovid19.models.ubicacion_geografica import Ubicacion_geografica
from .registro_contagio import Registro_contagio

class Seguimiento_de_cambios(models.Model):
    id_evolucion    = models.BigAutoField(primary_key=True)
    id_caso_fk      = models.ForeignKey(Registro_contagio, related_name='id_caso', on_delete=models.CASCADE)
    ubicacion_caso  = models.CharField('Ubicacion_caso', max_length=30)
    estado          = models.CharField('Estado', max_length=20)
    tipo_contagio   = models.CharField('Tipo_de_contagio', max_length=20)
    recuperado      = models.CharField('Recuperado', max_length=20)
    fecha_muerte    = models.DateTimeField()