from django.shortcuts import render, redirect
from .models import Entrenador
from .forms import EntrenadorForm, EntrenadorBusquedaForm

def crear_entrenador(request):
    if request.method == "POST":
        form = EntrenadorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("entrenador:buscar")
    else:
        form = EntrenadorForm()

    return render(request, "entrenador/entrenador_form.html", {"form": form})


def buscar_entrenador(request):
    form = EntrenadorBusquedaForm(request.GET or None)
    entrenadores = Entrenador.objects.all()

    if form.is_valid():
        nombre = form.cleaned_data.get("nombre")
        if nombre:
            entrenadores = entrenadores.filter(nombre__icontains=nombre)

    return render(
        request,
        "entrenador/entrenador_search.html",
        {"form": form, "entrenadores": entrenadores}
    )

def lista_entrenadores(request):
    entrenadores = Entrenador.objects.all()
    return render(
        request,
        "entrenador/entrenador_list.html",
        {"entrenadores": entrenadores}
    )


