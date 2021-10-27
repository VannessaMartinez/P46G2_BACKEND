from AppCovid19.models.registro_contagio      import Registro
from AppCovid19.models.ubicacion              import Ubicacion
from rest_framework                           import serializers

class RegSoloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registro
        fields = ['id_caso', 'codigo_divipola_municipio_fk', 'fecha_notificacion', 'fecha_reporte', 'fecha_sintomas', 'fecha_diagnostico_lab',
        'edad', 'unidad_de_medida_edad', 'sexo', 'grupo_etnico', 'pertenencia_etnica', 'fecha_recuperacion', 'tipo_recuperacion']

    def to_representation(self, obj):
        ubicacion   = Ubicacion.objects.get(codigoDivipolaMunicipio=obj.codigo_divipola_municipio_fk_id)
        registro    = Registro.objects.get(id_caso=obj.id_caso)
        
        return {
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