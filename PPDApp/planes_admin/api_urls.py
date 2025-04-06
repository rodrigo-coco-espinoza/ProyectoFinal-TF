from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
#from .views import PlanViewSet, MedidaViewSet, OrganismoViewSet, ReporteMedidaViewSet
from .views import PlanViewSet, MedidaViewSet, OrganismoViewSet,ComunaViewSet, ReporteMedidaCreateOnlyViewSet
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'plans', PlanViewSet)
router.register(r'medidas', MedidaViewSet)
router.register(r'organismos', OrganismoViewSet)
router.register(r'comunas', ComunaViewSet)
#router.register(r'reporte', ReporteMedidaViewSet)
router.register(r'reporte-medida', ReporteMedidaCreateOnlyViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
