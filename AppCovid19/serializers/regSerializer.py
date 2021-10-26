from AppCovid19.models.registro_contagio      import Registro
from AppCovid19.models.ubicacion              import Ubicacion
from AppCovid19.models.seguimiento_de_cambios import Seguimiento_de_cambios
from AppCovid19.serializers.segSerializer     import SegSerializer, Seguimiento_de_cambios
from rest_framework                           import serializers

class RegSerializer(serializers.ModelSerializer):

    seguimiento = SegSerializer()

    class Meta:
        model = Registro
        fields = ['id_caso', 'codigo_divipola_municipio_fk', 'fecha_notificacion',
                  'fecha_reporte', 'fecha_sintomas', 'fecha_diagnostico_lab',
                  'edad', 'unidad_de_medida_edad', 'sexo', 'grupo_etnico',
                  'pertenencia_etnica', 'fecha_recuperacion', 'tipo_recuperacion','seguimiento']

    def to_representation(self, obj):
        ubicacion           = Ubicacion.objects.get(codigoDivipolaMunicipio=obj.codigo_divipola_municipio_fk_id)
        registro            = Registro.objects.get(id_caso=obj.id_caso)
        seguimiento_cambios = Seguimiento_de_cambios.objects.get(id_caso_fk=obj.id_caso)
        
        return {
            'codigo_divipola_municipio_fk'      :registro.codigo_divipola_municipio_fk_id,
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

            'seguimiento'                       : {
                'id_caso_fk'                    : seguimiento_cambios.id_caso_fk_id, 
                'ubicacion_caso'                : seguimiento_cambios.ubicacion_caso,
                'estado'                        : seguimiento_cambios.estado,
                'tipo_contagio'                 : seguimiento_cambios.tipo_contagio,
                'recuperado'                    : seguimiento_cambios.recuperado,
                'fecha_muerte'                  : seguimiento_cambios.fecha_muerte
            }
        }