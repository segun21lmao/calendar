from django.shortcuts import render, redirect
from schedule.models import Calendar
from .forms import CalendarForm

def calendar_list(request):
    calendars = Calendar.objects.all()
    return render(request, 'events/calendar_list.html',
                  {"calendars": calendars})

def create_calendar(request):
    if request.method == "POST":
        form = CalendarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('calendar_list')
    else:
        form = CalendarForm()
    return render(request, 'events/create_calendar.html',
                  {"form": form})