from django.db import models

class Calificacion(models.Model):
    nombre = models.CharField(max_length=255)
    nota = models.DecimalField(max_digits=5, decimal_places=2)
    fecha = models.DateField()
