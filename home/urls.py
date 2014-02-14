from django.conf.urls import patterns, url, include

from home.views_home import *
urlpatterns = patterns('home.views',
	url(r'^$', views_index, name='index'),
	url(r'^info/$',views_info_registro,name='info'),
	url(r'^contacto/$',views_Contact,name='contacto'),
	url(r'^login/$',views_login,name='login'),
	url(r'^logout/$',views_logout,name='logout'),
	#url(r'^registro_user/$',views_registro,name='registro_usuarios'),
	#para provar el nuevo index
	url(r'^index2/$', index2, name='index2'),
	)