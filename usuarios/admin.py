from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

Usuario = get_user_model()

@admin.register(Usuario)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'get_full_name', 'is_active', 'get_groups')
    list_filter = ('is_active', 'groups', 'is_staff')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    ordering = ('username',)
    filter_horizontal = ('groups', 'user_permissions')

    fieldsets = (
        ('Información Personal', {
            'fields': ('username', 'password', 'first_name', 'last_name', 'email')
        }),
        ('Permisos', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
            'classes': ('collapse',)
        }),
        ('Fechas Importantes', {
            'fields': ('last_login', 'date_joined'),
            'classes': ('collapse',)
        }),
    )

    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}".strip() or "-"
    get_full_name.short_description = "Nombre Completo"

    def get_groups(self, obj):
        return ", ".join([group.name for group in obj.groups.all()]) or "-"
    get_groups.short_description = "Grupos"
