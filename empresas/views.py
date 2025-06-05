from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from .models import Empresa, UnidadNegocio, Proyecto, CentroOperativo, Cargo
from .serializers import EmpresaSerializer, UnidadNegocioSerializer, ProyectoSerializer, CentroOperativoSerializer, CargoSerializer

class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['nombre', 'nit', 'email']
    ordering_fields = ['nombre', 'creado_en']

class UnidadNegocioViewSet(viewsets.ModelViewSet):
    queryset = UnidadNegocio.objects.all()
    serializer_class = UnidadNegocioSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['nombre', 'empresa__nombre']
    ordering_fields = ['fecha_inicio', 'nombre']

    def get_queryset(self):
        queryset = super().get_queryset()
        empresa_id = self.request.query_params.get('empresa', None)
        if empresa_id:
            queryset = queryset.filter(empresa_id=empresa_id)
        return queryset

class ProyectoViewSet(viewsets.ModelViewSet):
    queryset = Proyecto.objects.all()
    serializer_class = ProyectoSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['nombre', 'unidades_negocio__nombre']
    ordering_fields = ['fecha_inicio', 'nombre']

    def get_queryset(self):
        queryset = super().get_queryset()
        unidad_id = self.request.query_params.get('unidad_negocio', None)
        if unidad_id:
            queryset = queryset.filter(unidades_negocio__id=unidad_id)
        return queryset

class CentroOperativoViewSet(viewsets.ModelViewSet):
    queryset = CentroOperativo.objects.all()
    serializer_class = CentroOperativoSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['nombre', 'ciudad', 'unidades_negocio__nombre']
    ordering_fields = ['nombre', 'ciudad']

    def get_queryset(self):
        queryset = super().get_queryset()
        unidad_id = self.request.query_params.get('unidad_negocio', None)
        if unidad_id:
            queryset = queryset.filter(unidades_negocio__id=unidad_id)
        return queryset

class CargoViewSet(viewsets.ModelViewSet):
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['nombre', 'centro_operativo__nombre']
    ordering_fields = ['nombre', 'creado_en']