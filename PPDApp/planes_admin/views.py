from django.shortcuts import render, redirect, get_object_or_404
from django.utils.text import normalize_newlines

from .models import *
from .forms import *
from django.http import JsonResponse
from rest_framework.decorators import api_view
from drf_spectacular.utils import extend_schema, extend_schema_view

# Create your views here.

@extend_schema(
    summary="Página de inicio",
    description="Página inicial que no devuelve datos en formato JSON, solo un renderizado.",
    exclude=True  # Excluir esta vista de la documentación porque no es una API.
)
def home(request):
    """
    Página inicial de la API.

    Args:
        request (Request): Solicitud HTTP.
    """
    return render(request, 'home.html')

@extend_schema(
    summary="Agregar un nuevo plan",
    description="Endpoint para agregar un nuevo plan mediante una solicitud POST.",
    request=agregar_plan_form,  # Esquema del formulario para la solicitud.
    responses={200: {"type": "string", "example": "Plan agregado correctamente"}}
)
@extend_schema(
    summary="Listar planes",
    description="Devuelve una lista de todos los planes en formato JSON.",
    responses={
        200: {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {"type": "integer"},
                    "nombre": {"type": "string"}
                }
            }
        }
    }
)
@api_view(['GET'])
def lista_plan(request):
    """
    Devuelve una lista de todos los planes.

    Args:
        request (Request): Solicitud HTTP.
    """
    planes = Plan.objects.all()
    return render(request, 'lista_plan.html', {'planes':planes})

@api_view(['GET'])
def detalle_plan(request, pk=None):
    """
    Devuelve una lista de todos los planes.

    Args:
        request (Request): Solicitud HTTP.
    """
    if pk:
        try:
            plan = get_object_or_404(Plan, pk=pk)
            print(f'Plan obtenido: {plan}')
        except Http404:
            print('No se encontró el plan')

    else:
        plan = None

    print(plan.__dict__)
    if plan:
        medidas = list(Medida.objects.filter(plan=plan.id))
        return render(request, 'plan.html', {'plan':plan.__dict__, 'medidas': list(medidas)})

    return redirect('/planes_admin/ver_planes/')

@api_view(['GET', 'POST'])
def agregar_plan(request):
    """
    Despliega un formulario para agregar un nuevo plan.

    Args:
        request (Request): Solicitud HTTP.
        """
    if request.method == "POST":
        form = agregar_plan_form(request.POST)
        if form.is_valid():
            instancia=form.save()
            print(instancia.id)
            return redirect("/planes_admin/detalle_plan/"+str(instancia.id))
    else:
        form = agregar_plan_form()

    return render(request, 'agregar_plan.html', {'form': form})


@api_view(['GET', 'POST'])
def agregar_medida(request, pk=None):
    """
    Despliega un formulario para agregar una nueva medida a un plan.

    Args:
        request (Request): Solicitud HTTP.
        """
    if pk:
        try:
            medida = get_object_or_404(Medida, pk=pk)
            print(f'medida obtenida: {medida}')
        except Http404:
            print('No se encontró la medida')

    else:
        medida = None

    if request.method == "POST":
        form = agregar_medida_form(request.POST, instance=medida)
        if form.is_valid():
            medida=form.save()
        else:
            print(form.errors)
        return redirect("/planes_admin/detalle_plan/"+str(medida.plan_id))
    else:
        plan_id=request.GET.get('plan_id')
        if plan_id:
            form = agregar_medida_form(initial={"plan":plan_id})
        else:
            form = agregar_medida_form(instance=medida)

        return render(request, 'agregar_medida.html', {'form': form})