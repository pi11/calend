from django.conf.urls import *

from django.contrib import admin
from cal.views import index

admin.autodiscover()

urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^c/', include('cal.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
