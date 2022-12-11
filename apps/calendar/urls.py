from django.views.generic import TemplateView
from django.conf.urls import include, url

from django.contrib import admin
from django.conf import settings


admin.autodiscover()

urlpatterns = [
    url(r'^schedule/', include('schedule.urls')),
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
