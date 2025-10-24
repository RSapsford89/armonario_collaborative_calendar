from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from event_view.models import Event, UserEventLink
from event_view.forms import CreateEventForm, UpdateStatusForm
# Create your views here.


@login_required
def list_events(request):
    """
    List events the user is directly linked to (via UserEventLink)
    AND events linked to groups the user is a member of (via event.group).
    Paginate and attach attendees for each.
    """
    user = request.user

    # 1) Events user is directly linked to
    personal_links = (
        UserEventLink.objects
        .filter(customUser=user)
        .select_related('event', 'event__group')
        .order_by('event__StartDate', 'event__StartTime', 'pk')
    )
    personal_event_ids = {link.event.id for link in personal_links}

    # 2) Events linked to groups the user is a member of (exclude already-listed personal events)
    group_events = (
        Event.objects
        .filter(group__members=user)
        .exclude(id__in=personal_event_ids)
        .select_related('group')
        .order_by('StartDate', 'StartTime', 'pk')
    )

    # 3) Build unified list of items for display
    items = []

    # add personal links
    for link in personal_links:
        attendees_qs = UserEventLink.objects.filter(event=link.event).select_related('customUser')
        items.append({
            'type': 'personal',
            'event': link.event,
            'user_status': link.get_status_display(),
            'attendees': [a.customUser for a in attendees_qs],
            'group': link.event.group,  # may be None
        })

    # add group events (no personal link)
    for ev in group_events:
        attendees_qs = UserEventLink.objects.filter(event=ev).select_related('customUser')
        items.append({
            'type': 'group',
            'event': ev,
            'user_status': None,  # user has no personal link
            'attendees': [a.customUser for a in attendees_qs],
            'group': ev.group,
        })

    # 4) Paginate the merged list
    paginator = Paginator(items, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'calendar_view/list.html', {'page_obj': page_obj})


@login_required
def edit_event(request, event_id):
    """
    Edit event and allow the logged-in user to update their UserEventLink.status.
    make sure get_or_create is unpacked into (obj, created).
    """
    response = ""
    event = get_object_or_404(Event, pk=event_id)
    # unpack get_or_create -> user_link is the model instance
    user_link, created = UserEventLink.objects.get_or_create(customUser=request.user, event=event)

    # build attendees list for display
    event_links_qs = UserEventLink.objects.filter(event=event).select_related('customUser')
    linkedUsers = [{'user': link.customUser, 'status': link.get_status_display()} for link in event_links_qs]

    if request.method == 'POST':
        event_form = CreateEventForm(request.POST, instance=event, user=request.user)
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
        event_form = CreateEventForm(instance=event, user=request.user)
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