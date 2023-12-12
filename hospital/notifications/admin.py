from django.contrib import admin
from .models import *

# Register your models here.
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('id', 'recipient', 'message', 'type')
    list_filter = ('recipient', 'type', 'status')
    search_fields = ('message', )

admin.site.register(Notification, NotificationAdmin)
