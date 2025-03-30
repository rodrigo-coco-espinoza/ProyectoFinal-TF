from rest_framework.permissions import BasePermission, DjangoModelPermissions


class DjangoModelPermissionsWithView(DjangoModelPermissions):
    perms_map = {
        # sobreescribe el perms_map de DjangoModelPermissions
        # agrega el permiso 'view_%(model_name)s' a los permisos de 'GET'
        "GET": ["%(app_label)s.view_%(model_name)s"],
        "OPTIONS": [],
        "HEAD": [],
        "POST": ["%(app_label)s.add_%(model_name)s"],
        "PUT": ["%(app_label)s.change_%(model_name)s"],
        "PATCH": ["%(app_label)s.change_%(model_name)s"],
        "DELETE": ["%(app_label)s.delete_%(model_name)s"],
    }

