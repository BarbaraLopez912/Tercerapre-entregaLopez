from django.db import models

class Volcan(models.Model):
    nombre = models.CharField(max_length=20)
    region = models.CharField(max_length=30)

    def __str__(self):
        return f"Volcan: {self.nombre}, Región: {self.region}"

class Clasificacion(models.Model):
    tipo = models.CharField(max_length=20)
    alturacolumna = models.IntegerField()

    def __str__(self):
        return f"Tipo: {self.tipo}, Altura de la columna piroclástica (km): hasta {self.alturacolumna} km"

class Producto(models.Model):
    producto=models.CharField(max_length=20)
    alcance=models.CharField(max_length=20)

    def __str__(self):
        return f"Producto: {self.producto}, Alcance: {self.alcance}"