from django.urls import path
from .views import (
    PlanListView,
    PlanSearchView,
    PlanCreateView,
    PlanDetailView,
    PlanUpdateView,
    PlanDeleteView
)


app_name = 'plan'

urlpatterns = [
    path("", PlanListView.as_view(), name="lista"),
    path("crear/", PlanCreateView.as_view(), name="crear"),
    path("buscar/", PlanSearchView.as_view(), name="buscar"),
    path("<int:pk>/", PlanDetailView.as_view(), name="detalle"),
    path("<int:pk>/editar/", PlanUpdateView.as_view(), name="editar"),
    path("<int:pk>/eliminar/", PlanDeleteView.as_view(), name="eliminar"),
]
