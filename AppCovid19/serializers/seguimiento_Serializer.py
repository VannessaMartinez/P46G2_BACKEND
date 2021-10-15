from AppCovid19.models.registro_contagio import Registro
from AppCovid19.models.seguimiento_de_cambios import Seguimiento_de_cambios
from rest_framework                           import serializers

class SeguimientoCambiosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seguimiento_de_cambios
        fields = ['id_evolucion', 'id_caso_fk', 'ubicacion_caso', 'estado', 'tipo_contagio', 'recuperado', 'fecha_muerte']
    
    def to_representation(self, obj):
        seguimiento_cambios = Seguimiento_de_cambios.objects.get(id_caso_fk=obj.id_caso_fk)
        registro            = Registro.objects.get(id_caso=obj.id_caso_fk_id)
        return {
            'id_evolucion'            : seguimiento_cambios.id_evolucion,
            'id_caso_fk'              : registro.id_caso,
            'ubicacion_caso'          : seguimiento_cambios.ubicacion_caso,
            'estado'                  : seguimiento_cambios.estado,
            'tipo_contagio'           : seguimiento_cambios.tipo_contagio,
            'recuperado'              : seguimiento_cambios.recuperado,
            'fecha_muerte'            : seguimiento_cambios.fecha_muerte,
            'registro'                : {
                'fecha_notificacion'                :registro.fecha_notificacion,
                'fecha_reporte'                     :registro.fecha_reporte,
                'fecha_sintomas'                    :registro.fecha_sintomas,
                'fecha_diagnostico_lab'             :registro.fecha_diagnostico_lab,
                'edad'                              :registro.edad,
                'unidad_de_medida_edad'             :registro.unidad_de_medida_edad,
                'sexo'                              :registro.sexo,
                'grupo_etnico'                      :registro.grupo_etnico,
                'pertenencia_etnica'                :registro.pertenencia_etnica,
                'fecha_recuperacion'                :registro.fecha_recuperacion,
                'tipo_recuperacion'                 :registro.tipo_recuperacion,
            }
        }