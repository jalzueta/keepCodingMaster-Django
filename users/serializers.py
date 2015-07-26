# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.Serializer):

    id = serializers.ReadOnlyField() #Solo lectura
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()

    def create(self, validated_data):
        """
        Crea una instancia de User a partir de los datos
        validated que contien valores deserializados
        :param validated_data:
        :return: objeto User
        """
        instance = User()
        return self.update(instance, validated_data)

    def update(self, instance, validated_data):
        """
        Actualiza una instancia de User a partir de los datos del diccionario 'validated_data'
        que contiene valores deserializados
        :param instance: User a actualizar
        :param validated_data: diccionario con nuevos valores para el User
        :return: objeto User actualizado
        """
        instance.first_name = validated_data.get('first_name')
        instance.last_name = validated_data.get('last_name')
        instance.username = validated_data.get('username')
        instance.email = validated_data.get('email')
        instance.set_password(
            validated_data.get('password')
        )
        instance.save() # lo guardamos en la BB.DD.
        return instance

    # método para validar el campo username
    def validate_username(self, data):
        """
        Valida si existe un usuario con ese username
        :param data: username que se quiere comprobar
        :return: username creado o error de validacion
        """

        users = User.objects.filter(username=data)

         # Si estoy creando un usuario (no hay instancia) comprobar si hay usuarios con ese username
        if not self.instance:
            return data
        elif not self.instance and len(users) != 0:
            raise serializers.ValidationError("Ya existe un usuario con ese username")
        # Si estoy acualizando, el nuevo usuario es diferente al de la instancia (está cambiado el username)
        # y existen usuarios ya registrados con el nuevo username
        elif self.instance.username != data and len(users) != 0:
            raise serializers.ValidationError("El username '{0}' no está disponible".format(data))
        else:
            return data
