# user/forms.py
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Usuario

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ('email', 'nombre', 'apellido')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = Usuario
        fields = ('email', 'nombre', 'apellido','is_planificador','is_aprobador','is_responsable')
