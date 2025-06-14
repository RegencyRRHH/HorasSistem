# Generated by Django 5.0.2 on 2025-06-04 21:57

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('nit', models.CharField(max_length=20, unique=True)),
                ('direccion', models.CharField(max_length=200)),
                ('telefono', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('activo', models.BooleanField(default=True)),
                ('creado_en', models.DateTimeField(auto_now_add=True)),
                ('actualizado_en', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='CargoPredefinido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True)),
                ('descripcion', models.TextField(help_text='Descripción general de las funciones del cargo')),
                ('nivel', models.CharField(choices=[('ALTO', 'Nivel Alto'), ('MEDIO', 'Nivel Medio'), ('OPERATIVO', 'Nivel Operativo')], default='OPERATIVO', help_text='Nivel jerárquico del cargo', max_length=20)),
                ('area', models.CharField(choices=[('ADMINISTRATIVA', 'Área Administrativa'), ('OPERATIVA', 'Área Operativa'), ('COMERCIAL', 'Área Comercial'), ('TECNICA', 'Área Técnica'), ('OTROS', 'Otras Áreas')], default='OTROS', help_text='Área funcional del cargo', max_length=20)),
                ('activo', models.BooleanField(default=True)),
                ('creado_en', models.DateTimeField(auto_now_add=True)),
                ('actualizado_en', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Cargo Predefinido',
                'verbose_name_plural': 'Cargos Predefinidos',
                'ordering': ['area', 'nivel', 'nombre'],
                'unique_together': {('nombre', 'nivel')},
            },
        ),
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField(blank=True, null=True)),
                ('activo', models.BooleanField(default=True)),
                ('creado_en', models.DateTimeField(auto_now_add=True)),
                ('actualizado_en', models.DateTimeField(auto_now=True)),
                ('responsable', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='proyectos_responsable', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Proyecto',
                'verbose_name_plural': 'Proyectos',
                'ordering': ['-fecha_inicio', 'nombre'],
            },
        ),
        migrations.CreateModel(
            name='CentroOperativo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('direccion', models.CharField(max_length=200)),
                ('ciudad', models.CharField(max_length=100)),
                ('activo', models.BooleanField(default=True)),
                ('creado_en', models.DateTimeField(auto_now_add=True)),
                ('actualizado_en', models.DateTimeField(auto_now=True)),
                ('responsable', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='centros_operativos_responsable', to=settings.AUTH_USER_MODEL)),
                ('proyectos', models.ManyToManyField(related_name='centros_operativos', to='empresas.proyecto', verbose_name='Proyectos')),
            ],
            options={
                'verbose_name': 'Centro Operativo',
                'verbose_name_plural': 'Centros Operativos',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='UnidadNegocio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField(blank=True, null=True)),
                ('activo', models.BooleanField(default=True)),
                ('creado_en', models.DateTimeField(auto_now_add=True)),
                ('actualizado_en', models.DateTimeField(auto_now=True)),
                ('empresas', models.ManyToManyField(related_name='unidades_negocio', to='empresas.empresa')),
                ('responsable', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Unidad de Negocio',
                'verbose_name_plural': 'Unidades de Negocio',
            },
        ),
        migrations.AddField(
            model_name='proyecto',
            name='unidades_negocio',
            field=models.ManyToManyField(related_name='proyectos', to='empresas.unidadnegocio', verbose_name='Unidades de Negocio'),
        ),
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion_especifica', models.TextField(blank=True)),
                ('activo', models.BooleanField(default=True)),
                ('creado_en', models.DateTimeField(auto_now_add=True)),
                ('actualizado_en', models.DateTimeField(auto_now=True)),
                ('cargo_predefinido', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cargos_asignados', to='empresas.cargopredefinido')),
                ('centro_operativo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cargos', to='empresas.centrooperativo')),
            ],
            options={
                'verbose_name': 'Cargo',
                'verbose_name_plural': 'Cargos',
                'ordering': ['cargo_predefinido__nivel', 'cargo_predefinido__nombre'],
                'unique_together': {('centro_operativo', 'cargo_predefinido')},
            },
        ),
    ]
