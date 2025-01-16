from django.contrib import admin
from .models import OrganismoSectorial, Plan, Medida, Comuna, PlanMedida, PlanComuna

class ComunaAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Comuna._meta.fields]

admin.site.register(Comuna, ComunaAdmin)

admin.site.register(OrganismoSectorial)
admin.site.register(Plan)
admin.site.register(Medida)
admin.site.register(PlanMedida)
admin.site.register(PlanComuna)
