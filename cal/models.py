# -*- coding: utf-8 -*-
# Calendar Models

from datetime import datetime, date
from datetime import timedelta
from calendar import monthrange

from django.db import models
from django.conf import settings

from users.models import Profile
from djangohelpers.images import scale

MONTHS = (
    (1, u'Январь'),
    (2, u'Февраль'),
    (3, u'Март'),
    (4, u'Апрель'),
    (5, u'Май'),
    (6, u'Июнь'),
    (7, u'Июль'),
    (8, u'Август'),
    (9, u'Сентябрь'),
    (10, u'Октябрь'),
    (11, u'Ноябрь'),
    (12, u'Декабрь'),
)

MONTHS_R = (
    (1, u'Января'),
    (2, u'Февраля'),
    (3, u'Марта'),
    (4, u'Апреля'),
    (5, u'Мая'),
    (6, u'Июня'),
    (7, u'Июля'),
    (8, u'Августа'),
    (9, u'Сентября'),
    (10, u'Октября'),
    (11, u'Ноября'),
    (12, u'Декабря'),
)

DAYS = ((x, x) for x in xrange(1, 32))

DATE_TYPES = (
    (0, u'Обычная дата'),
    (1, u'Номер дня недели в месяце'),
    (2, u'Номер дня в году'),
)

DAYS_OF_WEEK = (
    (0, u'Не выбрано'),

    (1, u'Понедельник'),
    (2, u'Вторник'),
    (3, u'Среда'),
    (4, u'Четверг'),
    (5, u'Пятница'),
    (6, u'Суббота'),
    (7, u'Воскресенье'),

)
WEEK_OF_MONTHS = (
    (0, u'Не выбрано'),
    (1, u'Первая неделя месяца'),
    (2, u'Вторая неделя месяца'),
    (3, u'Третья неделя месяца'),
    (4, u'Четвертая неделя месяца'),
)


class Holiday(models.Model):

    """Holiday model"""
    name = models.CharField(max_length=400)
    image = models.ImageField(upload_to="uploads/%Y-%m-%d/",
                              null=True, blank=True)
    profile = models.ForeignKey(Profile)
    description = models.TextField()
    date_type = models.IntegerField(choices=DATE_TYPES, default=0)
    month = models.IntegerField(choices=MONTHS, default=1,
                                verbose_name=u"Месяц")
    day = models.IntegerField(choices=DAYS, default=1,
                              verbose_name=u"День месяца")

    day_of_the_year = models.IntegerField(default=0,
                                          verbose_name=u"Номер дня в году")
    week_of_the_month = models.IntegerField(default=0,
                                            verbose_name=u"Номер недели в месяце",
                                            choices=WEEK_OF_MONTHS)
    week_day = models.IntegerField(default=0, verbose_name=u"День недели",
                                   choices=DAYS_OF_WEEK)
    publication_date = models.DateTimeField(auto_now=True)
    is_public = models.BooleanField(default=False)
    next_date = models.DateField(null=True, blank=True,
                                 verbose_name=u"Следующая дата праздника")

    def __unicode__(self):
        return self.name

    def get_thumb(self):
        try:
            thumb = scale(self.image, "%sx%s" % (settings.THUMB_WIDTH,
                                                 settings.THUMB_HEIGHT))
        except:
            import traceback
            print traceback.format_exc()
            thumb = False
        return thumb

    def get_date(self):
        now = datetime.now()
        now_date = date(now.year, now.month, now.day)
        if self.date_type == 0:
            next_date = date(now.year, self.month, self.day)
        elif self.date_type == 1:
            start_date = date(now.year, self.month, 1)
            current_week = 1
            # print self.week_day, self.week_of_the_month
            for dm in range(0, monthrange(now.year, self.month)[1]):  # go trough month
                # print dm
                # pd = dm - 1
                cd = start_date + timedelta(days=dm)
                # print "Weekday", cd.weekday() + 1, "Need", self.week_day, cd,
                # current_week

                if self.week_of_the_month <= current_week:
                    if cd.weekday() + 1 == self.week_day:
                        next_date = cd
                        break
                if cd.weekday() + 1 == self.week_day:  # and dm > 0:
                    current_week += 1
                    # print "INC week", current_week, 'need week',
                    # self.week_of_the_month

            # print next_date
        elif self.date_type == 2:
            next_date = date(now.year, 1, 1) + timedelta(
                days=self.day_of_the_year - 1)
        return next_date

    def get_day(self):
        return self.next_date.day

    def get_month(self):
        return self.next_date.month


class PostCard(models.Model):
    image = models.ImageField(upload_to="uploads/%Y-%m-%d/")
    holiday = models.ForeignKey(Holiday, blank=True, null=True)
    publication_date = models.DateTimeField(auto_now=True)
    informer_x = models.IntegerField(default=0)
    informer_y = models.IntegerField(default=0)
    image_width = models.IntegerField(default=0)
    image_height = models.IntegerField(default=0)
    informer_font = models.CharField(max_length=50, default="")
    is_informer = models.BooleanField(default=False)

    def __unicode__(self):
        return u"%s - %s" % (self.id, self.holiday)

    def get_date_to(self):
        if self.holiday:
            now = datetime.now()
            now_date = date(now.year, now.month, now.day)
            next_date = self.holiday.next_date  # date(now.year, self.holiday.month, self.holiday.day)
            if next_date < now_date:
                n_year = now.year + 1
                next_date = self.holiday.next_date + \
                    timedelta(
                        days=365)  # date(n_year, self.holiday.month, self.holiday.day)
            days = next_date - now_date

            return days.days
        else:
            # print "No hollyday"
            return False
