# -*- coding: utf-8 -*-

from django.conf.urls import *
from cal.views import *
from .feed import HolidaysFeed

urlpatterns = [
    url('i/(\d+)/$', informer, name='informer'),
    url('informers/$', informers_list, name='informers_list'),
    url('d/(?P<month>\d+)/(?P<day>\d+)/$', day, name='holiday_date'),
    url('d/(?P<month>\d+)/$', day, name='holiday_date_month'),

    url('h/(\d+)/$', holiday, name='holiday'),
    url('all/$', all_holydays, name='all_holydays'),
    url('rss/$', HolidaysFeed(), name='rss'),
]
