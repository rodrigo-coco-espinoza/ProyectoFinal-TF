from datetime import date

import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from planes_admin.models import *
from user.models import Usuario
from django.contrib.auth.models import Group, Permission

@pytest.fixture
def api_client_planificador():
    return APIClient()

@pytest.fixture
def plan_data():
    return {
        "nombre": "Gabriel",
        "resolucion": "García Márquez",
        "anio": 2025,
    }



@pytest.fixture
def plan(plan_data):
    return Plan.objects.create(**plan_data)

PASSWORD="12345678"
USERNAME="plan@ppda.cl"

@pytest.fixture
def crear_roles():
    roles = {
        "Administrador": ["add_comuna", "change_comuna", "delete_comuna", "view_comuna",
                          "add_organismo", "change_organismo", "delete_organismo", "view_organismo",
                          "add_medida", "change_medida", "delete_medida", "view_medida",
        ],
        "Planificador": ["add_plan", "change_plan", "delete_plan", "view_plan",
                         "view_medida",
                         "add_planmedida", "change_planmedida", "delete_planmedida", "view_planmedida",
                         ],
        "Agente": ["view_plan",
                   "view_medida",
                   "view_planmedida",
                   "change_reportemedida","add_reportemedida", "view_reportemedida"],
        "Lector": ["view_plan","view_medida", "view_planmedida", "view_reportemedida"],
    }
    for nombre_grupo, lista_permisos in roles.items():
        grupo, creado = Group.objects.get_or_create(name=nombre_grupo)

        # Agregar permisos al grupo
        if True:
            for codename in lista_permisos:
                permiso = Permission.objects.filter(codename=codename).first()
                if permiso:
                    grupo.permissions.add(permiso)

            grupo.save()

@pytest.fixture
def crear_usuario_admin(db):
    usuario = Usuario.objects.create_user(email="admin@ppda.cl", password=PASSWORD)
    grupo, creado = Group.objects.get_or_create(name="Administrador")

    usuario.groups.add(grupo)
    usuario.save()
    return usuario

@pytest.fixture
def jwt_token_admin(crear_usuario_admin, crear_roles):
    client = APIClient()
    response = client.post("/api/token/", {"email": "admin@ppda.cl", "password": PASSWORD})
    return response.data["access"]

@pytest.fixture
def api_client_admin(jwt_token_admin):
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {jwt_token_admin}')
    return client

@pytest.fixture
def crear_usuario_planificador(db):
    usuario = Usuario.objects.create_user(email=USERNAME, password=PASSWORD)
    grupo, creado = Group.objects.get_or_create(name="Planificador")

    usuario.groups.add(grupo)
    usuario.save()
    return usuario

@pytest.fixture
def jwt_token_planificador(crear_usuario_planificador, crear_roles):
    client = APIClient()
    response = client.post("/api/token/", {"email": USERNAME, "password": PASSWORD})
    return response.data["access"]

@pytest.fixture
def api_client_planificador(jwt_token_planificador):
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {jwt_token_planificador}')
    return client


def test_obtener_permisos(api_client_planificador, jwt_token_planificador):
    url = reverse("permisos")
    response = api_client_planificador.get(url)

    assert response.status_code == 200, f"❌ Error 401, respuesta: {response.data}"
    print("🔹 Permisos del usuario:", response.data["permisos"])

@pytest.mark.django_db
class TestPlanViewSet:
    def test_list_planes(self, api_client_planificador, plan):
        url = reverse("plan-list")
        response = api_client_planificador.get(url)
        print("🔹 Permisos requeridos por la API:", response)

        assert response.status_code == status.HTTP_200_OK
        #assert len(response.data) == 1

    def test_create_plan(self, api_client_planificador, plan_data):
        url = reverse("plan-list")
        response = api_client_planificador.post(url, plan_data, format="json")
        assert response.status_code == status.HTTP_201_CREATED
        assert Plan.objects.count() == 1

    def test_retrieve_plan(self, api_client_planificador, plan_data):
        plan = Plan.objects.create(**plan_data)
        url = reverse("plan-detail", args=[plan.id])
        response = api_client_planificador.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert response.data["nombre"] == plan_data["nombre"]

    def test_update_plan(self, api_client_planificador, plan_data):
        plan = Plan.objects.create(**plan_data)
        url = reverse("plan-detail", args=[plan.id])
        updated_data = plan_data.copy()
        updated_data["nombre"] = "Gabriel José"
        response = api_client_planificador.put(url, updated_data, format="json")
        assert response.status_code == status.HTTP_200_OK
        assert response.data["nombre"] == "Gabriel José"

    def test_delete_plan(self, api_client_planificador, plan_data):
        plan = Plan.objects.create(**plan_data)
        url = reverse("plan-detail", args=[plan.id])
        response = api_client_planificador.delete(url)
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert Plan.objects.count() == 0

    def test_create_plan_admin(self, api_client_admin, plan_data):
        # Se valida que el usuario admin no puede usar la API que crea planes
        url = reverse("plan-list")
        response = api_client_admin.post(url, plan_data, format="json")
        assert response.status_code == 403
        assert Plan.objects.count() == 0
