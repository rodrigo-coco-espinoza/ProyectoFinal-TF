# user/models.py
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models

class UsuarioManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('El email es obligatorio')
        email = self.normalize_email(email)
        usuario = self.model(email=email, **extra_fields)
        usuario.set_password(password)
        usuario.save(using=self._db)
        return usuario

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)

class Usuario(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    is_planificador = models.BooleanField(default=False)
    is_responsable = models.BooleanField(default=False)
    is_aprobador = models.BooleanField(default=False)

    clave_unica = models.CharField(max_length=100)

    objects = UsuarioManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombre', 'apellido']

    class Meta:
        permissions = [
            ('crear_plan', 'Puede crear planes'),
            ('aprobar_plan', 'Puede aprobar planes'),
            ('actualizar_medidas', 'Puede actualizar estados de medidas'),
            ('administrar', 'Puede administra sistema'),

        ]

    def __str__(self):
        return self.email + " - " + self.nombre + "  " + self.apellido