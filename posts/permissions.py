# -*- coding: utf-8 -*-
from rest_framework.permissions import BasePermission
from posts.views import PUBLICADO

class PostPermission(BasePermission):

    def has_permission(self, request, view):
        """
        Define si el usuario autenticado en request.user tiene
        permiso para realizar la accion (GET, POST, PUT, DELETE)
        :param request:
        :param view: controlador sobre el que se ejecuta la peticion
        :return: Boolean
        """
        # Importamos aquí para evitar la dependencia cíclica que teníamos con los import entre esta clase y api.py
        from posts.api import PostDetailAPI

        # Cualquiera puede leer un post si es 'PUB'
        if request.method == "GET":
            return True

        # Un usuario super-admin puede hacer cualquier cosa
        elif request.user.is_superuser:
            return True

        # Si la vista es una vista de detalle de usuario (no de listado), delego la decision al metodo de abajo
        elif isinstance(view, PostDetailAPI):
            return True

        # Si es un 'GET' a /api/1.0/users/
        else:
            return False


    # Si 'has_permission' devuelve True, entonces se evalua este metodo
    def has_object_permission(self, request, view, obj):
        """
        Define si el usuario autenticado en request.user tiene
        permiso para realizar la accion (GET, PUT, DELETE)
        sobre el objeto 'obj'
        :param request:
        :param view:
        :param obj:
        :return:
        """

        # Si es superadmin, o el usuario autenticado es el mismo que el usuario
        # sobre el que se ejecuta la petición
        if request.method == "GET":
            if obj.status == PUBLICADO:
                return True
            else:
                return request.user.is_superuser or request.user == obj.blog.author

        else:
            return request.user.is_superuser or request.user == obj.blog.author


