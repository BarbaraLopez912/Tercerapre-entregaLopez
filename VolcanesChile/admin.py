from django.contrib import admin
from VolcanesChile.models import Volcan, Clasificacion, Producto

# Register your models here.
admin.site.register(Volcan)
admin.site.register(Clasificacion)
admin.site.register(Producto)