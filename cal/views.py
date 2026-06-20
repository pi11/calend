# Create your views here.

from datetime import datetime, date, timedelta

from django.shortcuts import get_object_or_404, render
from django.db.models import Q 
from django.conf import settings

from cal.models import *


def informer(request, i_id):
    i = get_object_or_404(PostCard, pk=i_id)
    if i.get_date_to() < 100:
        delta = 25
    elif i.get_date_to() < 10:
        delta = 50
    else:
        delta = 0
    return render(request, 'informer.html', locals())

def index(request):
    now = datetime.now()
#    print now.year, now.month, now.day
    now_date = date(now.year, now.month, now.day)
    next_date = date(now.year, now.month, now.day) + timedelta(days=1)
    holidays = Holiday.objects.filter(next_date=now_date).order_by("-next_date")
    tholidays = Holiday.objects.filter(next_date=next_date).order_by("-next_date")
    return render(request, 'index.html', locals())

def informers_list(request):
    site_url = settings.SITE_URL
    informers = PostCard.objects.filter(is_informer=True)
    return render(request, "informers.html", locals())

def day(request, month, day=None):
    month = int(month)
    now = datetime.now()
    now_date = date(now.year, now.month, now.day)
    next_date = date(now.year+1, now.month, now.day)
    if day:
        day = int(day)
        current_date = date(now.year, month, day)
        holidays = Holiday.objects.filter(Q(next_date=current_date)|Q(next_date=next_date)).order_by("next_date") 
    else:
        current_date = date(now.year, month, 1)
        holidays = Holiday.objects.filter(month=month).order_by("next_date")
    return render(request, "day.html", locals())

def holiday(request, pk):
    holiday = get_object_or_404(Holiday, pk=pk)
    return render(request, "holiday.html", locals())

def all_holydays(request):
    holidays = Holiday.objects.filter(is_public=True).order_by("next_date")
    return render(request, "all_holydays.html", {"holidays": holidays})
