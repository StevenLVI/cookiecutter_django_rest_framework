from rest_framework import permissions
from {{cookiecutter.app_name}}.constanst import CUSTOM
from {{cookiecutter.app_name}}.dependencies import (default_injector, UsersService)


class UsersPermissions(permissions.BasePermission):

    METHODS = ['POST', 'PUT', 'DELETE', 'PATCH']

    def has_permission(self, request, view):
        if CUSTOM in request.headers and request.headers[CUSTOM].isnumeric() and request.method in self.METHODS:
            user = default_injector.get(UsersService).get_user(int(request.headers[CUSTOM]))
            method = getattr(request, request.method)
            method._mutable = True
            method['user'] = user
        return True
