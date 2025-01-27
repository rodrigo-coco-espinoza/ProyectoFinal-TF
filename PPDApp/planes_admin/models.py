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
    """
    Representa un Organismo Sectorial

    Atributos:
    - nombre: Nombre del Organismo Sectorial.
    - sigla: Sigla del Organismo Sectorial.
    - descripcion: Descripción del Organismo Sectorial.
    - rut: RUT del Organismo Sectorial
    - direccion: Dirección completa del Organismo Sectorial
    """
    nombre = models.CharField(max_length=200)
    sigla = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    rut = models.CharField(max_length=50)
    direccion = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class Plan (models.Model):
    """
    Representa un Plan de Descontaminación Ambiental

    Atributos:
    - nombre (str): Nombre del Plan
    - anio (int): Año de Aplicación del Plan
    - resolucion (str): Resolución en que se oficicializa el Plan
    """
    class Meta:
        verbose_name_plural = "planes"

    nombre = models.CharField(max_length=200)
    anio = models.IntegerField()
    resolucion = models.CharField(max_length=50, help_text="Resolucion oficial del PPDA")

class Medida(models.Model):
    """
    Representa una medida de un PPDA.

    Atributos:
    - referencia (str): Referencias de la medida.
    - nombre (str): Nombre único de la medida.
    - indicador (str): Nombre del indicador para evaluar la medida.
    - formula (str): Formula de calculo del indicador de la medida.
    - frecuencia (str): Frecuencia de reporte del indicador de la medida.
    - medio_verificacion (str): Medios de verificación del indicador de la medida.
    - tipo (str): Tipo de la medida.
    - organismo (OrganismoSectorial): Organismo sectorial responsable de la medida.
    """
    referencia = models.CharField(max_length=50)
    nombre = models.CharField(max_length=200)
    indicador = models.CharField(max_length=50)
    formula = models.CharField(max_length=200)
    frecuencia = models.CharField(max_length=50, choices=FRECUENCIA_CHOICES)
    medio_verificacion = models.CharField(max_length=200)
    tipo = models.CharField(max_length=50, choices=TIPO_CHOICES)
    organismo = models.ForeignKey(OrganismoSectorial, on_delete=models.CASCADE, help_text='Organismo sectorial responsable de reportar la medida')

    def __str__(self):
        return self.nombre
    
class Comuna(models.Model):
    """
    Representa a una comuna.

    Atributos:
    - nombre (str): Nombre de la comuna.
    - region (str): Nombre de la region a la que pertenece la comuna.
    - provincia (str): Nombre de la provincia a la que pertenece la comuna.
    """
    nombre = models.CharField(max_length=200)
    region = models.CharField(max_length=200)
    provincia = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre
    
class PlanMedida(models.Model):
    """
    Representa la relacion entre planes y medidas.

    Atributos:
    - plan (Plan): Identificador único de un plan.
    - medida (Medida): Identificador único de una medida.
    """
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    medida = models.ForeignKey(Medida, on_delete=models.CASCADE)

    def __str__(self):
        return self.plan.nombre + " - " + self.medida.nombre

class PlanComuna(models.Model):
    """
    Representa la relación de comunas que abarca cada plan.

    Atributos:
    - plan (Plan): Identificador único de un plan.
    - comuna (Comuna): Identificador único de la comuna.
    """
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.plan.nombre + " - " + self.comuna.nombre