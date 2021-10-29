from django.conf                                      import settings
from rest_framework                                   import generics, status
from rest_framework.response                          import Response
from AppCovid19.models.seguimiento_de_cambios         import Seguimiento_de_cambios
from AppCovid19.serializers.seguimiento_Serializer    import SeguimientoCambiosSerializer

class CrearSeguimiento(generics.CreateAPIView):                                    
    serializer_class   = SeguimientoCambiosSerializer
    def post(self, request, *args, **kwargs):                                      
            
        serializer = SeguimientoCambiosSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)                 
        serializer.save()                                                         

        return Response("Transacción exitosa", status=status.HTTP_201_CREATED)    

class ConsultarUnSeguimiento(generics.ListAPIView):
    serializer_class   = SeguimientoCambiosSerializer
    def get_queryset(self):
        queryset = Seguimiento_de_cambios.objects.filter(id_evolucion=self.kwargs['pk'])     
        return queryset

class MostrarTodosSeguimientos(generics.ListAPIView):
    serializer_class   = SeguimientoCambiosSerializer
    def get_queryset(self):
        queryset = Seguimiento_de_cambios.objects.all()                                   
        return queryset


class ActualizarSeguimiento(generics.UpdateAPIView):                                        
    serializer_class   = SeguimientoCambiosSerializer
    queryset           = Seguimiento_de_cambios.objects.all()
    def update(self, request, *args, **kwargs):     
        return super().update(request, *args, **kwargs)          