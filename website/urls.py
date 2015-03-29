from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('api.urls')),
    url('', include('ecommerce.urls')),
    url(r'^blog/', include('blog.urls')),
    url(r'', include('page.urls')),
)
