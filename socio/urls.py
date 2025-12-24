from django.urls import path
from . import views

app_name = 'socio'

urlpatterns = [
    path('', views.lista_socios, name='lista'),
    path('crear/', views.crear_socio, name='crear'),
    path('buscar/', views.buscar_socio, name='buscar'),
]
