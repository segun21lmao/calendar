from schedule.models import Calendar, Event
from django import forms
from colorfield.widgets import ColorWidget
from .models import ExtraEvent


class CalendarForm(forms.ModelForm):
    class Meta:
        model = Calendar
        fields = ("name", "slug")




class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ("calendar", "title", "start", "end", "color_event")
        widgets = {
            "color_event": ColorWidget(attrs={"style": "width:6rem"})
        }


 

class ExtraEventForm(forms.ModelForm):
    class Meta:
        model = ExtraEvent
        fields = ("address", "lesson_type")