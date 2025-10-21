from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CreateEventForm, AddUsersForm
from .models import UserEventLink

# Create your views here.

#The logic to view multiple forms in a view linked in ReadMe
@login_required
def create_event(request):
    if request.method == 'POST':
        eform = CreateEventForm(request.POST)
        uform = AddUsersForm(request.POST, prefix='inviteUsers')
        print("eform called")
        if eform.is_valid() and uform.is_valid():
            event = eform.save()
            eventLink = uform.save(commit=False)
            eventLink.event = event
            eventLink.status = 2
            eventLink.save()            
            UserEventLink.objects.get_or_create(
                customUser=request.user,
                event=event,
                defaults={'status': 1}
            )
            response = "Event created."
            eform = CreateEventForm()
        else:
            response = "Unable to create that Event"
    else:
        eform = CreateEventForm()
        uform = AddUsersForm(prefix='inviteUsers')
        response = ""
    return render(request, 'event_view/create.html', {'eform': eform, 'uform': uform, 'response': response})