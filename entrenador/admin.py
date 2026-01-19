from django.contrib import admin
from entrenador.models import *


@admin.register(Entrenador)
class Entrenador(admin.ModelAdmin):
    list_display = ("nombre", "apellido", "especialidad", "telefono")
    list_display_links = ("nombre",)
    search_fields = ("apellido", "nombre")
    list_filter = ("especialidad",)
    ordering = ("apellido", "nombre")
