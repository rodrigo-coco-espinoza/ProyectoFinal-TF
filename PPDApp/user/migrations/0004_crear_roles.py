from django.db import migrations


def crear_roles(apps, schema_editor):
    Group = apps.get_model("auth", "Group")
    Permission = apps.get_model("auth", "Permission")

    roles = {
        "Administrador": ["add_comuna", "change_comuna", "delete_comuna", "view_comuna",
                          "add_organismo", "change_organismo", "delete_organismo", "view_organismo",
                          "add_comuna", "change_comuna", "delete_comuna", "view_comuna"
        ],
        "Planificador": ["add_plan", "change_plan", "delete_plan", "view_plan",
                         "add_medida", "change_medida", "delete_medida", "view_medida",
                         ],
        "Agente": ["view_plan","view_medida","change_avance", "view_avance"],
        "Lector": ["view_plan","view_medida", "view_avance"],
    }

    for role, permisos in roles.items():
        group, created = Group.objects.get_or_create(name=role)
        for permiso in permisos:
            permission = Permission.objects.get(codename=permiso)
            group.permissions.add(permission)


def eliminar_roles(apps, schema_editor):
    Group = apps.get_model("auth", "Group")
    Group.objects.filter(name__in=["Administrador", "Planificador", "Agente", "Lector"]).delete()


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0002_remove_usuario_is_aprobador_and_more"),
    ]

    operations = [
        migrations.RunPython(crear_roles, eliminar_roles),
    ]