from django.urls import path
from . import views

app_name = 'group_profile'

urlpatterns = [
    path('create/', views.create_group, name='create'),
    path('join/', views.list_group, name='join'),

]
