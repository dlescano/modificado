from django.conf.urls import patterns, url, include

from productos.views import *


urlpatterns = patterns('productos.views',
	url(r'^listado-productos/pagina/(?P<id_neg>.*)/(?P<pagina>.*)/$',listadoProd, name='listado-prod'),
	url(r'^listado-ofertas/pagina/(?P<id_neg>.*)/(?P<pagina>.*)/$',listadoOfertas, name='listado-oferta'),
#------------------------------PRODUCTOS----------------------------------------------------
	url(r'^producto/(?P<id_pro>.*)/$',producto, name='producto'),
	url(r'^nuevo_producto/(?P<id_neg>.*)/$',nuevo_producto, name='nuevo_producto'),
	url(r'^editar_producto/(?P<id_prod>.*)/$',editar_producto, name='editar_producto'),
	url(r'^borrar_producto/(?P<id_prod>.*)/$',borrar_producto, name='borrar_producto'),
#-------------------------------------------------------------------------------------------
#------------------------------OFERTAS------------------------------------------------------
	url(r'^oferta/(?P<id_ofer>.*)/$',oferta, name='oferta'),
	url(r'^nueva_oferta/(?P<id_neg>.*)/$',nueva_oferta, name='nueva_oferta'),
	url(r'^editar_oferta/(?P<id_ofer>.*)/$',editar_oferta,name='editar_oferta'),
	url(r'^borrar_oferta/(?P<id_ofer>.*)/$',borrar_oferta, name='borrar_oferta')
#------------------------------PRODUCTOS----------------------------------------------------
	)
