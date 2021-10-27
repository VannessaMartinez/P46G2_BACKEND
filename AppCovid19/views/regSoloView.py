from django.conf                                        import settings
from rest_framework                                     import generics
from AppCovid19.models.registro_contagio                import Registro
from AppCovid19.serializers.regSoloSerializer           import RegSoloSerializer

class RegSolo(generics.ListAPIView):

    serializer_class = RegSoloSerializer
    
    def get_queryset(self):
        queryset = Registro.objects.all().order_by('id_caso').reverse()[:1]
        return queryset
