from django.shortcuts import render, redirect
from .forms import CreateGroupForm
from .models import GroupProfile
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Create your views here.
def create_group(request):
    print("create_group view called")
    if request.method == 'POST':
        form = CreateGroupForm(request.POST)
        print("form called")
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = CreateGroupForm()
    return render(request, 'group_profile/create.html', {'form': form})

@login_required
def list_group(request):
    """
    Method to search for the user entered Group
    Name and ShareCode. Checks query and sharecode
    return valid/exist before attempting to join user
    to the group. BUG: how to test entry into
    UsergroupLink is unique (i.e user not already related)
    """
    response=""
    if request.method == "POST":
        group_query = request.POST.get("group_search","")
        sharecode_query = request.POST.get("sharecode_test", "")
        
        if not group_query or not sharecode_query:
            print(group_query)
            response = "Request to join failed - Enter the exact name and sharecode again"
        else:
            group = GroupProfile.objects.filter(GroupName__iexact=group_query, GroupShareCode=sharecode_query).first()
            group.members.add(request.user, through_defaults={'status': 2})
            response = "Correct credentials entered. You are being added to the group"
    else:
        group_query=""
        sharecode_query=""
    groups = GroupProfile.objects.filter(GroupName__contains=group_query , GroupShareCode__contains=sharecode_query)#remove after testing
    
    return render(request, 'group_profile/join.html', {'groups': groups, 'response': response})

