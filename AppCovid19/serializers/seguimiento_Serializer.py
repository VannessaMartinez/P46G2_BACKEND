from AppCovid19.models.seguimiento_de_cambios import Seguimiento_de_cambios
from AppCovid19.models.registro_contagio      import Registro
from rest_framework                           import serializers

class SeguimientoCambiosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seguimiento_de_cambios
        fields = ['id_evolucion', 'ubicacion_caso', 'estado', 'tipo_contagio', 'recuperado', 'fecha_muerte']
    
    def to_representation(self, obj):
        seguimiento_cambios = Seguimiento_de_cambios.objects.get(id_evolucion=obj.id_evolucion)
        return {
            'id_evolucion'            : seguimiento_cambios.id_evolucion,
            'ubicacion_caso'          : seguimiento_cambios.ubicacion_caso,
            'estado'                  : seguimiento_cambios.estado,
            'tipo_contagio'           : seguimiento_cambios.tipo_contagio,
            'recuperado'              : seguimiento_cambios.recuperado,
            'fecha_muerte'            : seguimiento_cambios.fecha_muerte,
        }