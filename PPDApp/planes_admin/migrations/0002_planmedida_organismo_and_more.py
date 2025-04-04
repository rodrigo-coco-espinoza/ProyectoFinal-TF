# Generated by Django 5.1.5 on 2025-04-04 17:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planes_admin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='planmedida',
            name='organismo',
            field=models.ForeignKey(default=1, help_text='Organismo sectorial responsable de reportar la medida', on_delete=django.db.models.deletion.CASCADE, to='planes_admin.organismo'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='reportemedida',
            name='medio_verificacion',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
