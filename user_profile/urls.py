from django.urls import path
from . import views

app_name = 'user_profile'

urlpatterns = [
    path('register/', views.register_views, name='register'),
    path('login/', views.login_views, name='login'),
    path('profile/', views.profile_views, name='profile'),
]
