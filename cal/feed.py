# -*- coding: utf-8 -*-

from datetime import date
from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from django.template.defaultfilters import truncatewords
from cal.models import Holiday

class HolidaysFeed(Feed):
    title = u"Праздники сегодня!"
    link = "/c/rss/"
    description = "Не пропустите ни одного праздника"

    def items(self):
        return Holiday.objects.filter(next_date=date.today())

    def item_title(self, item):
        return item.name

    def item_description(self, item):
        return "%s %s" % (truncatewords(item.description, 70), "<br /><br /> <img width='100px' src='%s' />" % item.image.url)

    def item_link(self, item):
        return reverse('holiday', args=[item.pk])
