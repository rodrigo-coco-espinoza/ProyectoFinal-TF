# user/urls.py
from django.urls import path
from .views import registrar_usuario, actualizar_usuario, CustomLoginView, CustomLogoutView

urlpatterns = [
    path('registrar/', registrar_usuario, name='registrar_usuario'),
    path('actualizar/<int:pk>/', actualizar_usuario, name='actualizar_usuario'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
]
