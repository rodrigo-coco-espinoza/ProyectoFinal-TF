from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractUser

FRECUENCIA_CHOICES = [
    ('cada 5 años', 'Cada 5 años'),
    ('unica', 'Única'),
    ('anual', 'Anual'),
]
TIPO_CHOICES = [
    ('regulatoria', 'Regulatoria'),
    ('no regulatoria', 'No regulatoria'),
]

class Organismo(models.Model):
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

    def calcular_porcentaje_avance(self):
        """
        Calcula el porcentaje de avance del plan basado en los reportes de las medidas asociadas.
        """
        total_medidas = self.planmedida_set.count()
        if total_medidas == 0:
            return 0
        medidas_validas = sum(1 for medida in self.planmedida_set.all() if hasattr(medida, 'reportemedida') and medida.reportemedida.medio_verificacion)
        return (medidas_validas / total_medidas) * 100

    def __str__(self):
        return self.nombre

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
    """
    referencia = models.CharField(max_length=50)
    nombre = models.CharField(max_length=200)
    indicador = models.CharField(max_length=50)
    formula = models.CharField(max_length=200)
    frecuencia = models.CharField(max_length=50, choices=FRECUENCIA_CHOICES)
    medio_verificacion = models.CharField(max_length=200)
    tipo = models.CharField(max_length=50, choices=TIPO_CHOICES)
    #plan = models.ManyToManyField(Plan, on_delete=models.CASCADE, help_text='Plan')

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
    periodo = models.IntegerField(validators=[MinValueValidator(2020)], help_text="Año de ejecución de la medida", null=True, blank=True)
    organismo = models.ForeignKey(Organismo, on_delete=models.CASCADE,
                                  help_text='Organismo sectorial responsable de reportar la medida')

    def __str__(self):
        return self.plan.nombre + " - " + self.medida.nombre

class PlanComuna(models.Model):
    """
    Representa la relación de comunas que abarca cada plan.

    Atributos:
    - plan (Plan): Identificador único de un plan.
    - comuna (Comuna): Identificador único de la comuna.
    - organismo (Organismo): Organismo sectorial responsable de reportar la medida.
    """
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)
    organismo = models.ForeignKey(Organismo, on_delete=models.CASCADE, help_text='Organismo sectorial responsable de reportar la medida')
    
    def __str__(self):
        return self.plan.nombre + " - " + self.comuna.nombre

class ReporteMedida(models.Model):
    """ 
    Almacena los reportes de avance que un organismo sectorial entrega para una medida de un plan. Se considera más de un reporte por medida.
    
    Atributos:
    - medida (PlanMedida): Identificador único de la medida.
    - fecha (DateField): Fecha de entrega del reporte.
    - medio_verificacion (FileField): Archivo del reporte.
    - estado (str): Estado del reporte (validado o no validado).
    - observaciones (str): Observaciones del reporte.
    """

    medida = models.OneToOneField(PlanMedida, on_delete=models.CASCADE, help_text='Medida')
    fecha = models.DateField()
    medio_verificacion = models.CharField(max_length=200, blank=True, null=True) #models.FileField(upload_to='reportes/')
    #estado = models.CharField(max_length=50, choices=["validado", "no validado"], default="no validado")
    observaciones = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.medida.medida.nombre + "-" + str(self.fecha)