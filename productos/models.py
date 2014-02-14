from django.db import models
from localizacion.models import Negocio
from django.conf import settings

class Producto(models.Model):
	def url(self,filename):
		ruta = "img/productos/%s/%s"%(self.nombre,str(filename))
		return ruta
	nombre    = models.CharField(max_length=300)
	info      = models.TextField(blank=True)
	precio    = models.DecimalField(max_digits=10, decimal_places=2)
	marca	  = models.CharField(max_length=300,blank=True,null=True)
	stock     = models.IntegerField(blank=True)
	negocio   = models.ForeignKey(Negocio)
	imagen1	  = models.ImageField(upload_to=url,blank=True,null=True)
	imagen2	  = models.ImageField(upload_to=url,blank=True,null=True)
	imagen3	  = models.ImageField(upload_to=url,blank=True,null=True)
	
	def __unicode__(self):
		return self.nombre


class Oferta(models.Model):
	def url(self,filename):
		ruta = "img/ofertas/%s/%s"%(self.nombre,str(filename))
		return ruta
	nombre  = models.CharField(max_length=300)
	info    = models.TextField(blank=True)
	precio  = models.DecimalField(max_digits=10, decimal_places=2)
	marca   = models.CharField(max_length=300,blank=True,null=True)
	stock   = models.IntegerField(blank=True)
	negocio = models.ForeignKey(Negocio)
	imagen1 = models.ImageField(upload_to=url,blank=True,null=True)
	imagen2 = models.ImageField(upload_to=url,blank=True,null=True)
	imagen3 = models.ImageField(upload_to=url,blank=True,null=True)
	desde   = models.DateField(blank=True)
	hasta   = models.DateField(blank=True)
	def __unicode__(self):
		return self.nombre
