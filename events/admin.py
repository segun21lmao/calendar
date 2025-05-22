from django.contrib import admin
from schedule.admin import EventAdmin as ScheduleEventAdmin
from schedule.models import Event
from .models import ExtraEvent

class ExtraEventInline(admin.StackedInline):
    model = ExtraEvent
    max_num = 1
    extra = 0

class EventAdmin(ScheduleEventAdmin):
    inlines = [ExtraEventInline]

admin.site.unregister(Event)
admin.site.register(Event, EventAdmin)





from recurrence.forms import RecurrenceWidget
from recurrence.fields import RecurrenceField
from .models import FancyEvent

@admin.register(FancyEvent)
class FancyEventAdmin(admin.ModelAdmin):
    formfield_overrides = {RecurrenceField: {'widget': RecurrenceWidget}}
# Register your models here.
