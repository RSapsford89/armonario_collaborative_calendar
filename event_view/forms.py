from django import forms
from django.forms import formset_factory
from event_view.models import Event, UserEventLink


class CreateEventForm(forms.ModelForm):
    """
    Form contents to render in view for
    creating Events
    """
    
    class Meta():
        model = Event
        fields =('EventName','PrivateEvent','GroupEvent',
            'StartDate','EndDate','StartTime','EndTime',
            'Location','Notes', #'GroupId',
        )
        widgets = {
            'StartDate': forms.DateInput(attrs={'type': 'date'}),
            'EndDate': forms.DateInput(attrs={'type': 'date'}),
            'StartTime': forms.TimeInput(attrs={'type': 'time'}),
            'EndTime': forms.TimeInput(attrs={'type': 'time'}),
        }


class AddUsersForm(forms.ModelForm):
    """
    Form for adding users to an Event or Group
    Use formsets in required view 
    """
    class Meta():
        model = UserEventLink
        fields = ['customUser']


class UpdateStatusForm(forms.ModelForm):
    """
    Form for letting a user change their status on 
    UserEventLink events
    """
    class Meta:
        model = UserEventLink
        fields = ['status']
