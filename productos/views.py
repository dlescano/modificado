from productos.models import Producto,Oferta
from localizacion.models import Negocio
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator,EmptyPage, InvalidPage
from django.contrib.auth.decorators import login_required
from productos.forms import *

def listadoProd(request,id_neg,pagina):
	PRODUCTOS         = Producto.objects.all().filter(negocio__id=id_neg)
	designado         = False
	producto          = PRODUCTOS[0]#tomamos un elemento de referencia
	usuario_designado = producto.negocio.usuarios

	if request.user.is_authenticated():
		if (request.user.id == usuario_designado.id) or request.user.is_staff:
			designado = True
		else:
			designado = False
	else:
		designado = False

	paginator = Paginator(PRODUCTOS,4)
	try:
		page = int(pagina)
	except:
		page = 1
	try:
		productos = paginator.page(page)
	except (EmptyPage,InvalidPage):
		productos = paginator.page(paginator.num_pages)
	jsimagenes = True
	titulo = producto.negocio.nombre
	ctx        = {'productos':productos,
				  'jsimagenes':jsimagenes,
				  'id_neg':id_neg,
				  'designado':designado,
				  'titulo':titulo
				  }
	return render_to_response('listados/listado-productos.html',
		ctx,context_instance=RequestContext(request))
	



def listadoOfertas(request,id_neg,pagina):
	OFERTAS    = Oferta.objects.all().filter(negocio__id=id_neg)
	designado         = False
	oferta          = OFERTAS[0]#tomamos un elemento de referencia
	usuario_designado = oferta.negocio.usuarios
	if request.user.is_authenticated():
		if (request.user.id == usuario_designado.id) or request.user.is_staff:
			designado = True
		else:
			designado = False
	else:
		designado = False
	paginator = Paginator(OFERTAS,4)
	try:
		page = int(pagina)
	except:
		page = 1
	try:
		ofertas = paginator.page(page)
	except (EmptyPage,InvalidPage):
		ofertas = paginator.page(paginator.num_pages)
	jsimagenes = True
	titulo = oferta.negocio.nombre
	jsimagenes = True
	ctx        = {'ofertas':ofertas,
				  'jsimagenes':jsimagenes,
				  'id_neg':id_neg,
				  'designado':designado,
				  'titulo':titulo
				 }
	return render_to_response('listados/listado-ofertas.html',
		ctx,context_instance=RequestContext(request))

#-----------------------/ABM PRODUCTOS/------------------------------------------------
def producto(request,id_pro):
	PRODUCTO   = Producto.objects.get(pk=id_pro)
	designado = False
	usuario_designado = PRODUCTO.negocio.usuarios
	if request.user.is_authenticated():
		if (request.user.id == usuario_designado.id) or request.user.is_staff:
			designado = True
		else:
			designado = False
	else:
		designado = False
	titulo = PRODUCTO.negocio.nombre
	jsimagenes = True
	ctx        = {'producto':PRODUCTO,
				  'jsimagenes':jsimagenes,
				  'designado':designado,
				  'titulo':titulo
				  }
	return render_to_response('perfil/producto.html',ctx,
		context_instance=RequestContext(request))

