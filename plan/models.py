from django.db import models

class Plan(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    duracion_meses = models.IntegerField()

    def __str__(self):
        return self.nombre
