from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import CustomUserForm, CustomUserFormEdit
from user_profile.models import CustomUser
from django.contrib.auth import login, logout
# Create your views here.

def register_view(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect("home")
    else:
        form = CustomUserForm()
    return render(request, 'user_profile/register.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        # pass the request so AuthenticationForm can access request-specific
        # data (important for some authentication backends)
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("home")
    else:
        form = AuthenticationForm()
    return render(request, 'user_profile/login.html', {"form": form})

def profile_view(request):
    return render(request, 'user_profile/profile.html')

@login_required
def edit_view(request, user_id):
    """
    Edit the user profile view.
    """
    response=""
    user = get_object_or_404(CustomUser, pk=user_id)

    if request.method == 'POST':
        form = CustomUserFormEdit(request.POST, instance=user,)
        if form.is_valid():
            form.save()
            response="Update saved."
            return redirect('user:profile')
    else:
        response="Something went wrong..."
        form = CustomUserFormEdit(instance=user, )
    return render(request, 'user_profile/edit.html', {'form': form, 'user': user})

def logout_view(request):
    logout(request)
    return redirect("home")