"""ProyectCovid19 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from AppCovid19.views.CRUDUbicacionView import UnRegistroidUbicacion
from AppCovid19.views.CRUDUbicacionView import MostarTodasUbicaciones
from AppCovid19.views.CRUDUbicacionView import CrearUbicacion
from AppCovid19.views.CRUDUbicacionView import ActualizarUbicacion
from AppCovid19.views.CRUDUbicacionView import CrearRegistro

urlpatterns = [
    path('admin/', admin.site.urls),
    path('consultarUnaUbicacion/<int:codigo_mun>/', UnRegistroidUbicacion.as_view()),
    path('consultarTodasUbicaciones/', MostarTodasUbicaciones.as_view()),
    path('crearUbicacion/', CrearUbicacion.as_view()),
    path('modificarUbicacion/<int:pk>/', ActualizarUbicacion.as_view()),
    path('CrearRegistro/', CrearRegistro.as_view()),
        
]
