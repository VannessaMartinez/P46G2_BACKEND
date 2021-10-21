from AppCovid19.models import Ubicacion
from rest_framework    import serializers
from AppCovid19.models import Registro
from AppCovid19.models import Registro

class UbiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ubicacion,Registro
        fields = ['codigoDivipolaMunicipio', 'codigo_iso_pais', 'nombre_pais', 'codigo_divipola_departamento', 'nombre_departamento', 'nombre_municipio']
                       
    def to_representation(self, obj):
        ubicacion  = Ubicacion.objects.get(codigoDivipolaMunicipio=obj.codigoDivipolaMunicipio)
        registro   = Registro.objects.get(codigo_divipola_municipio_fk=obj.codigoDivipolaMunicipio)
    
        return {
            'codigoDivipolaMunicipio'       : ubicacion.codigoDivipolaMunicipio,
            'codigo_iso_pais'               : ubicacion.codigo_iso_pais,
            'nombre_pais'                   : ubicacion.nombre_pais,
            'codigo_divipola_departamento'  : ubicacion.codigo_divipola_departamento,
            'nombre_departamento'           : ubicacion.nombre_departamento,
            'nombre_municipio'              : ubicacion.nombre_municipio,
            
            'registro' : {
            'id_caso'                           :registro.id_caso,
            'codigo_divipola_municipio_fk'      :ubicacion.codigoDivipolaMunicipio,
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
            }
        }
