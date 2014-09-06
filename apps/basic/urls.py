from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'basic.views.index', name='home'),
    url(r'^requests$', 'basic.views.requests', name='first-requests'),
    
    url(r'^admin/', include(admin.site.urls)),
)