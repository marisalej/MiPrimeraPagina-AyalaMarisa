from django.db import models

class Socio(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    dni = models.CharField(max_length=10)
    email = models.EmailField()
    fecha_alta = models.DateField()

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"

