from django.contrib import admin
from socio.models import *


@admin.register(Socio)
class Socio(admin.ModelAdmin):
    list_display = ("nombre", "apellido", "dni", "email", "fecha_alta")
    list_display_links = ("nombre",)
    search_fields = ("apellido", "nombre", "dni")
    ordering = ("apellido", "nombre")
