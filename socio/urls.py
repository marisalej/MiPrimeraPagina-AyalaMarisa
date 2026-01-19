from django.urls import path
from .views import (
    SocioListView,
    SocioSearchView,
    SocioCreateView,
    SocioDetailView,
    SocioUpdateView,
    SocioDeleteView
)

app_name = "socio"

urlpatterns = [
    path("", SocioListView.as_view(), name="lista"),
    path("buscar/", SocioSearchView.as_view(), name="buscar"),
    path("crear/", SocioCreateView.as_view(), name="crear"),
    path("<int:pk>/", SocioDetailView.as_view(), name="detalle"),
    path("<int:pk>/editar/", SocioUpdateView.as_view(), name="editar"),
    path("<int:pk>/eliminar/", SocioDeleteView.as_view(), name="eliminar"),
]
