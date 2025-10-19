from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CreateEventForm

# Create your views here.
@login_required
def create_event(request):
    print("create_event view called")
    if request.method == 'POST':
        form = CreateEventForm(request.POST)
        print("form called")
        if form.is_valid():
            form.save()
            response = "Event created."
            form = CreateEventForm()
        else:
            response="Unable to create that Event"

    else:
        form = CreateEventForm()
        response=""
    return render(request, 'event_view/create.html', {'form': form, 'response': response})