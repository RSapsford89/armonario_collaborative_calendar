from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import CreateGroupForm
from .models import GroupProfile, UserGroupLink
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Create your views here.
@login_required
def create_group(request):
    if request.method == 'POST':
        form = CreateGroupForm(request.POST)
        if form.is_valid():
            group = form.save()
            UserGroupLink.objects.create(customUser=request.user, groupProfile=group, status=1)
            response = "Group created."
            form = CreateGroupForm()
        else:
            response="Unable to create that Group"

    else:
        form = CreateGroupForm()
        response=""
    return render(request, 'group_profile/create.html', {'form': form, 'response': response})


def leave_group(request,group_id):
    """
    Group PK is passed on button press. Look for
    the Group, or 404. if found, delete the event and
    immediately redirect to the same list page.
    """
    group = get_object_or_404(GroupProfile, pk=group_id)
    UserGroupLink.objects.filter(customUser=request.user, groupProfile=group).delete()
    
    return HttpResponseRedirect(reverse('user:profile'))


@login_required
def list_group(request):
    """
    Method to search for the user entered Group
    Name and ShareCode. Checks query and sharecode
    return valid/exist before attempting to join user
    to the group.
    """
    response = ""
    groups = []
    if request.method == "POST":
        group_query = request.POST.get("group_search","").strip()
        sharecode_query = request.POST.get("sharecode_test", "").strip()
        if not group_query or not sharecode_query:
            print(group_query)
            response = "Request to join failed - Enter the exact name and sharecode again"
        else:
            group = GroupProfile.objects.filter(GroupName__iexact=group_query, GroupShareCode=sharecode_query).first()
            
            if group:
                alreadyMember = UserGroupLink.objects.filter(customUser=request.user, groupProfile=group).exists()
                if alreadyMember:
                    response = "You are already a member of this Group"
                else:
                    group.members.add(request.user, through_defaults={'status': 2})
                    response = "Correct credentials entered. You are being added to the group"
    else:
        group_query = ""
        sharecode_query = ""
    
    return render(request, 'group_profile/join.html', {'groups': groups, 'response': response})

