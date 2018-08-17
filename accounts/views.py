from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic import CreateView

from .models import User
from .forms import UserAdminCreationForm


class RegisterView(CreateView):
	form_class = UserAdminCreationForm
	template_name = 'accounts/register.html'
	model = User
	success_url = reverse_lazy('index')
