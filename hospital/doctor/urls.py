from django.urls import path
from . import views

app_name = 'doctor'

urlpatterns = [
    # path('spec/create/', views.CreateSpecAPIView.as_view(), name='spec_create'),
    # path('spec/list/', views.ListSpecAPIView.as_view(), name='spec_list'),
    path('spec/', views.ListCreateSpecAPIView.as_view(), name='spec_list_create'),
    path('spec/one/<int:pk>/', views.RetrieveSpecAPIView.as_view(), name='spec_one'),
    path('spec/delete/<int:pk>/', views.DestroySpecAPIView.as_view(), name='spec_delete'),
    path('spec/update/<int:pk>/', views.UpdateSpecAPIView.as_view(), name='spec_update'),

    path('', views.DoctorAPIView.as_view(), name='doctor'),
    path('detail/<int:pk>/', views.DoctorDetailAPIView.as_view(), name='doctor-detail'),
]