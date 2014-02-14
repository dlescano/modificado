from django import forms
from django.contrib.auth.models import User

class ContactForm(forms.Form):
	Email = forms.EmailField(widget=forms.TextInput())
	Titulo = forms.CharField(widget=forms.TextInput())
	Texto = forms.CharField(widget=forms.Textarea())

class LoginForm(forms.Form):
	usuario = forms.CharField(widget=forms.TextInput())
	contrasenia = forms.CharField(widget=forms.PasswordInput(render_value=False))


class RegistroForm(forms.Form):
	username     = forms.CharField(label="Nombre de Usuario",widget=forms.TextInput())
	email        = forms.CharField(label="Correo Electronico",widget=forms.TextInput())
	password_uno = forms.CharField(label="Password",widget=forms.PasswordInput(render_value=False))
	password_dos = forms.CharField(label="confirmar Password",widget=forms.PasswordInput(render_value=False))
	
	def clean_username(self):
		username = self.cleaned_data['username']
		try:
			u = User.objects.get(username=username)
		except User.DoesNotExist:
			return username
		raise forms.ValidationError('El nombre de usuario ya existe')

	def clean_email(self):
		email = self.cleaned_data['email']
		try:
			u = User.objects.get(email=email)
		except User.DoesNotExist:
			return email
		raise forms.ValidationError('El email ya esta registrado')

	def clean_password_dos(self):
		password_uno = self.cleaned_data['password_uno']
		password_dos = self.cleaned_data['password_dos']
		if password_uno == password_dos:
			pass
		else:
			raise forms.ValidationError("Los Passwords no coinciden ")
















