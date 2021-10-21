from django.db import models
from .ubicacion import Ubicacion

class Registro(models.Model):
    id_caso                        = models.AutoField(primary_key=True,blank=True)
    codigo_divipola_municipio_fk   = models.ForeignKey(Ubicacion, null=False, blank=False, on_delete=models.CASCADE)
    fecha_notificacion             = models.DateField()
    fecha_reporte                  = models.DateField()
    fecha_sintomas                 = models.DateField()
    fecha_diagnostico_lab          = models.DateField()
    edad                           = models.IntegerField()
    unidad_de_medida_edad          = models.IntegerField()                                      #modificar frontend
    sexo                           = models.CharField(max_length=5)
    grupo_etnico                   = models.CharField(max_length=30)
    pertenencia_etnica             = models.IntegerField()   #modificar frontend
    fecha_recuperacion             = models.DateField()
    tipo_recuperacion              = models.CharField(max_length=20)