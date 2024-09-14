from rest_framework import viewsets
from .models import (Cor,
                     MarcaModelo,
                     Veiculo,
                     Morador,
                     Lote,
                     Quadra,
                     Residencia,
                     Visitantes)

from .serializers import (CorSerializer,
                          MarcaModeloSerializer,
                          VeiculoSerializer,
                          MoradorSerializer,
                          LoteSerializer,
                          QuadraSerializer,
                          ResidenciaSerializer,
                          VisitanteSerializer)


class CorViewSet(viewsets.ModelViewSet):
    queryset = Cor.objects.all()
    serializer_class = CorSerializer


class MarcaModeloViewSet(viewsets.ModelViewSet):
    queryset = MarcaModelo.objects.all()
    serializer_class = MarcaModeloSerializer


class VeiculoViewSet(viewsets.ModelViewSet):
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer


class MoradorViewSet(viewsets.ModelViewSet):
    queryset = Morador.objects.all()
    serializer_class = MoradorSerializer


class LoteViewSet(viewsets.ModelViewSet):
    queryset = Lote.objects.all()
    serializer_class = LoteSerializer


class QuadraViewSet(viewsets.ModelViewSet):
    queryset = Quadra.objects.all()
    serializer_class = QuadraSerializer


class ResidenciaViewSet(viewsets.ModelViewSet):
    queryset = Residencia.objects.all()
    serializer_class = ResidenciaSerializer


class VisitanteViewSet(viewsets.ModelViewSet):
    queryset = Visitantes.objects.all()
    serializer_class = VisitanteSerializer
