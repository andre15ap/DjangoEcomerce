"""DjangoEcomerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path


from django.urls import include, path
# from django.conf.urls import url, include #SERA DESCONTINUADA

from core import views
app_name = 'DjangoEcomerce'
urlpatterns = [
    path('admin/', admin.site.urls),

    #url ira ser substituido por path, url sera depreciada
    # url(r'^$',views.index, name="index"),
    # url(r'^contato/$',views.contact, name="contact"),
    # url(r'^produto/$',views.product, name="product"),
    # url(r'^produtos/', include(('catalog.urls', 'catalog'), namespace='catolog')), #novo modo de usar o include com url
    
    path('',views.index, name='index'),
    path('contato/', views.contact, name='contact'),
    # path('produtos/', include('catalog.urls'), name='catalog'),
    path('catalogo/', include(('catalog.urls', 'catalog'), namespace='catalog')),
]
