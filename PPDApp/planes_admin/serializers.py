from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

class MedidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medida
        fields = '__all__'

class ReporteMedidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReporteMedida
        fields = '__all__'

class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class OrganismoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organismo
        fields = '__all__'

class PlanMedidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanMedida
        fields = '__all__'

class ComunaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comuna
        fields = '__all__'