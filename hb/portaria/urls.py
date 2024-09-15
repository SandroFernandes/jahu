from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (CorViewSet,
                    MarcaModeloViewSet,
                    VeiculoViewSet,
                    MoradorViewSet,
                    LoteViewSet,
                    QuadraViewSet,
                    ResidenciaViewSet,
                    VisitanteViewSet)


router = DefaultRouter()
router.register(r'cor', CorViewSet)
router.register(r'marca-modelo', MarcaModeloViewSet)
router.register(r'veiculo', VeiculoViewSet)
router.register(r'morador', MoradorViewSet)
router.register(r'lote', LoteViewSet)
router.register(r'quadra', QuadraViewSet)
router.register(r'residencia', ResidenciaViewSet)
router.register(r'visitante', VisitanteViewSet)


urlpatterns = [
    path('api/v1/', include(router.urls)),
]
