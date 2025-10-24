from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from event_view.models import Event, UserEventLink
from event_view.forms import CreateEventForm, AddUsersForm, UpdateStatusForm
from group_profile.models import UserGroupLink
# Create your views here.


@login_required
def list_events(request):
    """
    list_events filters for username's events.
    Paginator paginates based on events with 3 per page.
    """
    username = request.user
    events = UserEventLink.objects.filter(customUser=username).order_by('event__StartDate')
    paginator = Paginator(events, 3)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    #generated this for loop with AI to get the linkedUsers to return the correct values and for
    #the pythonic for loop
    for link in page_obj.object_list:
        linkedUsers = UserEventLink.objects.filter(event=link.event).select_related('customUser')
        # attach a list of user objects so template can use attendee.username
        link.attendees = [linked.customUser for linked in linkedUsers]

    #taken from the event list view to show the user's groups...
    groupLinks = UserGroupLink.objects.filter(customUser=username).select_related('groupProfile')
    linkedGroups = []
    for link in groupLinks:
        item = {
            'group': link.groupProfile,
            'GroupShareCode': link.groupProfile.GroupShareCode,
            'GroupColour': link.groupProfile.GroupColour
        }
        linkedGroups.append(item)
        
    return render(request, 'calendar_view/list.html', {'page_obj': page_obj,})


@login_required
def edit_event(request, event_id):
    """
    Edit event and allow the logged-in user to update their UserEventLink.status.
    make sure get_or_create is unpacked into (obj, created).
    """
    response = ""
    event = get_object_or_404(Event, pk=event_id)
    # used AI here to fix an issue with the object being or not being a tuple...
    # unpack get_or_create -> user_link is the model instance
    user_link, created = UserEventLink.objects.get_or_create(customUser=request.user, event=event)

    # build attendees list for display
    event_links_qs = UserEventLink.objects.filter(event=event).select_related('customUser')
    linkedUsers = [{'user': link.customUser, 'status': link.get_status_display()} for link in event_links_qs]

    if request.method == 'POST':
        event_form = CreateEventForm(request.POST, instance=event)
        status_form = UpdateStatusForm(request.POST, instance=user_link)

        # update user status, stay on edit page
        if status_form.is_valid():
            status_form.save()
            return redirect('calendar:edit_event', event_id=event_id)
        #submit form changes, return to list
        if event_form.is_valid():
            event_form.save()
            return redirect('calendar:list')
    else:
        event_form = CreateEventForm(instance=event)
        status_form = UpdateStatusForm(instance=user_link)

    return render(request, 'calendar_view/edit_event.html', {
        'event_form': event_form,
        'status_form': status_form,
        'event': event,
        'response': response,
        'linkedUsers': linkedUsers,
    })


#based on the delete event here: https://www.w3schools.com/django/django_delete_record.php
#but utilises the edit_event code above. request param required even though unused.
def delete_event(request, event_id):
    """
    Event PK is passed on button press. Look for
    the Event, or 404. if found, delete the event and
    immediately redirect to the same list page.
    """
    event = get_object_or_404(Event, pk=event_id)
    event.delete()
    return HttpResponseRedirect(reverse('calendar:list'))