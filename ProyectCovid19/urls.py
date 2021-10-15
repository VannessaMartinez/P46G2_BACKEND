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
from AppCovid19.views.CRUDUbicacionView import consultar_registros_view
from AppCovid19.views.CRUDUbicacionView import UnRegistroidUbicacion
from AppCovid19.views.CRUDUbicacionView import MostarTodasUbicaciones
from AppCovid19.views.CRUDUbicacionView import CrearUbicacion
from AppCovid19.views.CRUDUbicacionView import ActualizarUbicacion
from AppCovid19.views.agregarRegistrosView import CrearRegistro
from AppCovid19.views.visualizarRegistros import MostarRegistros
from AppCovid19.views.ActualizarSeguimientoView import CrearSeguimiento
from AppCovid19.views.ActualizarSeguimientoView import ConsultarUnSeguimiento
from AppCovid19.views.ActualizarSeguimientoView import MostrarTodosSeguimientos
from AppCovid19.views.ActualizarSeguimientoView import ActualizarSeguimiento
from AppCovid19.views.filtrarRegistrosView      import FiltrarSexo, FiltrarEstado, FiltrarMunicipio

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('CrearUbicacion/', CrearUbicacion.as_view()),
    path('ConsultarUnaUbicacion/<int:codigo_mun>/', UnRegistroidUbicacion.as_view()),
    path('ConsultarTodasUbicaciones/', MostarTodasUbicaciones.as_view()),
    path('CodificarUbicacion/<int:pk>/', ActualizarUbicacion.as_view()),

    path('CrearSeguimiento/', CrearSeguimiento.as_view()),
    path('ActualizarSeguimiento/<int:pk>/', ActualizarSeguimiento.as_view()),
    path('ConsultarUnSeguimiento/<int:pk>/', ConsultarUnSeguimiento.as_view()),

    path('CrearRegistro/', CrearRegistro.as_view()),
    path('MostrarRegistros/', MostarRegistros.as_view()),

    path('FiltrarSexo/<sexo>/', FiltrarSexo.as_view()),
    path('FiltrarEstado/<estado>/', FiltrarEstado.as_view()),
    path('FiltrarMunicipio/<int:codigoDivipolaMunicipio>/', FiltrarMunicipio.as_view()),
]