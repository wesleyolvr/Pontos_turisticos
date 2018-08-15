from django.contrib.auth.models import User
from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from endereco.api.serializers import EnderecoSerializer
from atracoes.api.serializers import AtracaoSerializer
from avaliacoes.api.serializers import AvaliacaoSerializer
from comentarios.api.serializers import ComentarioSerializer
from core.models import PontoTuristico
from atracoes.models import Atracao
from endereco.models import Endereco
from core.models import Doc_identificacao


class Doc_identificacaoSerializer(ModelSerializer):
    class Meta:
        model = Doc_identificacao
        fields = '__all__'


class PontoturisticosSerializer(ModelSerializer):
    atracoes = AtracaoSerializer(many=True)
    avaliacoes = AvaliacaoSerializer(many=True,read_only=True)
    enderecos = EnderecoSerializer()
    comentarios = ComentarioSerializer(many=True,read_only=True)
    descricao_completa = SerializerMethodField()
    doc_identificacao = Doc_identificacaoSerializer()


    class Meta:
        model = PontoTuristico
        fields = ('id', 'nome', 'descricao', 'aprovado', 'foto',
                  'atracoes', 'comentarios', 'enderecos',
                  'descricao_completa','descricao_completa2','avaliacoes','doc_identificacao'
                  )
        read_only_fields = ('atracoes','enderecos')


    def cria_atracoes(self,atracoes,ponto):
        for atracao in atracoes:
            at = Atracao.objects.create(**atracao)
            ponto.atracoes.add(at)


    def create(self, validated_data):
        atracoes = validated_data['atracoes']
        del validated_data['atracoes']

        endereco = validated_data['enderecos']
        del validated_data['enderecos']
        end = Endereco.objects.create(**endereco)

        doc = validated_data['doc_identificacao']
        del validated_data['doc_identificacao']
        doci = Doc_identificacao.objects.create(**doc)

        ponto = PontoTuristico.objects.create(**validated_data)
        self.cria_atracoes(atracoes,ponto)

        ponto.enderecos = end
        ponto.doc_identificacao=doci

        ponto.save()


        return ponto


    def get_descricao_completa(self,obj):
        return "%s %s" % (obj.nome,obj.descricao)



