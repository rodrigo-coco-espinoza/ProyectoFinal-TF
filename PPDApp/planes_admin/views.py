from django.shortcuts import render, redirect
from .models import *
from .forms import *
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

def agregar_plan(request):
    
    if request.method == "POST":
        form = agregar_plan_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_plan')
    else:
        form = agregar_plan_form()

    return render(request, 'agregar_plan.html', {'form': form})

def lista_plan(request):
    planes = Plan.objects.all()
    return render(request, 'lista_plan.html', {'planes':planes})
