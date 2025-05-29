



from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, HttpResponse
from schedule.models import Calendar, Event
from .forms import CalendarForm, EventForm, ExtraEventForm


# --------------------------------------------------
# Список календарей
# --------------------------------------------------
def calendar_list(request: HttpRequest) -> HttpResponse:
    calendars = Calendar.objects.all()
    return render(
        request,
        "events/calendar_list.html",
        {"calendars": calendars},
    )


# --------------------------------------------------
# Создание календаря
# --------------------------------------------------
def create_calendar(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = CalendarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("calendar_list")
    else:
        form = CalendarForm()

    return render(
        request,
        "events/create_calendar.html",
        {"form": form},
    )


# --------------------------------------------------
# Создание события
# --------------------------------------------------
def create_event(request: HttpRequest, cal_id: int) -> HttpResponse:
    calendar = get_object_or_404(Calendar, pk=cal_id)

    if request.method == "POST":
        event_form = EventForm(request.POST)
        extra_form = ExtraEventForm(request.POST)

        if event_form.is_valid() and extra_form.is_valid():
            # 1. создаём Event, вручную привязываем к календарю
            event: Event = event_form.save(commit=False)
            event.calendar = calendar
            event.save()

            # 2. создаём ExtraEvent (или как он у вас называется)
            extra = extra_form.save(commit=False)
            extra.base = event          # поле base ссылается на Event
            extra.save()

            return redirect("calendar_list")
    else:
        event_form = EventForm()
        extra_form = ExtraEventForm()

    return render(
        request,
        "events/create_event.html",
        {
            "calendar": calendar,
            "event_form": event_form,
            "extra_form": extra_form,
        },
    )





from datetime import timedelta
from django.utils import timezone
from django.shortcuts import render
from schedule.models import Calendar, Occurrence

def next7(request):
    # Получаем календарь
    cal = Calendar.objects.get(slug='main')
    
    # Текущее время и время через 7 дней
    now = timezone.now()
    end_date = now + timedelta(days=7)
    
    # Получаем все Occurrence (вхождения событий) для этого календаря в диапазоне дат
    occurrences = Occurrence.objects.filter(
        event__calendar=cal,  # События из нужного календаря
        start__gte=now,       # Начало >= текущего времени
        start__lte=end_date   # Начало <= текущее время + 7 дней
    ).order_by('start')
    
    return render(request, 'next7.html', {'occurrences': occurrences})

# Create your views here.