from django.urls import include, path

from django.contrib import admin
from cal.views import index

urlpatterns = [
    path('', index, name="index"),
    path('c/', include('cal.urls')),
    path('admin/', admin.site.urls),
]
