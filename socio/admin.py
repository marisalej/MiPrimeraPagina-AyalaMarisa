from django.contrib import admin
from socio.models import *


@admin.register(Socio)
class Socio(admin.ModelAdmin):
    # columnas visibles en la lista del modelo
    list_display = ("nombre", "apellido", "dni", "email", "fecha_alta")
    # columnas con enlaces clickeables para entrar en el detalle
    list_display_links = ("nombre",)	#con coma al final xq es una tupla
    # campos por los que se pueden buscar
    search_fields = ("apellido", "nombre", "dni")
    # filtros laterales
    #list_filter = ("fecha_de_creacion",)
    # orden por defecto
    ordering = ("apellido", "nombre")
    # campos de solo lectura
    #readonly_fields = ("fecha_de_creacion",)
