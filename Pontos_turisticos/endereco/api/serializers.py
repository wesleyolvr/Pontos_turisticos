from rest_framework.serializers import ModelSerializer
from Pontos_turisticos.endereco.models import Endereco

class EnderecoSerializer(ModelSerializer):
    class Meta:
        model = Endereco
        fields = ('linha1','linha2','cidade','estado','pais',
                  'latitude','longitude')