"""ProyectoFinal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from ProyectoApp import views
from django.conf import settings

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from ProyectoApp.views import index, agregar_Platillo, eliminar_Platillo, restar_Platillo, limpiar_Platillo, agregar_ticket, compruebaLog, registroMesa

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ProyectoApp.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('agregar/<int:platillos_id>/', agregar_Platillo, name="Add"),
    path('eliminar/<int:platillos_id>/', eliminar_Platillo, name="Del"),
    path('restar/<int:platillos_id>/', restar_Platillo, name="Sub"),
    path('limpiar/', limpiar_Platillo, name="CLS"),
    path('GRD/', agregar_ticket, name="GRD"),
    path('CPL/', compruebaLog, name="CPL"),
    path('RGM/', registroMesa, name="RGM"),
]
urlpatterns += staticfiles_urlpatterns()