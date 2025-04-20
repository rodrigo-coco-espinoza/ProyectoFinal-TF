from datetime import date

import pytest
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.conf import settings

from planes_admin.models import *


@pytest.mark.django_db
class TestplanModel:
    def test_crear_plan(self):
        plan = Plan.objects.create(
            nombre="Aseguramiento calidad del agua",
            anio = 2025,
            resolucion = "2025/1023"
        )

        assert plan.nombre == "Aseguramiento calidad del agua"
        assert plan.anio == 2025
        assert str(plan) == "Aseguramiento calidad del agua"

    def test_plan_sin_anio(self):
        with pytest.raises(IntegrityError):
            Plan.objects.create(nombre="Aseguramiento calidad del agua", resolucion="2025/1023")

    def test_plan_nombre_max_length(self):
        with pytest.raises(ValidationError):
            plan = Plan(
                nombre="a" * 201,  # Más del límite de 200 caracteres
                anio = 2025,
                resolucion="a"
            )
            plan.full_clean()

    def test_plan_resolucion_max_length(self):
        with pytest.raises(ValidationError):
            plan = Plan(
                nombre="a" ,
                anio = 2025,
                resolucion="a"* 51  # Más del límite de 200 caracteres
            )
            plan.full_clean()
