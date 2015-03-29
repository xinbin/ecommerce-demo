from django.conf.urls import patterns, include, url

urlpatterns = patterns('page.views',
                           url(r'^docs/api/$', 'api'),
                           url(r'^about/$', 'about'),
                       )
