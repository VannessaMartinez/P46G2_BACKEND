from django.conf                                         import settings
from rest_framework                                      import generics, status
from rest_framework.response                             import Response
from AppCovid19.serializers.registroContagio_Serializer  import RegistroSerializer

class CrearRegistro(generics.CreateAPIView):
    serializer_class = RegistroSerializer
    def post(self, request, *args, **kwargs):
        serializer = RegistroSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response("Transacción exitosa", status=status.HTTP_201_CREATED)