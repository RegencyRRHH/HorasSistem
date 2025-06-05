from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmpresaViewSet, UnidadNegocioViewSet, ProyectoViewSet, CentroOperativoViewSet, CargoViewSet

router = DefaultRouter()
router.register(r'empresas', EmpresaViewSet)
router.register(r'unidades', UnidadNegocioViewSet)
router.register(r'proyectos', ProyectoViewSet)
router.register(r'centros-operativos', CentroOperativoViewSet)
router.register(r'cargos', CargoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]