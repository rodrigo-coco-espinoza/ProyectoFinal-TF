
$env:DJANGO_SETTINGS_MODULE="PPDApp.settings"


$codigo = @"

import django
django.setup()
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from user.models import Usuario
from django.contrib.auth.models import User

import random
import string

def generar_contrasena():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=12))

for usuario in Usuario.objects.all():
    nueva_pass = generar_contrasena()
    usuario.set_password('12345678')
    usuario.save()
    print(f""Contrasena generada para {usuario.email}: {nueva_pass}"")
"@
python -c "$codigo"
