from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'basic.views.index', name='home'),
    url(r'^requests$', 'basic.views.requests', name='first-requests'),
    url(r'^edit$', 'basic.views.edit', name='edit-profile'),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login',
        {'template_name': 'login.html'}, name="login"),
                       
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('django.views.static',
            url(r'^uploads/(?P<path>.*)', 'serve', {'document_root': settings.MEDIA_ROOT}),
    )