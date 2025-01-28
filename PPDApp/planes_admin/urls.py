from django.urls import path
from . import views


urlpatterns = [
    path('agregar_plan/', views.agregar_plan),
    path('ver_planes/', views.lista_plan, name='lista_plan'),
    path('detalle_plan/', views.detalle_plan, name='detalle_plan'),
]
