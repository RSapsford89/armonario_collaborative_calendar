from django.urls import path
from . import views

app_name='event'

urlpatterns = [
    path('create/', views.create_event, name='create')
    #path('create/', views.create_event, name='create')

]
