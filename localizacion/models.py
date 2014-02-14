from django.db import models
from django.contrib.gis.db import models
from django.contrib.auth.models import User
from django.conf import settings

class UserNegocio(models.Model):
	user  = models.OneToOneField(User)
	apodo = models.CharField(max_length=255)
	def __unicode__(self):
		return self.apodo


class Barrio(models.Model):
	nombre      = models.CharField(max_length=255)
	info		= models.TextField(blank=True)
	lon 		= models.CharField(max_length=255)
	lat 		= models.CharField(max_length=255)
	def __unicode__(self): 
		return self.nombre 

class Categoria(models.Model):
	nombre  	= models.CharField(max_length=255)
	def __unicode__(self):
		return self.nombre
		
class Negocio(models.Model):
		
	nombre             = models.CharField(max_length=50)
	barrios            = models.ForeignKey(Barrio)
	direccion          = models.CharField(max_length=50,blank=True)
	telefono           = models.CharField(max_length=50)
	categorias         = models.ManyToManyField(Categoria)
	info               = models.TextField(blank=True,null=True)
	horario            = models.CharField(max_length = 100)
	sucursales         = models.IntegerField()
	facebook           = models.URLField(max_length=300,blank=True,null=True)
	twitter            = models.URLField(max_length=300,blank=True,null=True)
	web                = models.URLField(max_length=300,blank=True,null=True)
	email              = models.EmailField(max_length=300,blank=True,null=True)
	status             = models.BooleanField(default=True)
	cantidad_ofertas   = models.IntegerField()
	cantidad_productos = models.IntegerField()
	usuarios  		   = models.ForeignKey(UserNegocio,blank=True,null=True)
	localizacion_mapa  = models.MultiPointField()
	objects            = models.GeoManager()
	def url(self,filename):
		ruta = "img/img_Negocios/%s/%s"%(self.nombre,str(filename))
		return ruta
	imagen             = models.ImageField(upload_to=url,blank=True)
	def __unicode__(self):
		return self.nombre

class Sucursal(models.Model):
	def url(self,filename):
		ruta = "img/img_Negocios/%d/%s/%s"%(self.id,self.nombre,str(filename))
		return ruta
	nombre             = models.CharField(max_length=50)
	barrios            = models.ForeignKey(Barrio)
	direccion          = models.CharField(max_length=50,blank=True)
	telefono           = models.CharField(max_length=50)
	info               = models.TextField(blank=True,null=True)
	horario            = models.CharField(max_length = 100)
	imagen             = models.ImageField(upload_to=url,blank=True)
	cantidad_ofertas   = models.IntegerField()
	cantidad_productos = models.IntegerField()
	casa_central       = models.ForeignKey(Negocio)
	localizacion_mapa  = models.MultiPointField()
	objects            = models.GeoManager()
	def __unicode__(self):
		return self.nombre

