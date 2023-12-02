from rest_framework import serializers
from .models import *

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        models = Service
        fields = '__all__'

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        models = Schedule
        fields = '__all__'

class VisitSerializer(serializers.ModelSerializer):
    class Meta:
        models = Visit
        fields = '__all__'