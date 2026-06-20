# -*- coding: utf-8 -*-

from django.contrib import admin

from cal.models import *


class HolidayAdmin(admin.ModelAdmin):
    list_display = ["name", "publication_date", "next_date"]
    search_fields = ["name", "description"]

class PostCardAdmin(admin.ModelAdmin):
    list_display = ["__str__"]

admin.site.register(Holiday, HolidayAdmin)
admin.site.register(PostCard, PostCardAdmin)

