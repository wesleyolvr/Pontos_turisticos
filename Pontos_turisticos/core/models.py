from django.db import models

from atracoes.models import Atracao
from avaliacoes.models import Avaliacao
from comentarios.models import Comentario
from endereco.models import Endereco


class PontoTuristico(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    aprovado = models.BooleanField(default=False)
    atracoes = models.ManyToManyField(Atracao)
    comentarios = models.ManyToManyField(Comentario)
    avaliacoes = models.ManyToManyField(Avaliacao)
    enderecos = models.ForeignKey(Endereco, on_delete=models.CASCADE, null=True, blank=True)
    foto = models.ImageField(upload_to='pontoturisticos', null=True, blank=True)

    def __str__(self):
        return self.nome

    @property
    def descricao_completa2(self):
        return "%s %s " % (self.nome, self.descricao)
