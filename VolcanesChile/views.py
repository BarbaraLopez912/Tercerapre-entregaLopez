from django.shortcuts import render, redirect
from django.http import HttpResponse
from VolcanesChile.models import Volcan, Clasificacion, Producto
from VolcanesChile.forms import VolcanForm, ProductoForm, ClasificacionForm, BuscarVolcan

def pag_principal(request):
    return render(request, "VolcanesChile/Volcanes_de_chile.html")

def unirse(request):
    return render(request, "VolcanesChile/Unirse.html")
def mostrar_volcanes(request):
    volcanes=Volcan.objects.all()
    contexto={"volcanes":volcanes,
              "form": BuscarVolcan(),
              }
    return render(request, "VolcanesChile/mostrar_volcanes.html", contexto)

def mostrar_clasificaciones(request):
    clasificaciones=Clasificacion.objects.all()
    contexto={"clasificaciones":clasificaciones}
    return render(request, "VolcanesChile/mostrar_clasificacion.html", contexto)

def mostrar_productos(request):
    productos=Producto.objects.all()
    contexto={"productos":productos}
    return render(request, "VolcanesChile/mostrar_productos.html", contexto)

def crear_volcan_form(request):
    if request.method == "POST":

        volcan_formulario = VolcanForm(request.POST)
        if volcan_formulario.is_valid():
            informacion = volcan_formulario.cleaned_data

            volcan_crear = Volcan(nombre=informacion["nombre"], region=informacion["region"])
            volcan_crear.save()
            return redirect("/app/volcanes/")

    volcan_formulario = VolcanForm()
    contexto = {
        "form": volcan_formulario
    }
    return render(request, "VolcanesChile/crear_volcan.html", contexto)

def crear_producto_form(request):
    if request.method == "POST":

        producto_formulario = ProductoForm(request.POST)
        if producto_formulario.is_valid():
            informacion = producto_formulario.cleaned_data

            producto_crear = Producto(producto=informacion["producto"], alcance=informacion["alcance"])
            producto_crear.save()
            return redirect("/app/productos/")

    producto_formulario = ProductoForm()
    contexto = {
        "form": producto_formulario
    }
    return render(request, "VolcanesChile/crear_producto.html", contexto)

def crear_clasificacion_form(request):
    if request.method == "POST":

        clasificacion_formulario = ClasificacionForm(request.POST)
        if clasificacion_formulario.is_valid():
            informacion = clasificacion_formulario.cleaned_data

            clasificacion_crear = Clasificacion(tipo=informacion["tipo"], alturacolumna=informacion["alturacolumna"])
            clasificacion_crear.save()
            return redirect("/app/clasificaciones/")

    clasificacion_formulario = ClasificacionForm()
    contexto = {
        "form": clasificacion_formulario
    }
    return render(request, "VolcanesChile/crear_clasificacion.html", contexto)

def busqueda_volcanes(request):

    region=request.GET["region"]
    volcanes=Volcan.objects.filter(region__icontains=region)
    contexto= {
        "volcanes":volcanes,
        "form": BuscarVolcan(),
    }
    return render(request, "VolcanesChile/mostrar_volcanes.html", contexto)