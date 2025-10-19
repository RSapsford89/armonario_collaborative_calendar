from django import forms
from event_view.models import Event

class CreateEventForm(forms.ModelForm):
    """
    Form contents to render in view for
    creating Events
    """
    class Meta():
        model = Event
        fields =(
            'EventName',
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
        widgets = {
            'StartDate': forms.DateTimeInput(attrs={'type':'date'}),
            'EndDate': forms.DateTimeInput(attrs={'type':'date'}),
            'StartTime': forms.TimeInput(attrs={'type':'time'}),
            'EndTime': forms.TimeInput(attrs={'type':'time'}),
        }