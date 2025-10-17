from django.shortcuts import render, redirect
from .forms import CreateGroupForm, GroupProfile

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
    groups = GroupProfile.objects.all()
    search = GroupProfile.objects.filter(GroupName__icontains='Test')
    #template_name = "group_profile/create.html"
    #paginate_by =20
    return render(request, 'group_profile/join.html', {'groups': groups , 'search': search})

def search_group(request):
    print("entered search group")
    search = GroupProfile.objects.filter(name__icontains='Test')
    return render(request, 'group_profile/join.html', {'search': search})


