from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from event_view.models import Event,UserEventLink
# Create your views here.
@login_required
def list_events(request):
    username =  request.user
    events = UserEventLink.objects.filter(customUser=username)

    return render(request, 'calendar_view/list.html', {'events': events})