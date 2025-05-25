"""
URL configuration for mycal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from events.views import next7          # если next7 действительно в events/views.py

urlpatterns = [
    path('',  include('events.urls')),   # ← корневые страницы вашего приложения
    path('admin/', admin.site.urls),
    path('calendar/', include('schedule.urls')),
    path('next7/', next7, name='next7'),  # уберите эту строку, если next7 не нужно
]
