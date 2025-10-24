from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CreateEventForm, AddUsersForm
from .models import Event, UserEventLink

# Create your views here.

#The logic to view multiple forms in a view linked in ReadMe
@login_required
def create_event(request):
    if request.method == 'POST':
        eform = CreateEventForm(request.POST, user=request.user)
        uform = AddUsersForm(request.POST, prefix='inviteUsers', user=request.user)

        if eform.is_valid():
            event = eform.save()
            if uform.is_valid():
                invited = uform.cleaned_data.get('customUser')
                if invited:
                    UserEventLink.objects.get_or_create(
                        customUser=invited,
                        event=event,
                        defaults={'status': 2}
                    )
            UserEventLink.objects.get_or_create(customUser=request.user, event=event, defaults={'status': 1})
            return redirect('calendar:list')

    else:
        eform = CreateEventForm(user=request.user)
        uform = AddUsersForm(prefix='inviteUsers', user=request.user)

    return render(request, 'event_view/create.html', {'eform': eform, 'uform': uform})