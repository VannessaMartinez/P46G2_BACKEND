from django.conf                                      import settings
from rest_framework                                   import generics, serializers, status
from rest_framework.response                          import Response
from django.http import HttpResponse

from AppCovid19.models.registro_contagio      import Registro
from AppCovid19.models.ubicacion              import Ubicacion
from AppCovid19.models.seguimiento_de_cambios import Seguimiento_de_cambios

from AppCovid19.serializers.ubicacion_Serializer        import UbicacionSerializer
from AppCovid19.serializers.registroContagio_Serializer import RegistroSerializer
from AppCovid19.serializers.seguimiento_Serializer      import SeguimientoCambiosSerializer

class CrearRegistro(generics.CreateAPIView):
    serializer_class = RegistroSerializer
    def post(self, request, *args, **kwargs):
        serializer = RegistroSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response("Transacción exitosa", status=status.HTTP_201_CREATED)
