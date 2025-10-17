from django.contrib import admin
from .models import GroupProfile, UserGroupLink
# Register your models here.
# information on how to link m2m fields from  here: https://www.freecodecamp.org/news/how-to-register-models-in-django-admin/
class GroupProfileAdmin(admin.ModelAdmin):
    list_display = ('GroupName', 'GroupColour', 'DateCreated', 'GroupShareCode')

class UserGroupLinkAdmin(admin.ModelAdmin):
    list_display = ['groupProfile', 'customUser', 'status', ]


admin.site.register(GroupProfile, GroupProfileAdmin)
admin.site.register(UserGroupLink, UserGroupLinkAdmin)

