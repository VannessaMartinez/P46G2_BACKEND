from django.conf                                      import settings
from rest_framework                                   import generics, status
from rest_framework.response                          import Response

from AppCovid19.serializers.regSerializer             import RegSerializer

class RegSegView(generics.CreateAPIView):

    serializer_class = RegSerializer

    def post(self, request, *args, **kwargs):
        serializer = RegSerializer (data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response("Transacción exitosa", status=status.HTTP_201_CREATED)