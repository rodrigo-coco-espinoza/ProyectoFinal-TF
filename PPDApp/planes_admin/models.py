from django.db import models

FRECUENCIA_CHOICES = (
    ('cada 5 años', 'Cada 5 años'),
    ('unica', 'Única'),
    ('anual', 'Anual'),
)
TIPO_CHOICES = (
    ('regulatoria', 'Regulatoria'),
    ('no regulatoria', 'No regulatoria'),
)

class OrganismoSectorial(models.Model):
    nombre = models.CharField(max_length=200)
    sigla = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    rut = models.CharField(max_length=50)
    direccion = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class Plan (models.Model):
    nombre = models.CharField(max_length=200)
    ano = models.IntegerField()
    resolucion = models.CharField(max_length=50)

class Medida(models.Model):
    referencia = models.CharField(max_length=50)
    nombre = models.CharField(max_length=200)
    indicador = models.CharField(max_length=50)
    formula = models.CharField(max_length=200)
    frecuencia = models.CharField(max_length=50, choices=FRECUENCIA_CHOICES)
    medio_verificacion = models.CharField(max_length=200)
    tipo = models.CharField(max_length=50, choices=TIPO_CHOICES)
    organismo = models.ForeignKey(OrganismoSectorial, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
    
class Comuna(models.Model):
    nombre = models.CharField(max_length=200)
    region = models.CharField(max_length=200)
    provincia = models.CharField(max_length=200)
    def __str__(self):
        return self.nombre
    
class PlanMedida(models.Model):
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    medida = models.ForeignKey(Medida, on_delete=models.CASCADE)
    def __str__(self):
        return self.plan.nombre + " - " + self.medida.nombre

class PlanComuna(models.Model):
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)
    def __str__(self):
        return self.plan.nombre + " - " + self.comuna.nombre