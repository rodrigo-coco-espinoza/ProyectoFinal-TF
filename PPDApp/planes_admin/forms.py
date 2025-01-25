from django import forms
from .models import *

class agregar_plan_form(forms.ModelForm):
    class Meta:
        model = Plan
        fields = ['nombre', 'ano', 'resolucion']
        
