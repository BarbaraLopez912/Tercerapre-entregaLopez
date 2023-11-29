"""
URL configuration for TerceraPreentrega project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from VolcanesChile.views import mostrar_volcanes, mostrar_clasificaciones, mostrar_productos, crear_volcan_form, crear_producto_form, crear_clasificacion_form, busqueda_volcanes, pag_principal, unirse


urlpatterns = [
    path('principal/', pag_principal),
    path('unirse/', unirse),
    path('buscar_volcanes/', busqueda_volcanes),
    path('agregar_volcan/', crear_volcan_form),
    path('agregar_producto/', crear_producto_form),
    path('agregar_clasificacion/', crear_clasificacion_form),
    path('admin/', admin.site.urls),
    path('volcanes/', mostrar_volcanes),
    path('clasificaciones/', mostrar_clasificaciones),
    path('productos/', mostrar_productos),
]
