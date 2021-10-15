from django.conf                                      import settings
from rest_framework                                   import generics, status
from rest_framework.response                          import Response
from django.http import HttpResponse


from AppCovid19.models.seguimiento_de_cambios         import Seguimiento_de_cambios
from AppCovid19.serializers.seguimiento_Serializer    import SeguimientoCambiosSerializer

class CrearSeguimiento(generics.CreateAPIView):                                    #Crear un seguimiento
    serializer_class   = SeguimientoCambiosSerializer
    def post(self, request, *args, **kwargs):                                      #request: viene en el body del post. Se obtiene info con request.data[nombre de la llave]
            
        serializer = SeguimientoCambiosSerializer(data=request.data)               #pasamos del json que recibimos al objeto de tipo transacción
        serializer.is_valid(raise_exception=True)                                  #verificar si es valido
        serializer.save()                                                          #guarda al transacción en la bd

        return Response("Transacción exitosa", status=status.HTTP_201_CREATED)     #devuelve msj de transacción exitosa

class ConsultarUnSeguimiento(generics.ListAPIView):
    serializer_class   = SeguimientoCambiosSerializer
    def get_queryset(self):
        queryset = Seguimiento_de_cambios.objects.filter(id_evolucion=self.kwargs['pk'])     #De todos los segumientos, filtra el id = "pk" que viene en la url
        return queryset

class MostrarTodosSeguimientos(generics.ListAPIView):
    serializer_class   = SeguimientoCambiosSerializer
    def get_queryset(self):
        queryset = Seguimiento_de_cambios.objects.all()                                      #Trae  todos los seguimientos
        return queryset


class ActualizarSeguimiento(generics.UpdateAPIView):                                         #Actualizar un seguimiento
    serializer_class   = SeguimientoCambiosSerializer
    queryset           = Seguimiento_de_cambios.objects.all()
    def update(self, request, *args, **kwargs):     
        return super().update(request, *args, **kwargs)                                      #con esta línea se actualiza el registro de seguimiento
