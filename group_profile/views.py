from django.shortcuts import render, redirect
from .forms import CreateGroupForm, GroupProfile
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

def list_group(request):
    #groups = GroupProfile.objects.all()
    #search = GroupProfile.objects.filter(GroupName__icontains='Test')
    group_query = request.POST.get("group_search","")
    sharecode_query = request.POST.get("sharecode_test", "")
    #if sharecode does not match group_query found, deny
    print(f'The pre-tested input was: {group_query} {len(group_query)}')
    if len(group_query) or len(sharecode_query) < 1:
        print("this is a fail")
        print(f'The fetched input was: {group_query}')
        #return redirect('group/join.html')#this becomes a looping failure
    print(group_query)
    groups = GroupProfile.objects.filter(GroupName__contains=group_query , GroupShareCode__contains=sharecode_query)
    #sharecode = GroupProfile.objects.filter(GroupShareCode__contains=sharecode_query)
    print(groups)
    
    #search = GroupProfile.objects.filter(Q(GroupName__icontains=query))
    return render(request, 'group_profile/join.html', {'groups': groups ,  })

def search_db(self):
    query = self.request.POST.get('q')
    return GroupProfile.objects.filter(Q(name__contains=query))


def search_group(request):
    print("entered search group")
    search = GroupProfile.objects.filter(name__icontains='Test')
    return render(request, 'group_profile/join.html', {'search': search})


