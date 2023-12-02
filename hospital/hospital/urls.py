from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from rest_framework_swagger.views import get_swagger_view
from . import settings

schema_view = get_swagger_view(title='Hospital API')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', schema_view),

    path('api/doctor/', include('doctor.urls')),
    path('api/users/', include('authe.urls')),
    path('api/patient/', include('patient.urls')),
    path('api/visit/', include('visit.urls')),
    path('api/notifications', include('notifications.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
