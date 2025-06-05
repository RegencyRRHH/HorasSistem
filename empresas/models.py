from django.db import models
from django.conf import settings

class Empresa(models.Model):
    nombre = models.CharField(max_length=200)
    nit = models.CharField(max_length=20, unique=True)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()
    activo = models.BooleanField(default=True)
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nombre} - {self.nit}"

class UnidadNegocio(models.Model):
    nombre = models.CharField(max_length=200)
    empresas = models.ManyToManyField('Empresa', related_name='unidades_negocio')
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(null=True, blank=True)
    responsable = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    activo = models.BooleanField(default=True)
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Unidad de Negocio'
        verbose_name_plural = 'Unidades de Negocio'

class Proyecto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    unidades_negocio = models.ManyToManyField(
        'UnidadNegocio',
        related_name='proyectos',
        verbose_name='Unidades de Negocio'
    )
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(null=True, blank=True)
    responsable = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name='proyectos_responsable'
    )
    activo = models.BooleanField(default=True)
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'
        ordering = ['-fecha_inicio', 'nombre']

class CentroOperativo(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    proyectos = models.ManyToManyField(
        'Proyecto',
        related_name='centros_operativos',
        verbose_name='Proyectos'
    )
    direccion = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=100)
    responsable = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name='centros_operativos_responsable'
    )
    activo = models.BooleanField(default=True)
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Centro Operativo'
        verbose_name_plural = 'Centros Operativos'
        ordering = ['nombre']

    def __str__(self):
        return f"{self.nombre} - {self.ciudad}"

class CargoPredefinido(models.Model):
    NIVEL_CARGO = [
        ('ALTO', 'Nivel Alto'),
        ('MEDIO', 'Nivel Medio'),
        ('OPERATIVO', 'Nivel Operativo'),
    ]

    AREA = [
        ('ADMINISTRATIVA', 'Área Administrativa'),
        ('OPERATIVA', 'Área Operativa'),
        ('COMERCIAL', 'Área Comercial'),
        ('TECNICA', 'Área Técnica'),
        ('OTROS', 'Otras Áreas'),
    ]

    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(help_text="Descripción general de las funciones del cargo")
    nivel = models.CharField(
        max_length=20,
        choices=NIVEL_CARGO,
        default='OPERATIVO',
        help_text="Nivel jerárquico del cargo"
    )
    area = models.CharField(
        max_length=20,
        choices=AREA,
        default='OTROS',
        help_text="Área funcional del cargo"
    )
    activo = models.BooleanField(default=True)
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nombre} - {self.get_nivel_display()} ({self.get_area_display()})"

    class Meta:
        verbose_name = 'Cargo Predefinido'
        verbose_name_plural = 'Cargos Predefinidos'
        ordering = ['area', 'nivel', 'nombre']
        unique_together = ['nombre', 'nivel']

class Cargo(models.Model):
    centro_operativo = models.ForeignKey(
        CentroOperativo,
        on_delete=models.CASCADE,
        related_name='cargos'
    )
    cargo_predefinido = models.ForeignKey(
        CargoPredefinido,
        on_delete=models.PROTECT,
        related_name='cargos_asignados'
    )
    descripcion_especifica = models.TextField(blank=True)
    activo = models.BooleanField(default=True)
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.cargo_predefinido.nombre} en {self.centro_operativo.nombre}"

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'
        ordering = ['cargo_predefinido__nivel', 'cargo_predefinido__nombre']
        unique_together = ['centro_operativo', 'cargo_predefinido']