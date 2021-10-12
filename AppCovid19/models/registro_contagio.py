from django.db import models
from .ubicacion import Ubicacion


class Registro(models.Model):
    id_caso                        = models.BigAutoField(primary_key=True)
    codigo_divipola_municipio_fk   = models.ForeignKey(Ubicacion, null=False, blank=False,  on_delete=models.CASCADE)
    fecha_notificacion             = models.DateField()
    fecha_reporte                  = models.DateField()
    fecha_sintomas                 = models.DateField()
    fecha_diagnostico_lab          = models.DateField()
    edad                           = models.IntegerField()
    unidad_de_medida_edad          = models.IntegerField()
    sexo                           = models.CharField('Sexo', max_length=5)
    grupo_etnico                   = models.CharField('Grupo_etnico', max_length=30)
    pertenencia_etnica             = models.CharField('Pertenencia_etnica', max_length=30)
    fecha_recuperacion             = models.DateField()
    tipo_recuperacion              = models.CharField('Tipo_de_recuperacion', max_length=20)


