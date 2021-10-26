from AppCovid19.models.registro_contagio        import Registro
from AppCovid19.models.seguimiento_de_cambios   import Seguimiento_de_cambios
from rest_framework                             import serializers

class SegSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seguimiento_de_cambios
        fields = ['id_caso_fk','ubicacion_caso', 'estado', 'tipo_contagio',
                     'recuperado', 'fecha_muerte']
    
    def to_representation(self, obj):
        seguimiento_cambios = Seguimiento_de_cambios.objects.get(id_caso_fk=obj.id_caso_fk)
        registro            = Registro.objects.get(id_caso=obj.id_caso_fk_id)
        
        return {
            'id_caso_fk'              : seguimiento_cambios.id_caso_fk,
            'ubicacion_caso'          : seguimiento_cambios.ubicacion_caso,
            'estado'                  : seguimiento_cambios.estado,
            'tipo_contagio'           : seguimiento_cambios.tipo_contagio,
            'recuperado'              : seguimiento_cambios.recuperado,
            'fecha_muerte'            : seguimiento_cambios.fecha_muerte,
        }
