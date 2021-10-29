from django.conf                                    import settings
from rest_framework                                 import generics, status
from rest_framework.response                        import Response
from django.http                                    import HttpResponse
from AppCovid19.models.ubicacion                    import Ubicacion
from AppCovid19.serializers.ubicacion_Serializer    import UbicacionSerializer
from AppCovid19.serializers.ubiSerializer           import UbiSerializer

def consultar_registros_view(request):
    message = 'Aca van los registros!'
    return HttpResponse (message)

class UnRegistroidUbicacion(generics.ListAPIView):
    serializer_class   = UbiSerializer
     
    def get_queryset(self):
        queryset = Ubicacion.objects.filter(codigoDivipolaMunicipio=self.kwargs['codigo_mun'])     
        return queryset

class MostarTodasUbicaciones(generics.ListAPIView):
    serializer_class   = UbiSerializer

    def get_queryset(self):
        queryset = Ubicacion.objects.all()     
        return queryset

class CrearUbicacion(generics.CreateAPIView):   
    serializer_class   = UbicacionSerializer
    

    def post(self, request, *args, **kwargs):                                                
        
        serializer = UbicacionSerializer(data=request.data)         
        serializer.is_valid(raise_exception=True)                                  
        serializer.save()                                                          

        return Response("Transacción exitosa", status=status.HTTP_201_CREATED)     

class ActualizarUbicacion(generics.UpdateAPIView):                                 
    serializer_class   = UbicacionSerializer
    queryset           = Ubicacion.objects.all()

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)              