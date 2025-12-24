from django.db.models import Q
from django.shortcuts import render, redirect
from .models import Socio
from .forms import SocioForm, SocioBusquedaForm

def crear_socio(request):
    if request.method == "POST":
        form = SocioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("socio:buscar")
    else:
        form = SocioForm()

    return render(request, "socio/socio_form.html", {"form": form})


# def buscar_socio(request):
#     form = SocioBusquedaForm(request.GET or None)
#     socios = Socio.objects.all()

#     if form.is_valid():
#         nombre = form.cleaned_data.get("nombre")
#         if nombre:
#             socios = socios.filter(nombre__icontains=nombre)

#     return render(
#         request,
#         "socio/socio_search.html",
#         {"form": form, "socios": socios}
#     )


def buscar_socio(request):
    query = request.GET.get("q")

    socios = Socio.objects.all()

    if query:
        socios = socios.filter(
            Q(nombre__icontains=query) |
            Q(apellido__icontains=query) |
            Q(dni__icontains=query)
        )

    return render(
        request,
        "socio/socio_search.html",
        {"socios": socios}
    )


def lista_socios(request):
    socios = Socio.objects.all()
    return render(request, 'socio/socio_list.html', {
        'socios': socios
    })