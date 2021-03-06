from django.db import models

from Pontos_turisticos.atracoes.models import Atracao
from Pontos_turisticos.avaliacoes.models import Avaliacao
from Pontos_turisticos.comentarios.models import Comentario
from Pontos_turisticos.endereco.models import Endereco


class Doc_identificacao(models.Model):
    description= models.CharField(max_length=150)


class PontoTuristico(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    aprovado = models.BooleanField(default=False)
    atracoes = models.ManyToManyField(Atracao)
    comentarios = models.ManyToManyField(Comentario)
    avaliacoes = models.ManyToManyField(Avaliacao)
    enderecos = models.ForeignKey(Endereco, on_delete=models.CASCADE, null=True, blank=True)
    foto = models.ImageField(upload_to='pontoturisticos', null=True, blank=True)
    doc_identificacao = models.OneToOneField(
        Doc_identificacao, on_delete=models.CASCADE, null=True,blank=True
    )

    def __str__(self):
        return self.nome

    @property
    def descricao_completa2(self):
        return "%s %s " % (self.nome, self.descricao)
