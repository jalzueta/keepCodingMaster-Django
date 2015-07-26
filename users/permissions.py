# -*- coding: utf-8 -*-
from rest_framework.permissions import BasePermission

class UserPermission(BasePermission):

    def has_permission(self, request, view):
        """
        Define si el usuario autenticado en request.user tiene
        permiso para realizar la accion (GET, POST, PUT, DELETE)
        :param request:
        :param view: controlador sobre el que se ejecuta la peticion
        :return: Boolean
        """
        # Importamos aquí para evitar la depenndencia cíclica que teníamos con los import entre esta clase y api.py
        from users.api import UserDetailAPI

        # Cualquiera puede crear un nuevo usuario
        if request.method == "POST":
            return True

        # Un usuario super-admin puede hacer cualquier cosa
        elif request.user.is_superuser:
            return True

        # Si la vista es una vista de detalle de usuario (no de listado), delego la decision al metodo de abajo
        elif isinstance(view, UserDetailAPI):
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
        return request.user.is_superuser or request.user == obj


