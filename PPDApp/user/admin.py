from django.contrib import admin
from django.contrib.auth.models import Permission

from .models import Usuario

class UsuarioAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Usuario._meta.fields]

admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Permission)
