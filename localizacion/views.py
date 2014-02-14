# Create your views here.
from django.shortcuts import render_to_response
from django.contrib.gis.shortcuts import render_to_kml
from localizacion.models import  Barrio,Negocio,Categoria
from productos.models import *
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
 
# hay que sacarlo de aca pero bueno despues
def all_kml2(request,id_n):
	 localizaciones = Negocio.objects.filter(id=id_n).kml()
	 return render_to_kml("kml/placemarks.kml", {'places':localizaciones})

def views_singlenegocio(request, id_neg):
	mapa              = True
	NEGOCIO           = Negocio.objects.get(id = id_neg)
	OFERTAS           = Oferta.objects.all().filter(negocio__id=id_neg)[:3]
	PRODUCTOS         = Producto.objects.filter(negocio__id=id_neg)[:5]
	usuario_designado = NEGOCIO.usuarios
#------------------- Cantidades --------------------------
	cantidad_ofertas_actuales   = Oferta.objects.all().filter(negocio__id=id_neg).count()
	cantidad_productos_actuales = Producto.objects.filter(negocio__id=id_neg).count()
#---------------------------------------------------------
	if request.user.is_authenticated():
		if not (usuario_designado == None):
			if (usuario_designado.id == request.user.id):
				designado = True 
				print "los dos id coinciden"
			else:
				designado = False
				print "los id son distintos"
		else:
			designado = False
			print "no tiene usuario designado"
	else:
		designado = False
		print "no esta autenticado"
#---------------------------------------------------------
	jsimagenes = True
	ctx = {
		'negocio'   :NEGOCIO,
		'productos' :PRODUCTOS,
		'mapa'      :True,
		'url_a_usar':'/kml2/',
		'id'        :NEGOCIO.id,
		'mapaG'     :mapa,
		'titulo'    :NEGOCIO.nombre,
		'ofertas'   :OFERTAS,
		'cantidad_ofertas_actuales'  :cantidad_ofertas_actuales,
		'cantidad_productos_actuales':cantidad_productos_actuales,
		'designado':designado,
		'jsimagenes':jsimagenes
		}
	all_kml2(request,NEGOCIO.id)
	return render_to_response('perfil/Singlenegocio.html',ctx,
		context_instance=RequestContext(request))


def barrios_referencia(request, id_barrio):
	referencia = Barrio.objects.get(id=id_barrio)
	lon        = referencia.lon
	lat        = referencia.lat
	nombre     = referencia.nombre
	ctx        = {'lon':lon,'lat':lat,'nombre':nombre}
	return render_to_response('kml/barrios.html',ctx,context_instance=RequestContext(request))
	

def not_found(request):
	return render_to_response('home/error/404.html',
		context_instance=RequestContext(request))

def server_error(request):
	return render_to_response('home/error/500.html',
		context_instance=RequestContext(request))
