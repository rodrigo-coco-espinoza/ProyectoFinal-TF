from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PlanViewSet, MedidaViewSet, OrganismoViewSet, ReporteMedidaCreateOnlyViewSet
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'plans', PlanViewSet)
router.register(r'medidas', MedidaViewSet)
router.register(r'organismos', OrganismoViewSet)
router.register(r'reporte-medida', ReporteMedidaCreateOnlyViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('agregar_plan/', views.agregar_plan),
    path('ver_planes/', views.lista_plan, name='lista_plan'),
    path('detalle_plan/<int:pk>', views.detalle_plan, name='detalle_plan'),
    path('agregar_medida/', views.agregar_medida, name='agregar_medida'),
    path('modificar_medida/<int:pk>/', views.agregar_medida, name='modificar_medida'),


]
