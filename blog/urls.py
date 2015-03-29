from django.conf.urls import patterns, include, url

urlpatterns = patterns('blog.views',
                       url(r'^$', 'index'),
                       url(r'(?P<aid>[\d]+)/$', 'article'),
                       )
