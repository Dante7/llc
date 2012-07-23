from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'llc.views.home', name='home'),
    # url(r'^llc/', include('llc.foo.urls')),
    #url(r'^$', 'plantilla.views.template', name='template'),
    url(r'^$', 'plantilla.views.index', name='index'),

    #Url del sitio creadas por JJ
    #url(r'^$','plantilla.views.lista_medicos'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
