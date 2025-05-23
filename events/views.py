from django.shortcuts import render




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