from datetime import datetime
from unittest.mock import patch
from user.models import Usuario
from django.contrib.auth.models import User, Group

from django.test import TestCase, Client
from rest_framework.test import APITestCase, APIClient

import json

USERNAME = "plan@ppda.cl"
PASSWORD = "12345678"

class PlanTestCase(APITestCase):
    token=""

    def get_token(self, username):
        response = self.client.post("/api/token/", {"email": username, "password": PASSWORD})

        data = response.json()
        self.token = data["access"]

    def setUp(self):
        fixtures = ['comunas.json']
        fixtures = ['organismos.json']

        usuario = Usuario.objects.create_user(email="plan@ppda.cl", password=PASSWORD)
        grupo_planificador, creado = Group.objects.get_or_create(name="Planificador")
        usuario.groups.add(grupo_planificador)

        usuario = Usuario.objects.create_user(email="admin@ppda.cl", password=PASSWORD)
        grupo_administrador, creado = Group.objects.get_or_create(name="Administrador")
        usuario.groups.add(grupo_administrador)

        grupo_agente, creado = Group.objects.get_or_create(name="Agente")
        usuario = Usuario.objects.create_user(email="dgac@ppda.cl", password=PASSWORD, organismo_id=1)
        usuario.groups.add(grupo_agente)
        usuario = Usuario.objects.create_user(email="seremi@ppda.cl", password=PASSWORD, organismo_id=2)
        usuario.groups.add(grupo_agente)

        usuarios = Usuario.objects.all()
        print("Usuarios existentes en la base de datos de pruebas:", list(usuarios))

        self.client == Client()

    def test_plan(self):
        self.get_token("plan@ppda.cl")
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.token}")
        payload = {
            "nombre": "Plan Fiscalizacion",
            "anio": 2025,
            "resolucion": "Resolucion 1/2024"
        }

        response = self.client.post('/api/plans/', payload, format="json")
        #data = response.json()
        print(response.data)
        self.assertEqual(response.status_code, 201)
        self.assertIn("anio",response.data)
        self.assertIn("nombre",response.data)
        self.assertIn("resolucion",response.data)
        plan_id = response.data["id"]
        print(f"{plan_id}")
        payload = {
            "nombre": "Plan Fiscalizacion",
            "anio": 2025,
            "resolucion": "Resolucion 1/2024"
        }

    def test_medida(self):
        self.get_token("admin@ppda.cl")
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.token}")
        payload = {
            "referencia": "REF-1",
            "nombre": "Fiscalizaciones",
            "indicador": "Numero de fiscalizaciones",
            "formula": "Count",
            "frecuencia": "anual",
            "medio_verificacion": "Actas",
            "tipo": "regulatoria"
        }

        response = self.client.post('/api/medidas/', payload, format="json")
        data = response.json()
        print(data)
        self.assertEqual(response.status_code, 201)
        self.assertIn("referencia",response.data)
        self.assertIn("nombre", response.data)
        self.assertIn("indicador", response.data)
        self.assertIn("formula", response.data)
        self.assertIn("frecuencia", response.data)
        self.assertIn("medio_verificacion", response.data)
        self.assertIn("tipo", response.data)
