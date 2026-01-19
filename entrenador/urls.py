from django.urls import path
from . import views

app_name = 'entrenador'

urlpatterns = [
    path("", views.lista_entrenadores, name="lista"),
    path("crear/", views.crear_entrenador, name="crear"),
    path("buscar/", views.buscar_entrenador, name="buscar"),
    path("detalle/<int:id>/", views.detalle_entrenador, name="detalle"),
    path("editar/<int:id>/", views.editar_entrenador, name="editar"),
    path("eliminar/<int:id>/", views.eliminar_entrenador, name="eliminar"),
]
