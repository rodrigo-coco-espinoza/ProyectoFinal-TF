from rest_framework.permissions import BasePermission, DjangoModelPermissions
import json
from django.forms.models import model_to_dict


class DjangoModelPermissionsWithRead(DjangoModelPermissions):
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

class EsMismoOrganismo(BasePermission):
    """
    Permite la edición solo si el usuario pertenece al mismo organismo que el objeto PlanMedida.
    """

    def has_permission(self, request, view):
        # Verificar si el usuario está autenticado
        if not request.user.is_authenticated:
            return False
        # Permitir lectura a todos

        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True

        planmedida_id = request.data.get("medida")
        if not planmedida_id:
            return False  # No se puede insertar sin referencia a PlanMedida

        from planes_admin.models import PlanMedida

        try:
            plan_medida = PlanMedida.objects.get(id=planmedida_id)
        except PlanMedida.DoesNotExist:
            return False

        # Comparar el organismo del usuario con el del PlanMedida
        return request.user.organismo == plan_medida.organismo






