from django import forms

class VolcanForm(forms.Form):
    nombre=forms.CharField()
    region=forms.CharField()

class ProductoForm(forms.Form):
    producto=forms.CharField()
    alcance=forms.CharField()

class ClasificacionForm(forms.Form):
    tipo=forms.CharField()
    alturacolumna=forms.IntegerField()

class BuscarVolcan(forms.Form):
    region=forms.CharField()
