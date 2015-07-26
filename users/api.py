# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from rest_framework.response import Response
from users.serializers import UserSerializer
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.generics import GenericAPIView
from users.permissions import UserPermission
from blogs.models import Blog

# hereda de 'GenericAPIView' habilitamos la autorización basada en clases
class UserListAPI(GenericAPIView):

    permission_classes = (UserPermission,)
    # No es necesario hacer la comprobación de permisos de forma manual 'check_object_permissions'
    # porque, aunque estamos heredando de una GenericAPIView, no se está accediendo a ningún
    # objeto concreto de la BB.DD sobre el que se deba hacer la comprobación 'has_object_permission'

    # 'get': metodo para recuperar usuarios de la BB.DD.
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True) # 'many=True' para cuando hay que serializar varios objetos
        # 'serializer.data' -> cada objeto serializado pasa a ser un diccionario con las 'keys' definidas en el serializador
        serializer_users = serializer.data
        return Response(serializer_users)

    # 'post': metodo para crear usuarios en la BB.DD. (misma url que el 'get')
    def post(self, request):
        serializer = UserSerializer(data=request.data) # se inicializa el serializer con los datos que me llegan por http mediante POST
        if serializer.is_valid():
            new_user = serializer.save() # Guarda el objeto en BB.DD. y me lo devuelve
            new_blog = Blog()
            new_blog.name = 'El blog de {0} {1}'.format(request.data.get('first_name'), request.data.get('last_name'))
            new_blog.author = new_user
            new_blog.save()
            # serializer almacena los datos en 'serializer.data'
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            # serializer almacena los errores en 'serializer.errors'
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetailAPI(GenericAPIView):

    permission_classes = (UserPermission,)

    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk) # devuelve el objeto o, si este no existe, un error 404

        # compruebo si el usuario autenticado puede hacer GET en este user.
        # Hay que hacerlo a mano porque estamos heredando de una GenericAPIView.
        # Al hacer la recuperación del objeto 'user' manualmente, la comprobacion tambien debe ser manual
        self.check_object_permissions(request, user)

        serializer = UserSerializer(user)
        serializer_user = serializer.data
        return Response(serializer_user)

    # Actualizacion de un usuario
    def put(self, request, pk):
        user = get_object_or_404(User, pk=pk) # devuelve el objeto o, si este no existe, un error 404

        # compruebo si el usuario autenticado puede hacer PUT en este user
        # Hay que hacerlo a mano porque estamos heredando de una GenericAPIView
        # Al hacer la recuperación del objeto 'user' manualmente, la comprobacion tambien debe ser manual
        self.check_object_permissions(request, user)

        serializer = UserSerializer(instance=user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Borrado de un usuario
    def delete(self, request, pk):
        user = get_object_or_404(User, pk=pk) # devuelve el objeto o, si este no existe, un error 404

        # compruebo si el usuario autenticado puede hacer DELETE en este user
        # Hay que hacerlo a mano porque estamos heredando de una GenericAPIView
        # Al hacer la recuperación del objeto 'user' manualmente, la comprobacion tambien debe ser manual
        self.check_object_permissions(request, user)

        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)