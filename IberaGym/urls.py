from django.contrib import admin
from django.urls import path, include
from .views import home, about
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("about/", about, name="about"),
    path("socios/", include("socio.urls")),
    path("entrenadores/", include("entrenador.urls")),
    path("planes/", include("plan.urls")),
    path("users/", include("users.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

