# from django.conf.urls import url
from django.urls import path


from . import views

urlpatterns = [
	path('',views.ProductListView.as_view(), name='product_list'),
	path('<slug:slug>/', views.CategoryListView.as_view(), name='category'),
	path('produtos/<slug:slug>/', views.product, name='product'),
]