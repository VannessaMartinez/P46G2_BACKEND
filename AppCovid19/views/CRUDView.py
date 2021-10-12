from django.conf                                      import settings
from rest_framework                                   import generics, status
from rest_framework.response                          import Response
from django.http import HttpResponse

from AppCovid19.models.registro_contagio      import Registro
from AppCovid19.models.ubicacion              import Ubicacion
from AppCovid19.models.seguimiento_de_cambios import Seguimiento_de_cambios

from AppCovid19.serializers.ubicacion_Serializer        import UbicacionSerializer
from AppCovid19.serializers.registroContagio_Serializer import RegistroSerializer

def consultar_registros_view(request):
    message = 'Aca van los registros!'
    return HttpResponse (message)

class UnRegistroidUbicacion(generics.ListAPIView):
    serializer_class   = UbicacionSerializer
     

    def get_queryset(self):
        queryset = Ubicacion.objects.filter(codigoDivipolaMunicipio=self.kwargs['codigo_mun'])     #De todas las transacciones, filtra aquellas con cuenta origen = "account" que viene en la url
        return queryset


class MostarTodasUbicaciones(generics.ListAPIView):
    serializer_class   = UbicacionSerializer
     

    def get_queryset(self):
        queryset = Ubicacion.objects.all()     #De todas las transacciones, filtra aquellas con cuenta origen = "account" que viene en la url
        return queryset

class CrearUbicacion(generics.CreateAPIView):    #Crear un registro
    serializer_class   = UbicacionSerializer
    def post(self, request, *args, **kwargs):                                      #request: viene en el body del post. Se obtiene info con request.data[nombre de la llave]
            
        serializer = UbicacionSerializer(data=request.data)                        #pasamos del json que recibimos al objeto de tipo transacción
        serializer.is_valid(raise_exception=True)                                  #verificar si es valido
        serializer.save()                                                          #guarda al transacción en la bd

        return Response("Transacción exitosa", status=status.HTTP_201_CREATED)     #devuelve msj de transacción exitosa
