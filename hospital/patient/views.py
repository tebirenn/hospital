from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework import status

from .models import *
from .serializers import *
from .permissions import *

# Create your views here.
class PatientAPIView(ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes  = (IsAdminOrReadOnly, )

# class PatientDetailAPIView(RetrieveUpdateAPIView):
#     queryset = Patient
#     serializer_class = PatientSerializer

class PatientDestroyAPIView(APIView):
    def delete(self, request, patient_pk):
        try:
            patient = Patient.objects.get(id=patient_pk)
        except:
            return Response({'detail': 'Object not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            patient.delete()
            return Response({'data': 'Object deleted'}, status=status.HTTP_200_OK)
        
class PatientGetByGenderAPIView(APIView):
    def get(self, request, gender):
        try:
            patients = Patient.objects.filter(gender=gender.upper())
        except:
            return Response({'detail': 'Object not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            serializer = PatientSerializer(patients, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)