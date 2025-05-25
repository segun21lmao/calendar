from django.shortcuts import render, redirect, get_object_or_404
from schedule.models import Calendar
from .forms import CalendarForm, EventForm, ExtraEventForm   


def calendar_list(request):
    calendars = Calendar.objects.all()
    return render(request,
                  'events/calendar_list.html',
                  {"calendars": calendars})



def create_calendar(request):
    if request.method == "POST":
        form = CalendarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('calendar_list')
    else:
        form = CalendarForm()

    return render(request,
                  'events/create_calendar.html',
                  {"form": form})



def create_event(request, cal_id):
    calendar = get_object_or_404(Calendar, id=cal_id)

    if request.method == "POST":
        event_form = EventForm(request.POST)
        extra_form = ExtraEventForm(request.POST)

        
        event_form.data = event_form.data.copy()   
        event_form.data['calendar'] = calendar.id

        if event_form.is_valid() and extra_form.is_valid():
            ev = event_form.save()                
            ex = extra_form.save(commit=False)     
            ex.base = ev                           
            ex.save()
            return redirect('calendar_list')
    else:
        event_form = EventForm(initial={"calendar": calendar})
        extra_form = ExtraEventForm()

    return render(request,
                  'events/create_event.html',
                  {
                      "calendar": calendar,
                      "event_form": event_form,
                      "extra_form": extra_form,
                  })





