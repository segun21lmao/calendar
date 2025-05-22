from django.shortcuts import render




from datetime import timedelta
from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404
from schedule.models import Calendar

def next7(request):
    
    cal = Calendar.objects.get(slug='main')     
    now = timezone.now()                       
    week_ahead = now + timedelta(days=7)        
    occs = cal.occurrences(now, week_ahead)     
    return render(request,                     
                  'events/next7.html',          
                  {'occurrences': occs})


# Create your views here.