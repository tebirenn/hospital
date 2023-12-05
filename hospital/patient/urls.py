from django.urls import path
from . import views

urlpatterns = [
    path('', views.PatientAPIView.as_view(), name='patient'),
    # path('<int:patient_pk>/', views.PatientDetailAPIView.as_view(), name='patient_detail'),
    path('destroy/<int:patient_pk>/', views.PatientDestroyAPIView.as_view(), name='patient_destroy'), 
    path('gender/<str:gender>/', views.PatientGetByGenderAPIView.as_view(), name='patient_gender'),   
]