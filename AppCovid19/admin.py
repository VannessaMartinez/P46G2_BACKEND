from django.contrib import admin
from .models.ubicacion import Ubicacion
from .models.registro_contagio import Registro
from .models.seguimiento_de_cambios import Seguimiento_de_cambios

# Register your models here.

admin.site.register(Ubicacion)
admin.site.register(Registro)
admin.site.register(Seguimiento_de_cambios)

