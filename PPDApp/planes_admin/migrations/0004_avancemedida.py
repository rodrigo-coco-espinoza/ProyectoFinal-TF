# Generated by Django 5.1.5 on 2025-03-28 02:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planes_admin', '0003_medida_plan_alter_medida_organismo_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AvanceMedida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('porcentaje', models.IntegerField(choices=[('regulatoria', 'Regulatoria'), ('no regulatoria', 'No regulatoria')], max_length=50)),
                ('medida', models.OneToOneField(help_text='Medida', on_delete=django.db.models.deletion.CASCADE, to='planes_admin.medida')),
            ],
        ),
    ]
