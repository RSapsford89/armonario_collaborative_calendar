from django.contrib import admin
from .models import Event, UserEventLink
# Register your models here.

class EventProfileAdmin(admin.ModelAdmin):
    list_display=('EventName',
            'PrivateEvent',
            'GroupEvent',
            #'GroupId',
            'StartDate',
            'EndDate',
            'StartTime',
            'EndTime',
            'Location',
            'Notes',
            )
    
class UserEventProfileAdmin(admin.ModelAdmin):
    list_display = ('customUser', 'event', 'status')


admin.site.register(Event, EventProfileAdmin)
admin.site.register(UserEventLink, UserEventProfileAdmin)
