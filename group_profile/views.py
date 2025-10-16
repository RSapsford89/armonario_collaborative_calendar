from django.shortcuts import render, redirect
from .forms import GroupForm

# Create your views here.

def create_group(request):
    print("create_group view called")
    if request.method == 'POST':
        form = GroupForm(request.POST)
        print("form called")
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = GroupForm()
    return render(request, 'group_profile/create.html', {'form': form})