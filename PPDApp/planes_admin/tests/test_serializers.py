from datetime import date

import pytest
from rest_framework.exceptions import ValidationError

from myapp.models import Autor, Libro
from myapp.serializers import AutorSerializer, LibroSerializer


@pytest.mark.django_db
class TestAutorSerializer:
    @pytest.fixture
    def autor_data(self):
        return {
            "nombre": "Gabriel",
            "apellido": "García Márquez",
            "fecha_nacimiento": "1927-03-06",
            "biografia": "Escritor colombiano, premio Nobel de Literatura",
        }

    def test_serializar_autor(self, autor_data):
        serializer = AutorSerializer(data=autor_data)
        assert serializer.is_valid()
        autor = serializer.save()
        assert autor.nombre == autor_data["nombre"]
        assert autor.apellido == autor_data["apellido"]
        assert str(autor.fecha_nacimiento) == autor_data["fecha_nacimiento"]
        assert autor.biografia == autor_data["biografia"]

    def test_serializar_autor_sin_fecha_nacimiento(self):
        data = {"nombre": "Gabriel", "apellido": "García Márquez"}
        serializer = AutorSerializer(data=data)
        assert serializer.is_valid()
        autor = serializer.save()
        assert autor.fecha_nacimiento is None
        assert autor.biografia == ""

    def test_validacion_nombre_max_length(self, autor_data):
        autor_data["nombre"] = "a" * 101  # Más del límite de 100 caracteres
        serializer = AutorSerializer(data=autor_data)
        assert not serializer.is_valid()
        assert "nombre" in serializer.errors

    def test_validacion_apellido_max_length(self, autor_data):
        autor_data["apellido"] = "a" * 101  # Más del límite de 100 caracteres
        serializer = AutorSerializer(data=autor_data)
        assert not serializer.is_valid()
        assert "apellido" in serializer.errors

    def test_deserializar_autor(self):
        autor = Autor.objects.create(
            nombre="Gabriel",
            apellido="García Márquez",
            fecha_nacimiento=date(1927, 3, 6),
        )
        serializer = AutorSerializer(autor)
        data = serializer.data
        assert data["nombre"] == autor.nombre
        assert data["apellido"] == autor.apellido
        assert data["fecha_nacimiento"] == "1927-03-06"


@pytest.mark.django_db
class TestLibroSerializer:
    @pytest.fixture
    def autor(self):
        return Autor.objects.create(nombre="Gabriel", apellido="García Márquez")

    @pytest.fixture
    def libro_data(self, autor):
        return {
            "titulo": "Cien años de soledad",
            "fecha_publicacion": "1967-05-30",
            "isbn": "9780307474728",
            "descripcion": "Una obra maestra de la literatura latinoamericana",
            "paginas": 417,
            "autores": [autor.id],
        }

    def test_serializar_libro_sin_descripcion(self, autor):
        data = {
            "titulo": "Cien años de soledad",
            "fecha_publicacion": "1967-05-30",
            "isbn": "9780307474728",
            "paginas": 417,
            "autores": [autor.id],
        }
        serializer = LibroSerializer(data=data)
        assert serializer.is_valid()
        libro = serializer.save()
        assert libro.descripcion == ""

    def test_validacion_titulo_max_length(self, libro_data):
        libro_data["titulo"] = "a" * 201  # Más del límite de 200 caracteres
        serializer = LibroSerializer(data=libro_data)
        assert not serializer.is_valid()
        assert "titulo" in serializer.errors

    def test_validacion_isbn_unico(self, libro_data):
        # Crear un libro con el mismo ISBN
        Libro.objects.create(
            titulo="El amor en los tiempos del cólera",
            fecha_publicacion=date(1985, 1, 1),
            isbn=libro_data["isbn"],
            paginas=368,
        )
        serializer = LibroSerializer(data=libro_data)
        assert not serializer.is_valid()
        assert "isbn" in serializer.errors

    def test_validacion_paginas_positivas(self, libro_data):
        libro_data["paginas"] = -1
        serializer = LibroSerializer(data=libro_data)
        assert not serializer.is_valid()
        assert "paginas" in serializer.errors

    def test_deserializar_libro(self, autor):
        libro = Libro.objects.create(
            titulo="Cien años de soledad",
            fecha_publicacion=date(1967, 5, 30),
            isbn="9780307474728",
            paginas=417,
        )
        libro.autores.add(autor)
        serializer = LibroSerializer(libro)
        data = serializer.data
        assert data["titulo"] == libro.titulo
        assert data["fecha_publicacion"] == "1967-05-30"
        assert data["isbn"] == libro.isbn
        assert len(data["autores"]) == 1
        assert data["autores"][0]["nombre"] == autor.nombre
