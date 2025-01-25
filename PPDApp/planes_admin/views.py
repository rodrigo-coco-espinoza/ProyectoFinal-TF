from django.shortcuts import render
from .models import *
from django.http import JsonResponse

# Create your views here.
def Comunas(request):
    comunas = Comuna.objects.all()
    comunas_list = list(comunas.values())
    return JsonResponse(comunas_list, safe=False)

def Planes(request):
    planes = Plan.objects.all()
    planes_list = list(planes.values())
    return JsonResponse(planes_list, safe=False)

