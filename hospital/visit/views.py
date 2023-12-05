from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from patient.permissions import IsAdminOrReadOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import *
from .serializers import *

# Create your views here.
class ServiceAPIView(ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = (IsAdminOrReadOnly, )

class ServiceDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = (IsAdminOrReadOnly, )

class ScheduleAPIView(ListCreateAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    permission_classes = (IsAdminOrReadOnly, )

class ScheduleDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleAPIView
    permission_classes = (IsAdminOrReadOnly, )

class VisitAPIView(ListCreateAPIView):
    queryset = Visit.objects.all()
    serializer_class = VisitSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

class VisitDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Visit.objects.all()
    serializer_class = VisitSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )