from django.urls import path
from .views_calendar import calendar_list, create_calendar   
from .views_event import create_event                    

urlpatterns = [
    path('', calendar_list, name='calendar_list'),
    path('calendar/add/', create_calendar, name='create_calendar'),
    path('calendar/<int:cal_id>/event/add/', create_event,
         name='create_event'),
]
