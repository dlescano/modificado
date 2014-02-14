from django import forms
from productos.models import Producto,Oferta

class nuevoProducto(forms.ModelForm):
	class Meta:
		model   = Producto
		exclude = {'usuarios','negocio'}

class nuevaOferta(forms.ModelForm):
	class Meta:
		model   = Oferta
		exclude = {'usuarios','negocio'}



