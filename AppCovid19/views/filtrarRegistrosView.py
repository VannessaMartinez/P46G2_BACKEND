from django.conf                                      import settings
from django.db import models
from django.db.models import query
from rest_framework                                   import generics, serializers, status
from rest_framework.response                          import Response
from django.http import HttpResponse

from AppCovid19.models.registro_contagio      import Registro
from AppCovid19.models.ubicacion              import Ubicacion
from AppCovid19.models.seguimiento_de_cambios import Seguimiento_de_cambios

from AppCovid19.serializers.ubicacion_Serializer        import UbicacionSerializer
from AppCovid19.serializers.registroContagio_Serializer import RegistroSerializer
from AppCovid19.serializers.seguimiento_Serializer      import SeguimientoCambiosSerializer

class FiltrarSexo(generics.ListAPIView):
    serializer_class = RegistroSerializer
    def get_queryset(self):
        queryset = self.kwargs['sexo']
        return Registro.objects.filter(sexo=queryset)

class FiltrarEstado(generics.ListAPIView):
    serializer_class = SeguimientoCambiosSerializer
    def get_queryset(self):
        queryset = self.kwargs['estado']
        return Seguimiento_de_cambios.objects.filter(estado=queryset)


class FiltrarMunicipio(generics.ListAPIView):
    serializer_class = UbicacionSerializer
    def get_queryset(self):
        queryset = self.kwargs['codigoDivipolaMunicipio']
        return Ubicacion.objects.filter(codigoDivipolaMunicipio=queryset)