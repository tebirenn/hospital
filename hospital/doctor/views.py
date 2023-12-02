from django.shortcuts import render
from rest_framework.generics import (
    CreateAPIView, 
    ListAPIView, 
    RetrieveAPIView, 
    DestroyAPIView, 
    UpdateAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)
from rest_framework.views import APIView

from .models import *
from .serializers import *


class ListCreateSpecAPIView(ListCreateAPIView):
    queryset = Specialization.objects.all()
    serializer_class = SpecializationSerializer

class RetrieveSpecAPIView(RetrieveAPIView):
    queryset = Specialization.objects.all()
    serializer_class = SpecializationSerializer

class DestroySpecAPIView(DestroyAPIView):
    queryset = Specialization.objects.all()
    serializer_class = SpecializationSerializer

class UpdateSpecAPIView(UpdateAPIView):
    queryset = Specialization.objects.all()
    serializer_class = SpecializationSerializer

class DoctorAPIView(ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class DoctorDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer




# class CreateSpecAPIView(CreateAPIView):
#     queryset = Specialization.objects.all()
#     serializer_class = SpecializationSerializer

# class ListSpecAPIView(ListAPIView):
#     queryset = Specialization.objects.all()
#     serializer_class = SpecializationSerializer