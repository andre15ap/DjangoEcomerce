# coding=utf-8
from django.test import TestCase, Client
from django.urls import reverse

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
