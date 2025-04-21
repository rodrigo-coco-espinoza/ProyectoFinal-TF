# user/views.py
from django.shortcuts import render, redirect, get_object_or_404, Http404
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import Usuario
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response



import json

# Create your views here.
from django.contrib.auth.views import LoginView, LogoutView

class CustomLoginView(LoginView):
    template_name = 'user/login.html'

class CustomLogoutView(LogoutView):
    http_method_names = ['post','get']
    template_name = 'user/logged_out.html'

def registrar_usuario(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            form.save()
        else:
            print("Formulario invalido")
            print(form.errors)
        return redirect("/user/registrar/")

    else:
        form = CustomUserCreationForm(request.GET)
        return render(request, 'user/registrar.html', {'form': form})

def actualizar_usuario(request, pk):
    try:
        usuario = get_object_or_404(Usuario, pk=pk)
        if request.method == 'POST':
            form = CustomUserChangeForm(request.POST, instance=usuario)
            if form.is_valid():
                form.save()
                return redirect("/user/actualizar/"+str(pk))
            else:
                print("Formulario invalido")
                print(form.errors)
        else:
            form = CustomUserChangeForm(instance=usuario)
        return render(request, 'user/registrar.html', {'form': form})

    except Http404:
        print('No se encontró el usuario')

class UsuarioPermisosView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        permisos = list(request.user.get_all_permissions())
        return Response({"permisos": permisos})