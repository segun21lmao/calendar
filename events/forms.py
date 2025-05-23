from schedule.models import Calendar
from django import forms

class CalendarForm(forms.ModelForm):
    class Meta:
        model = Calendar
        fields = ("name", "slug")