"""virtual URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from atracoes.api.viewsets import AtracaoViewSet
from avaliacoes.api.viewsets import AvaliacaoViewSet
from comentarios.api.viewsets import ComentarioViewSet
from core.api.viewsets import PontoTuristicoViewSet
from core.models import PontoTuristico
from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from endereco.api.viewsets import EnderecoViewSet
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register(r'pontoturistico', PontoTuristicoViewSet, base_name=PontoTuristico)
router.register(r'atracoes', AtracaoViewSet)
router.register(r'enderecos', EnderecoViewSet)
router.register(r'comentarios', ComentarioViewSet)
router.register(r'avaliacoes', AvaliacaoViewSet)



urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-token-auth/',obtain_auth_token),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
