
# Plataforma de Fiscalización y Seguimiento de PPDA
## Descripción General del Sistema 
### Visión del Producto
**¿Qué estamos creando?**  
Una plataforma electrónica para el registro y reporte de fiscalización y seguimiento de los Planes de Prevención y Descontaminación Ambiental (PPDA), basándonos en el PPDA de Concón, Quintero y Puchuncaví. Esta plataforma integrará sistemas de información de organismos sectoriales como la SMA, promoviendo transparencia y cumplimiento normativo.

## Relación con el Seguimiento de Medidas PPDA

La plataforma facilitará la recopilación y monitoreo de los avances en las medidas de los PPDA, promoviendo la integración de sistemas sectoriales, el reporte de avances y la verificación del cumplimiento de las medidas ambientales.

## Objetivos del Producto
- Facilitar la integración de sistemas de información de organismos sectoriales.
- Registrar y reportar el avance de medidas de los PPDA en Concón, Quintero y Puchuncaví.
- Fortalecer la transparencia, permitiendo acceso a la información a ciudadanos y organismos sectoriales.
- Implementar indicadores de avance y medios verificadores en el monitoreo en línea.

## Instrucciones de Instalación y Ejecución

### Requisitos Previos
- Django 5.1.5
- VS Code o PyCharm (se recomienda el uso de PyCharm )
- Python version 3.12.7
- virtualenv version 20.27.1
- pip version 25.0
- git bash 2.44.0
- Dependencias: requerimientos se encuentran en requirements.txt. Este proyecto requiere las siguientes librerías de Python:
  ```bash
   asgiref==3.8.1
   attrs==25.3.0
   Django==5.1.5
   djangorestframework==3.15.2
   djangorestframework_simplejwt==5.5.0
   drf-spectacular==0.28.0
   inflection==0.5.1
   jsonschema==4.23.0
   jsonschema-specifications==2024.10.1
   psycopg2==2.9.10
   PyJWT==2.9.0
   python-decouple==3.8
   PyYAML==6.0.2
   referencing==0.36.2
   rpds-py==0.24.0
   sqlparse==0.5.3
   typing_extensions==4.13.1
   uritemplate==4.1.1
  ```

### Instalación
1. Clonar el repositorio:
   ```bash
    git clone https://github.com/rodrigo-coco-espinoza/ProyectoFinal-TF.git
   cd ProyectoFinal-TF
   
2. Crear y activar entorno virtual
   ```bash
   python -m venv venv
   venv\Scripts\activate         # En Windows
   
3. Instalar dependencias
   ```bash
   pip install -r requirements.txt

4. Navegar a carpeta PPDApp
   ```bash
   cd  PPDApp
   
5. Migrar la base de datos
   ```bash
   python manage.py makemigrations
   python manage.py migrate auth  
   python manage.py migrate contenttypes
   python manage.py migrate
     
6. Ejecutar el servidor
   ```bash
   python manage.py runserver

## Modelos y entidades clave del sistema

Los modelos del sistema están definidos en el archivo models.py y representan las entidades fundamentales para el registro, seguimiento y reporte de las medidas establecidas en los Planes de Prevención y Descontaminación Atmosférica (PPDA). Estas entidades permiten organizar la información por planes, medidas, organismos sectoriales responsables, comunas afectadas y reportes asociados.

### Modelos principales:

- Organismo: Representa a los organismos sectoriales responsables de ejecutar y reportar medidas. Contiene campos como nombre, sigla, descripción, RUT y dirección.
- Plan: Define los PPDA con nombre, año y resolución. Incluye un método para calcular el porcentaje de avance del plan según los reportes vinculados.
- Medida: Describe cada medida ambiental, su indicador, fórmula, tipo (regulatoria o no regulatoria), frecuencia de reporte y medios de verificación.
- Comuna: Identifica las comunas involucradas en cada PPDA, incluyendo nombre, región y provincia.
- PlanMedida: Relaciona medidas específicas con planes y organismos sectoriales, y permite registrar el año de ejecución.
- PlanComuna: Asocia cada plan con las comunas que abarca y el organismo responsable en cada caso.
- ReporteMedida: Contiene los reportes entregados por los organismos para cada medida, incluyendo fecha, archivo de respaldo y observaciones.

 Para ver la estructura de estos modelos en detalle, puedes revisar el archivo models.py.
 
## Historias de Usuario

Las historias de usuario han sido definidas para representar las necesidades y funcionalidades clave del sistema desde la perspectiva de los distintos usuarios. Estas se encuentran 
registradas y gestionadas en [Taiga](https://taiga.io/).


Puedes revisar todas las historias de usuario en nuestro tablero de Taiga:  
[https://tree.taiga.io/project/jsanmart-registro-actividades-ppda/backlog)

---

## Documentación del Proyecto (Wiki)

Contamos con una Wiki colaborativa que contiene lo siguiente :

- Product Vision Board
- Modelo de proyecto (models.py)
- 
- 

Puedes acceder a la Wiki aquí:  
[Wiki del Proyecto](https://tree.taiga.io/project/jsanmart-registro-actividades-ppda/wiki/home)

---
## Documentación de la API (Swagger)

Contamos con una documentación interactiva de nuestra API implementada con Swagger, la cual permite visualizar los endpoints disponibles, sus métodos, parámetros y respuestas esperadas.

**Acceso a la documentación Swagger:**  
[http://127.0.0.1:8000/docs/](http://127.0.0.1:8000/docs/)  

### ¿Qué puedes hacer desde Swagger?
- Gestionar planes de descontaminación ambiental.
- Visualización de estados de avance.

## Demo Funcional

Para ver una demostración funcional del proyecto, puedes consultar el siguiente enlace al video de YouTube:

 https://youtu.be/4n6RrgtvVvA (Primera entrega)

## Alcances funcionales de la primera y segunda entrega

La segunda entrega contempla funcionalidades clave para el seguimiento de los Planes de Prevención y Descontaminación Atmosférica (PPDA), incluyendo:

- Gestión de organismos sectoriales, planes, medidas, y comunas.
- Asociación de medidas y comunas a cada plan, incluyendo responsable y periodo de ejecución.
- Registro de reportes de avance por medida, con fecha, archivo y observaciones.
- Cálculo automático del porcentaje de avance por plan según medidas reportadas.
- Estructura del proyecto en Django.
- Incorporación de autenticación JWT y roles de usuarios.
- Documentación parcial de la API a través de Swagger.

## Proyecciones a futuro
Las siguientes etapas del proyecto consideran:
- Incorporación de control de acceso y roles (usuarios SMA, organismos, público).
- Generación de reportes descargables y visualizaciones gráficas.
- Validación de reportes con estado y comentarios.
- Mejora de la interfaz de usuario y documentación completa en Swagger.


