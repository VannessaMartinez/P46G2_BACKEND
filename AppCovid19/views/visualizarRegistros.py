from django.conf                                         import settings
from rest_framework                                      import generics,status
from AppCovid19.models.registro_contagio                 import Registro
from AppCovid19.serializers.registroContagio_Serializer  import RegistroSerializer
from AppCovid19.serializers.ubiSerializer                import UbiSerializer
from rest_framework.response                             import Response


class MostarRegistros(generics.ListAPIView):
    serializer_class   = RegistroSerializer
    def get_queryset(self):
        queryset = Registro.objects.all()     #De todas las transacciones, filtra aquellas con cuenta origen = "account" que viene en la url
        return queryset

class Ubi(generics.CreateAPIView):
    serializer_class = UbiSerializer

    def post(self, request, *args, **kwargs):                                      #request: viene en el body del post. Se obtiene info con request.data[nombre de la llave]
            
        serializer = UbiSerializer(data=request.data)                        #pasamos del json que recibimos al objeto de tipo transacción
        serializer.is_valid(raise_exception=True)                                  #verificar si es valido
        serializer.save()                                                          #guarda al transacción en la bd

        return Response("Transacción exitosa", status=status.HTTP_201_CREATED)