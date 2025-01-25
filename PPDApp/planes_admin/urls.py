from django.urls import path
from . import views


urlpatterns = [
    path('agregarplanes/', views.agregar_plan),
    path('planes/', views.lista_plan),
]
