from django.conf.urls import patterns, url, include

from localizacion.views import *

urlpatterns = patterns('localizacion.views',
    url(r'^Singlenegocio/(?P<id_neg>.*)/$',views_singlenegocio,name='Singlenegocio'),
    url(r'^kml2/(?P<id_n>.*)/$',all_kml2),
    url(r'^barrio_referencia/(?P<id_barrio>.*)/$',barrios_referencia,name='barrio'),
    )
