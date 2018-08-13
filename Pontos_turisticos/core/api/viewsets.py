from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth import get_user_model

from Pontos_turisticos.core.models import PontoTuristico
from .serializers import PontoturisticosSerializer, LoginSerializer

User = get_user_model()

class LoginViewSet(ModelViewSet):
    serializer_class = LoginSerializer
    permission_classes = (IsAdminUser,)
    queryset = User.objects.all()

class PontoTuristicoViewSet(ModelViewSet):
    serializer_class = PontoturisticosSerializer
    permission_classes = (IsAdminUser,)
    authentication_classes = (TokenAuthentication,)
    filter_backends = (SearchFilter,)
    search_fields = ('nome', 'descricao', 'enderecos__linha1')

    

    def get_queryset(self):
        return PontoTuristico.objects.filter(aprovado=True)

    def list(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).destroy(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).retrieve(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).partial_update(request, *args, **kwargs)

    @action(methods=['get'], detail=True)
    def denunciar(self, request, pk=None):
        pass
