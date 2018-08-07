from django.contrib.auth.models import User
from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from atracoes.api.serializers import AtracaoSerializer
from core.models import PontoTuristico


class PontoturisticosSerializer(ModelSerializer):
    atracoes = AtracaoSerializer(many=True)
    descricao_completa = SerializerMethodField()

    class Meta:
        model = PontoTuristico
        fields = ('id', 'nome', 'descricao', 'aprovado', 'foto',
                  'atracoes', 'comentarios', 'avaliacoes', 'enderecos',
                  'descricao_completa','descricao_completa2'
                  )

    def get_descricao_completa(self,obj):
        return "%s %s" % (obj.nome,obj.descricao)


class LoginSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('')
