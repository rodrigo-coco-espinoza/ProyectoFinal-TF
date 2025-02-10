from django.urls import path
from . import views


urlpatterns = [
    path('agregar_plan/', views.agregar_plan),
    path('ver_planes/', views.lista_plan, name='lista_plan'),
    path('detalle_plan/<int:pk>', views.detalle_plan, name='detalle_plan'),
    path('agregar_medida/', views.agregar_medida, name='agregar_medida'),
    path('modificar_medida/<int:pk>/', views.agregar_medida, name='modificar_medida'),

]
