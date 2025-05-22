from django.db import models
from schedule.models import Event



class ExtraEvent(models.Model):
    base = models.OneToOneField(Event, on_delete=models.CASCADE,
                                primary_key=True, related_name='extra')
    address = models.CharField('Адрес', max_length=250, blank=True)
    lesson_type = models.CharField('Тип занятия',
        max_length=30,
        choices=[('yoga', 'Йога'), ('box', 'Бокс'), ('run', 'Бег')],
        blank=True)

    def __str__(self):
        return f"Дополнение к «{self.base.title}»"
    







from recurrence.fields import RecurrenceField
from recurrence import Recurrence, Rule, DAILY
# другие импорты…

class FancyEvent(models.Model):
    title       = models.CharField(max_length=120)
    start_time  = models.TimeField()
    start_date  = models.DateField()
    end_date    = models.DateField()
    rrule       = RecurrenceField(
        default=lambda: Recurrence(rrules=[Rule(freq=DAILY)])
    )

    def __str__(self):
        return self.title

# Create your models here.
