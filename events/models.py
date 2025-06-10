from django.db import models
from schedule.models import Event
from colorfield.fields import ColorField     

class ExtraEvent(models.Model):

    color = ColorField('Цвет', default='#3896E8')   
    base = models.OneToOneField(Event, on_delete=models.CASCADE,
                                primary_key=True, related_name='extraevent')
    drugs = models.CharField('Название лекарства', max_length=250, default="extraevent")
    dose = models.CharField('Доза', max_length=250, default="0")

    def __str__(self):
        return f"Дополнение к «{self.base.title}»"
    


