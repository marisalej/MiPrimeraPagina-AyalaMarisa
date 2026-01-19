from django.db import models

def socio_foto_upload(instance, filename):
    return f"socios/{instance.dni}/{filename}"

class Socio(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    dni = models.CharField(max_length=10, unique=True)
    email = models.EmailField()
    fecha_alta = models.DateField()
    foto = models.ImageField(
        upload_to=socio_foto_upload,
        blank=True,
        null=True
    )

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"
