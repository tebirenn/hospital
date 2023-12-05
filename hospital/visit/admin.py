from django.contrib import admin
from .models import *

# Register your models here.
class VisitAdmin(admin.ModelAdmin):
    list_display = ('id', 'status', 'patient', 'service', 'schedule')
    list_filter = ('status', 'patient', 'service', )
    