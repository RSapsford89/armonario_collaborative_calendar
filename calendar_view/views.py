from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from event_view.models import Event, UserEventLink
from event_view.forms import CreateEventForm
# Create your views here.
@login_required
def list_events(request):
    username =  request.user
    events = UserEventLink.objects.filter(customUser=username)

    return render(request, 'calendar_view/list.html', {'events': events})

@login_required
def edit_event(request, event_id):
    """
    Edit the event which has been selected from the list_event
    view.
    """
    response=""
    event = get_object_or_404(Event, pk=event_id)
    if request.method == 'POST':
        form = CreateEventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            response="Update saved."
            return redirect('calendar:list')
    else:
        response="Something went wrong..."
        form = CreateEventForm(instance=event)
    return render(request, 'calendar_view/edit_event.html', {'form': form, 'event': event, 'response': response})