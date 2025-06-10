# events/views_calendar.py
from django.shortcuts import render, redirect, get_object_or_404
from django.http import QueryDict, HttpRequest, HttpResponse 

from schedule.models import Calendar, Event          # модели пакета django-schedule
from .forms import CalendarForm, EventForm, ExtraEventForm  # ваши формы


# ------------------------------------------------------------------
# Список календарей
# ------------------------------------------------------------------
def calendar_list(request: HttpRequest) -> HttpResponse:
    calendars = Calendar.objects.all()
    
    # Для отладки - добавьте переменные в контекст
    debug_vars = request.META.keys() if hasattr(request, 'META') else []
    
    return render(
        request,
        "events/calendar_list.html",
        {
            "calendars": calendars,
            "debug_vars": debug_vars
        },
    )


# ------------------------------------------------------------------
# Создание календаря
# ------------------------------------------------------------------
def create_calendar(request):
    """
    GET  → показать пустую форму.
    POST → сохранить календарь и перейти к списку (PRG-паттерн).
    """
    if request.method == 'POST':
        form = CalendarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('calendar_list')
    else:
        form = CalendarForm()

    return render(
        request,
        'events/create_calendar.html',
        {'form': form}
    )


# ------------------------------------------------------------------
# Создание события
# ------------------------------------------------------------------
def create_event(request, cal_id: int):
    calendar: Calendar = get_object_or_404(Calendar, id=cal_id)

    if request.method == 'POST':
        # клонируем POST-данные и «подклеиваем» id календаря
        data: QueryDict = request.POST.copy()
        data['calendar'] = calendar.id

        event_form = EventForm(data)
        extra_form = ExtraEventForm(request.POST)

        if event_form.is_valid() and extra_form.is_valid():
            event: Event = event_form.save()            # базовое событие
            extra = extra_form.save(commit=False)       # доп. данные
            extra.base = event
            extra.save()
            return redirect('calendar_list')
    else:
        event_form = EventForm(initial={'calendar': calendar.id})
        extra_form = ExtraEventForm()

    return render(
        request,
        'events/create_event.html',
        {
            'calendar': calendar,
            'event_form': event_form,
            'extra_form': extra_form,
        }
    )
