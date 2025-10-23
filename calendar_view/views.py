from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from event_view.models import Event, UserEventLink
from event_view.forms import CreateEventForm
# Create your views here.
# @login_required
# def list_events(request):
#     username =  request.user
#     events = UserEventLink.objects.filter(customUser=username)
    
#     return render(request, 'calendar_view/list.html', {'events': events})

@login_required
def list_events(request):
    username =  request.user
    events = UserEventLink.objects.filter(customUser=username)
    paginator = Paginator(events,3)#show 3 events per page?
    page_number= request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, 'calendar_view/list.html', {'events': events, 'page_obj': page_obj})


@login_required
def edit_event(request, event_id):
    """
    Edit the event which has been selected from the list_event
    view.
    """
    response=""
    event = get_object_or_404(Event, pk=event_id)

    eventLink = UserEventLink.objects.filter(event=event).select_related('customUser')
    linkedUsers =[]
    for userLink in eventLink:
        item = {
            'user': userLink.customUser 
        }        
        linkedUsers.append(item)

    if request.method == 'POST':
        form = CreateEventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            response="Update saved."
            return redirect('calendar:list')
    else:
        response="Something went wrong..."
        form = CreateEventForm(instance=event)
    return render(request, 'calendar_view/edit_event.html', {'form': form, 'event': event, 'response': response,'linkedUsers': linkedUsers,})


#based on the delete event here: https://www.w3schools.com/django/django_delete_record.php
#but utilises the edit_event code above.
def delete_event(request,event_id):
    """
    Event PK is passed on button press. Look for
    the Event, or 404. if found, delete the event and
    immediately redirect to the same list page.
    """
    event = get_object_or_404(Event,pk=event_id)
    event.delete()
    return HttpResponseRedirect(reverse('calendar:list'))