from django.shortcuts import render, redirect, get_object_or_404
from schedule.models import Calendar
from .forms import EventForm, ExtraEventForm
from .models import ExtraEvent

def create_event(request, cal_id):
    calendar = get_object_or_404(Calendar, id=cal_id)

    if request.method == "POST":
        event_form = EventForm(request.POST)
        extra_form = ExtraEventForm(request.POST)

        
        event_form.data = event_form.data.copy()
        event_form.data['calendar'] = calendar.id

        if event_form.is_valid() and extra_form.is_valid():
            event = event_form.save()               
            extra = extra_form.save(commit=False)   
            extra.base = event
            extra.save()
            return redirect('calendar_list')
    else:
        event_form = EventForm(initial={"calendar": calendar})
        extra_form = ExtraEventForm()

    return render(request, 'events/create_event.html', {
        "calendar": calendar,
        "event_form": event_form,
        "extra_form": extra_form,
    })