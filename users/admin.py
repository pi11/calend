# -*- coding: utf-8 -*-
# Admin configuration Users
# 

from django.contrib import admin

from users.models import *

class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user",)

admin.site.register(Profile, ProfileAdmin)

