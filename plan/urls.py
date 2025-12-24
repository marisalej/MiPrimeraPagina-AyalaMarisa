from django.urls import path
from . import views

app_name = 'plan'

urlpatterns = [
    path('', views.lista_planes, name='lista'),
    path('crear/', views.crear_plan, name='crear'),
    path('buscar/', views.buscar_plan, name='buscar'),
]
