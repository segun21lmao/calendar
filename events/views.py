from django.shortcuts import render

from datetime import timedelta
from django.utils import timezone
from django.shortcuts import render
from schedule.models import Calendar

def next7(request):
    cal = Calendar.objects.get(slug='main')
    now = timezone.now()
    occs = cal.occurrences(now, now + timedelta(days=7))
    return render(request, 'next7.html', {'occurrences': occs})
# Create your views here.