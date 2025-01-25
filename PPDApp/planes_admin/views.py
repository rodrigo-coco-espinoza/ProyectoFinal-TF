from django.shortcuts import render
from .models import Comuna
from django.http import JsonResponse

# Create your views here.
def Comunas(request):
    comunas = Comuna.objects.all()
    comunas_list = list(comunas.values())
    return JsonResponse(comunas_list, safe=False)