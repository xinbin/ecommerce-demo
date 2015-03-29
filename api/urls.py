from django.conf.urls import patterns, include, url

urlpatterns = patterns('api.views',
                       url(r'v1/products/$', 'products'),
                       url(r'v1/products/(?P<cid>[\d]+)/$', 'product'),
                       url(r'v1/categories/$', 'categories'),
                       url(r'v1/categories/(?P<cid>[\d]+)/$', 'category'),
                       url(r'v1/articles/$', 'articles'),
                       url(r'v1/articles/(?P<cid>[\d]+)/$', 'article'),
                       )
