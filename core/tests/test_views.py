# coding=utf-8
from django.test import TestCase, Client
from django.urls import reverse
from django.core import mail


class IndexViewTestCase(TestCase):

	#executado no inicio do teste
	def setUp(self):
		self.client = Client()
		self.url = reverse('index')
	#executado ao final do teste
	def tearDown(self):
		pass

	#verificar se o codigo retornado é 200 ok
	def test_status_code(self):
		#pega a raiz do projeto o index
		response = self.client.get(self.url)
		self.assertEquals(response.status_code, 200)


	def test_template_used(self):
		#pega a raiz do projeto o index
		response = self.client.get(self.url)
		self.assertTemplateUsed(response, 'index.html')


class ContactViewTestCase(TestCase):
	#executado no inicio do teste
	def setUp(self):
		self.client = Client()
		self.url = reverse('contact')
	#executado ao final do teste
	def tearDown(self):
		pass	


	def test_view_ok(self):
		#pega a raiz do projeto o index
		response = self.client.get(self.url)
		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'contact.html')

	def test_form_error(self):
		data ={'name':'', 'email': '', 'message': ''}
		response = self.client.post(self.url, data)
		#form é o nome do formulario passado pelo contesto
		#name, email, message são os campos do formulario
		#o ultimo parametro é a mensagem de erro que o template vai dar, pq o campo esta vazio, tem que ser a msg igual a do navegador
		self.assertFormError(response, 'form', 'name', 'Este campo é obrigatório.')
		self.assertFormError(response, 'form', 'email', 'Este campo é obrigatório.')
		self.assertFormError(response, 'form', 'message', 'Este campo é obrigatório.')


	def test_form_ok(self):
		data ={'name':'test', 'email': 'test@email.com', 'message': 'msg test'}
		response = self.client.post(self.url, data)
		#verifica se a variavel success passada no contesto é verdadeira
		self.assertTrue(response.context['success'])
		#verifica se a caixa de saida do email tem um email
		self.assertEquals(len(mail.outbox), 1)
		#verifica se subject = assunto do primeiro email na caixa de saida é igual a msg passada como 2 parametro
		self.assertEquals(mail.outbox[0].subject,'Contato do Django Ecomerce')