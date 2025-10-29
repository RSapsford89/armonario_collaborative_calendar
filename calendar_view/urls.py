from django.urls import path
from . import views

app_name = 'calendar'

urlpatterns = [
    path('list/', views.list_events, name='list'),
    path('edit/<int:event_id>/', views.edit_event, name='edit_event'),  # django docs on URLs for <int:event_id>
    path('delete/<int:event_id>/', views.delete_event, name='delete_event'),
]
