from django.conf.urls import url
# from django.urls import path


from . import views

urlpatterns = [
	url(r'^$',views.product_list, name='product_list'),
	url(r'^(?P<slug>[\w_-]+)/$',views.category, name='category'),
	# path('/<slug:slug>/<int:teste>/', views.category, name='category'),
]