from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *


router = DefaultRouter()
router.register(r'plans', PlanViewSet)
router.register(r'medidas', MedidaViewSet)
router.register(r'organismos', OrganismoViewSet)
router.register(r'comunas', ComunaViewSet)
router.register(r'plan-medida', PlanMedidaViewSet)
router.register(r'reporte-medida', ReporteMedidaCreateOnlyViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
