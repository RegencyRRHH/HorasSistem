from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Rol

Usuario = get_user_model()

class UsuarioSerializer(serializers.ModelSerializer):
    groups = serializers.SerializerMethodField()

    def get_groups(self, obj):
        return [group.name for group in obj.groups.all()]

    class Meta:
        model = Usuario
        fields = ('id', 'username', 'email', 'groups')

class UsuarioCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Usuario
        fields = ('id', 'username', 'email', 'password', 'first_name', 
                 'last_name', 'telefono', 'direccion')

    def create(self, validated_data):
        password = validated_data.pop('password')
        usuario = Usuario(**validated_data)
        usuario.set_password(password)
        usuario.save()
        return usuario

class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = '__all__'