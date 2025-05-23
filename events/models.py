from django.db import models
from schedule.models import Event
from colorfield.fields import ColorField     

class ExtraEvent(models.Model):
    base = models.OneToOneField(
        Event, on_delete=models.CASCADE,
        primary_key=True, related_name='extra'
    )

    address = models.CharField('Адрес', max_length=250, blank=True)

    lesson_type = models.CharField(
        'Тип занятия',
        max_length=30,
        choices=[('yoga', 'Йога'),
                 ('box',  'Бокс'),
                 ('run',  'Бег')],
        blank=True
    )

    color = ColorField('Цвет', default='#3896E8')     

    def __str__(self):
        return f"Дополнение к «{self.base.title}»"
# Create your models here.