@login_required
def nuevo_producto(request,id_neg):
	neg  = Negocio.objects.get(pk=id_neg)
	user = neg.usuarios
	if request.user.is_staff or (user.id == request.user.id):
		if request.method == "POST":
			form = nuevoProducto(request.POST,request.FILES)
			if form.is_valid():
				negocio       = Negocio.objects.get(pk=id_neg)
				nuevo         = form.save(commit=False)
				nuevo.negocio = negocio
				nuevo.save()
				return HttpResponseRedirect('/Singlenegocio/%s'%id_neg)
		else:
			form = nuevoProducto()
		titulo     = neg.nombre
		referencia = "Nuevo Producto"
		ctx        = {'formulario':form,'titulo':titulo,'referencia':referencia,'textarea':True}
		return render_to_response('formularios/formProducto.html',ctx,
			context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('/')

@login_required
def editar_producto(request,id_prod):
	producto = Producto.objects.get(pk=id_prod)
	usuario_designado = producto.negocio.usuarios
	if request.user.is_staff or (usuario_designado.id == request.user.id):
		if request.method == "POST":
			formulario = nuevoProducto(request.POST,request.FILES,instance=producto)
			if formulario.is_valid():
				edit_prod = formulario.save(commit=False)
				edit_prod.save()
				return	HttpResponseRedirect('/producto/%s/'%edit_prod.id)
		else:
			formulario = nuevoProducto(instance=producto)
		ctx = {'formulario':formulario,'textarea':True}
		return render_to_response('formularios/formProducto.html',ctx,
				context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('/')

@login_required
def borrar_producto(request, id_prod):
	prod              = Producto.objects.get(pk=id_prod)
	usuario_designado = prod.negocio.usuarios
	negocio           = prod.negocio.id	
	if request.user.is_staff or (usuario_designado.id == request.user.id):
		prod.delete()
		mensaje = "El producto se borro satisfactoriamente"
		ctx     = {'mensaje':mensaje,'negocio':negocio}
		return render_to_response('perfil/mensaje.html',ctx,
			context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('/')


#-----------------------------/FIN ABM PRODUCTO/-----------------------------------------------

#-------------------------------/ABM OFERTAS/--------------------------------------------------
def oferta(request,id_ofer):
	OFERTA   = Oferta.objects.get(pk=id_ofer)
	designado = False
	usuario_designado = OFERTA.negocio.usuarios
	if request.user.is_authenticated():
		if (request.user.id == usuario_designado.id) or request.user.is_staff:
			designado = True
		else:
			designado = False
	else:
		designado = False
	titulo = OFERTA.negocio.nombre
	jsimagenes = True
	ctx        = {'oferta':OFERTA,
				  'jsimagenes':jsimagenes,
				  'designado':designado,
				  'titulo':titulo
				  }
	return render_to_response('perfil/oferta.html',ctx,
		context_instance=RequestContext(request))

@login_required
def nueva_oferta(request,id_neg):
	neg  = Negocio.objects.get(pk=id_neg)
	user = neg.usuarios
	if request.user.is_staff or (user.id == request.user.id):
		if request.method == "POST":
			form = nuevaOferta(request.POST,request.FILES)
			if form.is_valid():
				negocio       = Negocio.objects.get(pk=id_neg)
				nuevo         = form.save(commit=False)
				nuevo.negocio = negocio
				nuevo.save()
				return HttpResponseRedirect('/Singlenegocio/%s/'%id_neg)
		else:
			form = nuevaOferta()
		titulo     = neg.nombre
		referencia = "Nueva Oferta"
		ctx        = {'formulario':form,'titulo':titulo,'referencia':referencia,'textarea':True}
		return render_to_response('formularios/formProducto.html',ctx,
			context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('/')

@login_required
def editar_oferta(request,id_ofer):
	oferta = Oferta.objects.get(pk=id_ofer)
	usuario_designado = oferta.negocio.usuarios
	titulo = oferta.negocio.nombre
	if request.user.is_staff or (usuario_designado.id == request.user.id):
		if request.method == "POST":
			formulario = nuevaOferta(request.POST,request.FILES,instance=oferta)
			if formulario.is_valid():
				edit_oferta = formulario.save(commit=False)
				edit_oferta.save()
				return	HttpResponseRedirect('/oferta/%s/'%id_ofer)
		else:
			formulario = nuevaOferta(instance=oferta)
		ctx = {'formulario':formulario,'textarea':True}
		return render_to_response('formularios/formProducto.html',ctx,
				context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('/')

@login_required
def borrar_oferta(request, id_ofer):
	oferta            = Oferta.objects.get(pk=id_ofer)
	usuario_designado = oferta.negocio.usuarios
	negocio           = oferta.negocio.id	
	if request.user.is_staff or (usuario_designado.id == request.user.id):
		oferta.delete()
		mensaje = "La Oferta se borro satisfactoriamente"
		ctx     = {'mensaje':mensaje,'negocio':negocio}
		return render_to_response('perfil/mensaje.html',ctx,
			context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('/')

#----------------------------/FIN ABM OFERTAS/----------------------------------------------------