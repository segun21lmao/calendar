from django.contrib import admin
from schedule.admin import EventAdmin as ScheduleEventAdmin
from schedule.models import Event
from .models import ExtraEvent

class ExtraEventInline(admin.StackedInline):
    model = ExtraEvent
    max_num = 1
    extra = 0
    fields = ('address', 'lesson_type', 'color')

class EventAdmin(ScheduleEventAdmin):
    inlines = [ExtraEventInline]

admin.site.unregister(Event)
admin.site.register(Event, EventAdmin)




# Register your models here.
