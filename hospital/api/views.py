from django.shortcuts import render
from rest_framework.generics import \
    CreateAPIView, \
    ListAPIView, \
    RetrieveAPIView, \
    DestroyAPIView, \
    UpdateAPIView, \
    ListCreateAPIView
from rest_framework.views import APIView

from .models import *
from .serializers import *

# class CreateSpecAPIView(CreateAPIView):
#     queryset = Specialization.objects.all()
#     serializer_class = SpecializationSerializer

# class ListSpecAPIView(ListAPIView):
#     queryset = Specialization.objects.all()
#     serializer_class = SpecializationSerializer

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