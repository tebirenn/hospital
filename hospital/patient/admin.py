from django.contrib import admin
from .models import *

# Register your models here.
class PatientAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'contact_info', 'date_of_birth', 'gender')
    list_filter = ('gender', )
    search_fields = ('first_name', 'last_name', 'contanct_info', 'date_of_birth')

admin.site.register(Patient, PatientAdmin)