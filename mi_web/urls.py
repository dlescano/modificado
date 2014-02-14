from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin

admin.autodiscover()

handler500 = 'localizacion.views.server_error'
handler404 = 'localizacion.views.not_found'

urlpatterns = patterns('',
    url(r'^', include('home.urls')),
    url(r'^', include('localizacion.urls')),
    url(r'^', include('productos.urls')),
    url(r'^admin/', include(admin.site.urls)),
	url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),
)
