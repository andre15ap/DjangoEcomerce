from django.contrib import admin

from catalog.models import Product, Category


class CategoryAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug', 'created', 'modified']
	search_fields = ['name', 'slug']
	list_filter = ['created', 'modified']

class ProductAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug', 'category', 'created', 'modified']
	search_fields = ['name', 'slug', 'category__name']


	#para pegar o nome do foreikey
	def get_name(self, obj):
		return obj.category
	#alterar o nome de descricao da funcao 
	get_name.short_description = 'Categoria'

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)