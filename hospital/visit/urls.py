from django.urls import path
from . import views

app_name = 'visit'

urlpatterns = [
    path('service/', views.ServiceAPIView.as_view(), name='service'),   # api/visit/service/
    path('service/<int:pk>/', views.ServiceDetailAPIView.as_view(), name='service-detail'),
    path('schedule/', views.ScheduleAPIView.as_view(), name='service'), # api/visit/schedule/
    path('schedule/<int:pk>/', views.ScheduleDetailAPIView.as_view(), name='schedule-detail'),
    path('', views.VisitAPIView.as_view(), name='visit'),               # api/visit/
    path('<int:pk>/', views.VisitDetailAPIView.as_view(), name='visit-detail'),     # api/visit/1/
]