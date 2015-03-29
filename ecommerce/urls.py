from django.conf.urls import patterns, include, url

urlpatterns = patterns('ecommerce.views',
                       url(r'^$', 'home'),
                       url(r'catalog/$', 'catalog'),
                       url(r'catalog/(?P<cid>[\d]+)/$', 'products'),
                       url(r'products/(?P<pid>[\d]+)/$', 'product'),
                       url(r'specials/$', 'specials'),
                       url(r'cart/add/(?P<pid>[\d]+)/$', 'cart_add'),
                       url(r'cart/remove/(?P<pid>[\d]+)/$', 'cart_remove'),
                       url(r'cart/$', 'cart_display'),
                       )
