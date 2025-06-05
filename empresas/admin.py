from django.contrib import admin
from .models import Empresa, UnidadNegocio, Proyecto, CentroOperativo, CargoPredefinido, Cargo

@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'nit', 'email', 'activo')
    search_fields = ('nombre', 'nit')
    list_filter = ('activo',)

@admin.register(UnidadNegocio)
class UnidadNegocioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'get_empresas', 'fecha_inicio', 'activo')
    list_filter = ('activo', 'fecha_inicio')
    search_fields = ('nombre', 'empresas__nombre')
    filter_horizontal = ('empresas',)

    def get_empresas(self, obj):
        return ", ".join([empresa.nombre for empresa in obj.empresas.all()])
    get_empresas.short_description = 'Empresas'

@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'get_unidades_negocio', 'fecha_inicio', 'responsable', 'activo')
    list_filter = ('activo', 'fecha_inicio', 'unidades_negocio')
    search_fields = ('nombre', 'unidades_negocio__nombre', 'unidades_negocio__empresas__nombre')
    filter_horizontal = ('unidades_negocio',)
    readonly_fields = ('get_empresas_relacionadas',)

    def get_unidades_negocio(self, obj):
        return ", ".join([un.nombre for un in obj.unidades_negocio.all()])
    get_unidades_negocio.short_description = 'Unidades de Negocio'

    def get_empresas_relacionadas(self, obj):
        empresas = set()
        for unidad in obj.unidades_negocio.all():
            empresas.update(unidad.empresas.all())
        return ", ".join([emp.nombre for emp in empresas])
    get_empresas_relacionadas.short_description = 'Empresas Relacionadas'

    fieldsets = (
        (None, {
            'fields': ('nombre', 'descripcion', 'fecha_inicio', 'fecha_fin', 'responsable', 'activo')
        }),
        ('Relaciones', {
            'fields': ('unidades_negocio', 'get_empresas_relacionadas'),
            'classes': ('collapse',)
        }),
    )

@admin.register(CentroOperativo)
class CentroOperativoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'ciudad', 'get_proyectos', 'responsable', 'activo')
    list_filter = ('activo', 'ciudad', 'proyectos')
    search_fields = ('nombre', 'ciudad', 'proyectos__nombre')
    filter_horizontal = ('proyectos',)

    def get_proyectos(self, obj):
        return ", ".join([proyecto.nombre for proyecto in obj.proyectos.all()])
    get_proyectos.short_description = 'Proyectos'

    fieldsets = (
        (None, {
            'fields': ('nombre', 'descripcion', 'direccion', 'ciudad', 'responsable', 'activo')
        }),
        ('Relaciones', {
            'fields': ('proyectos',),
            'classes': ('collapse',)
        }),
    )

@admin.register(CargoPredefinido)
class CargoPredefinidoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'nivel', 'area', 'activo')
    list_filter = ('nivel', 'area', 'activo')
    search_fields = ('nombre', 'descripcion')
    ordering = ('area', 'nivel', 'nombre')

@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('cargo_predefinido', 'centro_operativo', 'activo')
    list_filter = ('cargo_predefinido__nivel', 'cargo_predefinido__area', 'centro_operativo', 'activo')
    search_fields = ('cargo_predefinido__nombre', 'centro_operativo__nombre')
    ordering = ('cargo_predefinido__nivel', 'cargo_predefinido__nombre')