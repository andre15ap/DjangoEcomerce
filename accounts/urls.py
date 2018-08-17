

from django.urls import path

from . import views

urlpatterns = [
	path('registro/', views.RegisterView.as_view(), name='register'),
]