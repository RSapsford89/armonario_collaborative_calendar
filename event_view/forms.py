from django import forms
#from django.forms import formset_factory
from event_view.models import Event, UserEventLink
from group_profile.models import UserGroupLink, GroupProfile
from user_profile.models import CustomUser


class CreateEventForm(forms.ModelForm):
    """
    Form contents to render in view for
    creating Events
    """
    
    class Meta():
        model = Event
        fields =('EventName','PrivateEvent','GroupEvent','group',
            'StartDate','EndDate','StartTime','EndTime',
            'Location','Notes', 
        )
        widgets = {
            'StartDate': forms.DateInput(attrs={'type': 'date'}),
            'EndDate': forms.DateInput(attrs={'type': 'date'}),
            'StartTime': forms.TimeInput(attrs={'type': 'time'}),
            'EndTime': forms.TimeInput(attrs={'type': 'time'}),
        }

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        if 'group' in self.fields:
            if user is not None:
                # show only groups current user belongs to
                self.fields['group'].queryset = GroupProfile.objects.filter(members=user)
            else:
                self.fields['group'].queryset = GroupProfile.objects.none()
            self.fields['group'].required = False


class AddUsersForm(forms.ModelForm):
    """
    Form for adding users to an Event or Group
    Use formsets in required view 
    """
    class Meta():
        model = UserEventLink
        fields = ['customUser']

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        if user is not None:
            self.fields['customUser'].queryset = CustomUser.objects.exclude(pk= user.pk)
        else:
            self.fields['customUser'].queryset = CustomUser.objects.all()
        self.fields['customUser'].required = False

class AddGroupForm(forms.ModelForm):
    """
    Form for adding the user's groups they are a part of.

    """
    class Meta():
        model = UserGroupLink
        fields = ['groupProfile']

class UpdateStatusForm(forms.ModelForm):
    """
    Form for letting a user change their status on 
    UserEventLink events
    """
    class Meta:
        model = UserEventLink
        fields = ['status']
