from django.urls import path
from . import views

app_name ='calendar'

urlpatterns = [
    path('list/', views.list_events, name='list')
]
