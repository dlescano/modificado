# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from forms import *
from django.template.loader import get_template

#from django.core.mail import EmailMultiAlternatives
from django.core.mail import EmailMessage

from django.http import HttpResponse, HttpResponseRedirect
from localizacion.models import  Barrio,Negocio,Categoria
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User


from django.shortcuts import render
 
def handler404(request):
	return render(request, 'home/error/404.html')
def handler500(request):
	return render(request, 'home/error/500.html')



def views_index(request):
	barrios    = Barrio.objects.all()
	categorias = Categoria.objects.all()
	barrio     = request.POST.get("dato1","")
	categoria  = request.POST.get("dato2","")
	mapa = True
	print barrio
	print categoria
	if barrio == '' and categoria == '':
		ctx = {'barrios':barrios,'categorias':categorias,'mapaG':mapa}
		return render_to_response ('home/buscadores.html',ctx,context_instance=RequestContext(request))
	elif barrio != '' or categoria != '':
		if barrio != '' and categoria == '':
			negocios = Negocio.objects.all().filter(barrios__nombre=barrio)
			mapa = False
			ctx = {'negocios':negocios,'mapaG':mapa}
		elif barrio == '' and categoria != '':
			negocios = Negocio.objects.all().filter(categorias__nombre=categoria)
			mapa = False
			ctx = {'negocios':negocios,'mapaG':mapa}	
		elif barrio != '' and categoria != '':
			negocios = Negocio.objects.all().filter(barrios__nombre=barrio,categorias__nombre=categoria)
			mapa = False
			ctx = {'negocios':negocios,'mapaG':mapa}
		return render_to_response('listados/negocios.html',ctx,context_instance=RequestContext(request))
	else:
		ctx = {'barrios':barrios,'categorias':categorias,'mapaG':mapa}
		return render_to_response ('home/buscadores.html',ctx,context_instance=RequestContext(request))
	
#########################################################################################################
def views_info_registro(request):
	mapa = False
	ctx = {'mapaG':mapa}
	return render_to_response('home/tipo-registro-info.html',ctx,
		context_instance=RequestContext(request))

def views_Contact(request):
	mapa = False
	info_enviada = False
	email        = ""
	titulom      = ""
	texto        = ""
	if request.method == "POST":
		formulario = ContactForm(request.POST)
		if formulario.is_valid():
			info_enviada = True
			email        = formulario.cleaned_data['Email'] 
			titulom      = formulario.cleaned_data['Titulo']
			texto        = formulario.cleaned_data['Texto']
			#si todo sale bien se envia la informacion 
			to_admin     = 'vustralbil@gmail.com'
			html_content = "Informacion recibida de:  [%s]   ***Mensaje***  %s  "%(email,texto)
			msg          = EmailMessage("subject", html_content, to=[to_admin])
			#msg.attach_alternative(html_content,'text/html')
			#msg.send()
	else:
		formulario = ContactForm()
	ctx = {'form':formulario,'email':email,'titulom':titulom,'texto':texto,'info_enviada':info_enviada,'mapaG':mapa}
	return render_to_response('home/contacto.html',
		ctx,context_instance=RequestContext(request))

#login de usuarios 
def views_login(request):
	mapa = False
	mensaje = ""
	if request.user.is_authenticated():
		return HttpResponseRedirect('/')
	else:
		if request.method == "POST":
			form = LoginForm(request.POST)
			if form.is_valid():
				usuario = form.cleaned_data['usuario']
				contrasenia = form.cleaned_data['contrasenia']
				usuario = authenticate(username=usuario,password=contrasenia)
				if usuario is not None and usuario.is_active:
					login(request,usuario)
					return HttpResponseRedirect('/')
				else:
					mensaje = "usuario y/o contrasenia incorrecta"
		form = LoginForm()
		ctx = {'form':form,'mensaje':mensaje,'mapaG':mapa}
		return render_to_response('home/login.html',ctx,context_instance=RequestContext(request))

def views_logout(request):
	logout(request)
	return HttpResponseRedirect('/')

"""
def views_registro(request):
	mapa = False
	formulario = RegistroForm()
	if request.method == "POST":
		formulario = RegistroForm(request.POST)
		if formulario.is_valid():
			usuario      = formulario.cleaned_data['username']
			email        = formulario.cleaned_data['email']
			password_uno = formulario.cleaned_data['password_uno']
			password_dos = formulario.cleaned_data['password_dos']
			u            = User.objects.create_user(username=usuario,email=email,password=password_uno)
			u.save()
			ctx = {'mapaG':mapa}
			return	render_to_response('home/gracias.html',context_instance=RequestContext(request))
		else:
			ctx = {'formulario':formulario,'mapaG':mapa}
			return render_to_response('home/registro_usuarios.html',ctx,context_instance=RequestContext(request))
	ctx = {'formulario':formulario,'mapaG':mapa}
	return render_to_response('home/registro_usuarios.html',ctx,context_instance=RequestContext(request))
"""
#ESTO ES PARA PROBAR TEMPLATES
def index2(request):
	return render_to_response('home/error/500.html',context_instance=RequestContext(request))


