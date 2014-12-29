from django.conf.urls import patterns, url

from counsels.controllers import counsel, account


urlpatterns = patterns('',
   url(r'^$', counsel.index, name='index'),
   url(r'^post', counsel.post, name='post'),
   url(r'^login', account.login, name='login')
)
