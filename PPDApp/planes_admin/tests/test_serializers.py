from datetime import date
from django.db import IntegrityError

import pytest
from rest_framework.exceptions import ValidationError

from planes_admin.models import *
from planes_admin.serializers import *


@pytest.mark.django_db
class TestPlanSerializer:
    @pytest.fixture
    def plan_data(self):
        return {
            "nombre": "Gabriel",
            "anio": 2025,
            "resolucion": "1927-03-06",
        }

    def test_serializar_plan(self, plan_data):
        serializer = PlanSerializer(data=plan_data)
        assert serializer.is_valid()
        plan = serializer.save()
        assert plan.nombre == plan_data["nombre"]
        assert plan.anio == plan_data["anio"]
        assert plan.resolucion == plan_data["resolucion"]

    def test_serializar_plan_sin_anio(self):

        data = {"nombre": "Gabriel", "resolucion": "García Márquez"}
        serializer = PlanSerializer(data=data)
        #plan = serializer.save()
        with pytest.raises(ValidationError):
            serializer.is_valid(raise_exception=True)


    def test_validacion_nombre_max_length(self, plan_data):
        plan_data["nombre"] = "a" * 101  # Más del límite de 100 caracteres
        serializer = PlanSerializer(data=plan_data)
        assert not serializer.is_valid()
        assert "nombre" in serializer.errors

    def test_validacion_resolucion_max_length(self, plan_data):
        plan_data["resolucion"] = "a" * 51  # Más del límite de 100 caracteres
        serializer = PlanSerializer(data=plan_data)
        assert not serializer.is_valid()
        assert "resolucion" in serializer.errors

    def test_deserializar_plan(self):
        plan = Plan.objects.create(
            nombre="Gabriel",
            resolucion="García Márquez",
            anio=2025,
        )
        serializer = PlanSerializer(plan)
        data = serializer.data
        assert data["nombre"] == plan.nombre
        assert data["resolucion"] == plan.resolucion
        assert data["anio"] == 2025

