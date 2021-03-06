from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, TemplateView, CreateView


from .forms import ContactForm


# Create your views here.

class IndexView(TemplateView):
	
	template_name = 'index.html'




def contact(request):

	success = False

	form = ContactForm(request.POST or None)
	if form.is_valid():
		form.send_mail()
		success = True
	
	context = {
		'form' : form,
		'success': success
	}
	return render(request, 'contact.html', context)

def product(request):
	return render(request, 'product.html')



