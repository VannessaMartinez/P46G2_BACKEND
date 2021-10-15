from django.conf                import settings
from rest_framework             import generics, status
from rest_framework.response    import Response
from django.http                import HttpResponse

from AppCovid19.models.registro_contagio      import Registro
from AppCovid19.models.ubicacion              import Ubicacion
from AppCovid19.models.seguimiento_de_cambios import Seguimiento_de_cambios

from AppCovid19.serializers.ubicacion_Serializer        import UbicacionSerializer
from AppCovid19.serializers.registroContagio_Serializer import RegistroSerializer

class MostarRegistros(generics.ListAPIView):
    serializer_class   = RegistroSerializer
    def get_queryset(self):
        queryset = Registro.objects.all()     #De todas las transacciones, filtra aquellas con cuenta origen = "account" que viene en la url
        return queryset