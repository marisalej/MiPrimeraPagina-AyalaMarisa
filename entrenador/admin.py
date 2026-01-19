from django.contrib import admin
from entrenador.models import *

@admin.register(Entrenador)
class Entrenador(admin.ModelAdmin):
    # columnas visibles en la lista del modelo
    list_display = ("nombre", "apellido", "especialidad", "telefono")
    # columnas con enlaces clickeables para entrar en el detalle
    list_display_links = ("nombre",)	#con coma al final xq es una tupla
    # campos por los que se pueden buscar
    search_fields = ("apellido", "nombre")
    # filtros laterales
    list_filter = ("especialidad",)
    # orden por defecto
    ordering = ("apellido", "nombre")
    
