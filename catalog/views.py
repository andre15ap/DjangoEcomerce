from django.shortcuts import render, get_object_or_404
from django.views import generic

from .models import Product, Category


class ProductListView(generic.ListView):

	model = Product
	#a lista pode ser passado pelo model ou pela queryset
	# queryset = Product.objects.all()
	template_name = 'catalog/product_list.html'
	#o comando abaixo serve para mudar o nome no context, por padrao é o nome do model minusculo mais _list
	# context_object_name = 'products'

	paginate_by = 3

class CategoryListView(generic.ListView):

	template_name = 'catalog/category.html'	
	context_object_name = 'product_list'

	paginate_by = 3

	# customizar a listagem, seu queryset
	def get_queryset(self):
		# self.request - acesso a requisição 
		# self.kwargs - acesso aos argumentos nomeados
		# self.args - acesso aos argumentos não nomeados, numerados
		
		# caso queira pegar a category para fazer o filter depois
		# category = get_object_or_404(Category, slug=self.kwargs['slug'])

		return Product.objects.filter(category__slug=self.kwargs['slug'])

	#customizar os arqumentos do contesto
	def get_context_data(self, **kwargs):
		#metodo super chama a funcao padrao para manter o funcionamendo 
		context = super(CategoryListView, self).get_context_data(**kwargs)
		context['current_category']  = get_object_or_404(Category, slug=self.kwargs['slug'])
		return context



# def product_list(request):
# 	context = {
# 		'product_list' : Product.objects.all()
# 	}
# 	return render(request, 'catalog/product_list.html',context)

# def category(request, slug):
# 	category = Category.objects.get(slug=slug)
# 	context = {
# 		'current_category': category,
# 		'product_list' : Product.objects.filter(category=category)
# 	}
# 	return render(request, 'catalog/category.html', context)



def product(request, slug):
	product = Product.objects.get(slug=slug)

	context = {
		'product' : product
	}
	return render(request, 'catalog/product.html', context)