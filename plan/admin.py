from django.contrib import admin
from plan.models import *


@admin.register(Plan)
class Plan(admin.ModelAdmin):
    list_display = ("nombre", "descripcion", "precio", "duracion_meses")
    list_display_links = ("nombre",)
    search_fields = ("nombre",)
    list_filter = ("duracion_meses",)
    ordering = ("nombre", "precio")
