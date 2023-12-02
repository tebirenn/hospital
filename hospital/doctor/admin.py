from django.contrib import admin
from .models import *

class SpecializationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name', )

class DoctorAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'specialization')
    list_filter = ('specialization', )
    search_fields = ('first_name', 'last_name')

admin.site.register(Specialization, SpecializationAdmin)
admin.site.register(Doctor, DoctorAdmin)