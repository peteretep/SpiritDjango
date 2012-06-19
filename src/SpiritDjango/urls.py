from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^review/$', 'guestbook.views.review'),    
    url(r'^tours/$', 'home.views.tours'),
    url(r'^angling/$', 'home.views.angling'),
    url(r'^wildlife/$', 'home.views.wildlife'),
    url(r'^book/$', 'home.views.book'),       
    
    # Examples:
    url(r'^$', 'home.views.index', name='home'),
    # url(r'^SpiritDjango/', include('SpiritDjango.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
