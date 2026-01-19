from django.contrib import admin
from plan.models import *


@admin.register(Plan)
class Plan(admin.ModelAdmin):
    # columnas visibles en la lista del modelo
    list_display = ("nombre", "descripcion", "precio", "duracion_meses")
    # columnas con enlaces clickeables para entrar en el detalle
    list_display_links = ("nombre",)	#con coma al final xq es una tupla
    # campos por los que se pueden buscar
    search_fields = ("nombre",)
    # filtros laterales
    list_filter = ("duracion_meses",)
    # orden por defecto
    ordering = ("nombre", "precio")
