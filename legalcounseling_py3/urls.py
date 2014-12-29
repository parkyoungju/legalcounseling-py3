from django.conf.urls import patterns, include, url
from django.contrib import admin

from counsels.controllers import counsel, account


urlpatterns = patterns('',
    url(r'^counsels/', include('counsels.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', counsel.index, name='index'),
    url(r'^login', account.login, name='login')
)
