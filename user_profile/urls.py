from django.urls import path
from . import views

app_name = 'user_profile'

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('edit/<int:user_id>', views.edit_view, name='edit_view'),
]
