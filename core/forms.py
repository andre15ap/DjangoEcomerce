
from django import forms
from django.core.mail import send_mail
from django.conf import settings

class ContactForm(forms.Form):
	name = forms.CharField(label='Nome')
	email = forms.EmailField(label='E-mail')
	message = forms.CharField(label='Mensagem', widget=forms.Textarea(attrs={'rows':'4'}))


	def send_mail(self):
		nome = self.cleaned_data['name']
		email = self.cleaned_data['email']
		message = self.cleaned_data['message']
		message = 'Nome: {} \nEmail: {}\n {}'.format(nome,email,message)
		print('-------------chegou aqui\n')
		#1 parametro = titulo da msg, 2 mensagem, 3 email de saida, 4 lista com emails destino
		send_mail(
			'Contato do Django Ecomerce',message, settings.DEFAULT_FROM_EMAIL, [settings.DEFAULT_FROM_EMAIL]
			)

	# def __init__(self, *args, **kwargs):
	# 	super(ContactForm, self).__init__(*args, **kwargs)
	# 	self.fields['name'].widget.attrs['class'] = 'form-control'
	# 	self.fields['email'].widget.attrs['class'] = 'form-control'
	# 	self.fields['message'].widget.attrs['class'] = 'form-control'