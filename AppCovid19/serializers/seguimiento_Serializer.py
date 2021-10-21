from AppCovid19.models.registro_contagio        import Registro
from AppCovid19.models.seguimiento_de_cambios   import Seguimiento_de_cambios
from AppCovid19.models.ubicacion                import Ubicacion
from rest_framework                             import serializers

class SeguimientoCambiosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seguimiento_de_cambios
        fields = ['id_evolucion', 'id_caso_fk', 'ubicacion_caso', 'estado', 'tipo_contagio', 'recuperado', 'fecha_muerte']
    
    def to_representation(self, obj):
        seguimiento_cambios = Seguimiento_de_cambios.objects.get(id_caso_fk=obj.id_caso_fk)
        registro            = Registro.objects.get(id_caso=obj.id_caso_fk_id)
        ubicacion           = Ubicacion.objects.get(codigoDivipolaMunicipio=obj.id_caso_fk.id_caso)
        return {
            'id_evolucion'            : seguimiento_cambios.id_evolucion,
            'id_caso_fk'              : registro.id_caso,
            'ubicacion_caso'          : seguimiento_cambios.ubicacion_caso,
            'estado'                  : seguimiento_cambios.estado,
            'tipo_contagio'           : seguimiento_cambios.tipo_contagio,
            'recuperado'              : seguimiento_cambios.recuperado,
            'fecha_muerte'            : seguimiento_cambios.fecha_muerte,
            'registro'                : {
                'id_caso'                           :registro.id_caso,
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
                'tipo_recuperacion'                 :registro.tipo_recuperacion                
            },
            'ubicacion'                     : { 
                'codigoDivipolaMunicipio'       : ubicacion.codigoDivipolaMunicipio,
                'codigo_iso_pais'               : ubicacion.codigo_iso_pais,
                'nombre_pais'                   : ubicacion.nombre_pais,
                'codigo_divipola_departamento'  : ubicacion.codigo_divipola_departamento,
                'nombre_departamento'           : ubicacion.nombre_departamento,
                'nombre_municipio'              : ubicacion.nombre_municipio
            }
        }
