from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserForm
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

def logout_view(request):
    logout(request)
    return redirect("home")