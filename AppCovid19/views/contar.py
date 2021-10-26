from django.conf                                         import settings
from rest_framework                                      import generics
from AppCovid19.models.registro_contagio                 import Registro
from AppCovid19.serializers.registroContagio_Serializer  import RegistroSerializer
from rest_framework.response                             import Response
from rest_framework                                      import generics, status



class Contar(generics.ListAPIView):
    serializer_class   = RegistroSerializer
    def get_queryset(self):
        queryset = Registro.objects.all()
        numero = len(queryset)
        num = str(numero)    
        return Response(num,status=status.HTTP_200_OK)