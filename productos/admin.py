from django.contrib import admin
from models import *
from django.conf import settings

class ProductoAdmin(admin.ModelAdmin):
	class Media:
		js = ( '../'+settings.MEDIA_ROOT+'js/tiny_mce/tiny_mce.js', '../'+settings.MEDIA_ROOT+'/js/textareas.js')

class OfertaAdmin(admin.ModelAdmin):
	class Media:
		js = ( '../'+settings.MEDIA_ROOT+'js/tiny_mce/tiny_mce.js', '../'+settings.MEDIA_ROOT+'/js/textareas.js')



admin.site.register(Producto,ProductoAdmin)
admin.site.register(Oferta,OfertaAdmin)
