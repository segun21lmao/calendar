# Generated by Django 4.2.21 on 2025-05-23 08:41

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='extraevent',
            name='color',
            field=colorfield.fields.ColorField(default='#3896E8', image_field=None, max_length=25, samples=None, verbose_name='Цвет'),
        ),
    ]
