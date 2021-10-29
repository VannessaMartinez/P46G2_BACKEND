from AppCovid19.models import Ubicacion
from rest_framework    import serializers

class UbiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ubicacion
        fields = ['codigoDivipolaMunicipio', 'codigo_iso_pais', 'nombre_pais', 'codigo_divipola_departamento', 'nombre_departamento', 'nombre_municipio']
    
    def to_representation(self, obj):
        ubicacion  = Ubicacion.objects.get(codigoDivipolaMunicipio=obj.codigoDivipolaMunicipio)
        
        return {
            'codigoDivipolaMunicipio'       : ubicacion.codigoDivipolaMunicipio,
            'codigo_iso_pais'               : ubicacion.codigo_iso_pais,
            'nombre_pais'                   : ubicacion.nombre_pais,
            'codigo_divipola_departamento'  : ubicacion.codigo_divipola_departamento,
            'nombre_departamento'           : ubicacion.nombre_departamento,
            'nombre_municipio'              : ubicacion.nombre_municipio
        }