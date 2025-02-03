from django import forms
from .models import *

class agregar_plan_form(forms.ModelForm):
    class Meta:
        model = Plan
        fields = ['nombre', 'anio', 'resolucion']

class agregar_medida_form(forms.ModelForm):
    id = forms.IntegerField(widget=forms.HiddenInput(), required=False)
    organismo = forms.ModelChoiceField(queryset=OrganismoSectorial.objects.all())
    plan = forms.ModelChoiceField(queryset=Plan.objects.all(),widget=forms.HiddenInput())

    class Meta:
        model = Medida
        fields = ['id','referencia', 'nombre', 'indicador', 'plan', 'formula','frecuencia','medio_verificacion','tipo','organismo']


#    def __init__(self, *args, **kwargs):
#        plan_id  = kwargs.pop('plan_id', None)
#        super(agregar_medida_form, self).__init__(*args, **kwargs)
#        self.fields['plan_id'].initial=plan_id

