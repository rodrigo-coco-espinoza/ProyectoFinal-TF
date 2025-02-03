from django.shortcuts import render, redirect
from django.core.paginator import Paginator
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
            form.save()
            return redirect('lista_plan')
    else:
        form = agregar_plan_form()

    return render(request, 'agregar_plan.html', {'form': form})

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

    # Paginación: dividir los planes en páginas de 10 elementos
    paginator = Paginator(planes, 10)

    # Obtener el número de página desde la solicitud GET
    page = request.GET.get('page', 1)  # Si no se pasa ningún número de página, se usa la página 1 por defecto
    page_obj = paginator.get_page(page)

    return render(request, 'lista_plan.html', {'page_obj': page_obj})
@api_view(['GET'])
def detalle_plan(request):
    """
    Devuelve una lista de todos los planes.

    Args:
        request (Request): Solicitud HTTP.
    """
    plan_id=request.GET.get('plan_id')
    plan = Plan.objects.filter(id=plan_id)
    if plan:
        return render(request, 'plan.html', {'plan':list(plan)[0]})

    return redirect('/planes_admin/ver_planes/')