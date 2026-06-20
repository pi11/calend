# -*- coding: utf-8 -*-

from django.urls import re_path
from cal.views import *
from .feed import HolidaysFeed

urlpatterns = [
    re_path(r'i/(\d+)/$', informer, name='informer'),
    re_path(r'informers/$', informers_list, name='informers_list'),
    re_path(r'd/(?P<month>\d+)/(?P<day>\d+)/$', day, name='holiday_date'),
    re_path(r'd/(?P<month>\d+)/$', day, name='holiday_date_month'),

    re_path(r'h/(\d+)/$', holiday, name='holiday'),
    re_path(r'all/$', all_holydays, name='all_holydays'),
    re_path(r'rss/$', HolidaysFeed(), name='rss'),
]
