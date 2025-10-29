from django.contrib import admin
from django.utils.html import format_html
from .models import CustomUser


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'profile_thumb', 'email', 'first_name', 'last_name', 'email')
    readonly_fields = ('profile_thumb',)
    # Used AI to help display the profile picture in the column

    def profile_thumb(self, obj):
        if obj.picture:
            return format_html(
                '<img src="{}" style="height:50px; border-radius:4px;" />',
                obj.picture.url
            )
        return "-"
    profile_thumb.short_description = 'Profile'


admin.site.register(CustomUser, UserProfileAdmin)
