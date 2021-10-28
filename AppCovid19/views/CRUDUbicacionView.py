from django.conf                                    import settings
from rest_framework                                 import generics, status
from rest_framework.response                        import Response
from django.http                                    import HttpResponse
from AppCovid19.models.ubicacion                    import Ubicacion
from AppCovid19.serializers.ubicacion_Serializer    import UbicacionSerializer
from AppCovid19.serializers.ubiSerializer           import UbiSerializer

from rest_framework.permissions                   import IsAuthenticated

def consultar_registros_view(request):
    message = 'Aca van los registros!'
    return HttpResponse (message)

class UnRegistroidUbicacion(generics.ListAPIView):
    serializer_class   = UbiSerializer
     
    def get_queryset(self):
        queryset = Ubicacion.objects.filter(codigoDivipolaMunicipio=self.kwargs['codigo_mun'])     #De todas las transacciones, filtra aquellas con cuenta origen = "account" que viene en la url
        return queryset

class MostarTodasUbicaciones(generics.ListAPIView):
    serializer_class   = UbiSerializer

    def get_queryset(self):
        queryset = Ubicacion.objects.all()     #De todas las transacciones, filtra aquellas con cuenta origen = "account" que viene en la url
        return queryset

class CrearUbicacion(generics.CreateAPIView):    #Crear un registro
    serializer_class   = UbicacionSerializer
    permission_classes = (IsAuthenticated,)
    def post(self, request, *args, **kwargs):                                      #request: viene en el body del post. Se obtiene info con request.data[nombre de la llave]
            
        serializer = UbicacionSerializer(data=request.data)                        #pasamos del json que recibimos al objeto de tipo transacción
        serializer.is_valid(raise_exception=True)                                  #verificar si es valido
        serializer.save()                                                          #guarda al transacción en la bd

        return Response("Transacción exitosa", status=status.HTTP_201_CREATED)     #devuelve msj de transacción exitosa

class ActualizarUbicacion(generics.UpdateAPIView):                                 #Actualizar un registro
    serializer_class   = UbicacionSerializer
    queryset           = Ubicacion.objects.all()

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)                            #con esta línea se actualiza el registro