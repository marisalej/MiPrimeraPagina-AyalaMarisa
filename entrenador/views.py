from django.shortcuts import render, redirect
from .models import Entrenador
from .forms import EntrenadorForm

def crear_entrenador(request):
    if request.method == "POST":
        form = EntrenadorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("entrenador:lista")
    else:
        form = EntrenadorForm()

    return render(request, "entrenador/entrenador_form.html", {"form": form})


def buscar_entrenador(request):
    query = request.GET.get("q", "")
    entrenadores = Entrenador.objects.all()

    if query:
        entrenadores = entrenadores.filter(nombre__icontains=query)

    return render(
        request,
        "entrenador/entrenador_search.html",
        {
            "entrenadores": entrenadores,
            "query": query
        }
    )


def lista_entrenadores(request):
    entrenadores = Entrenador.objects.all()
    return render(
        request,
        "entrenador/entrenador_list.html",
        {"entrenadores": entrenadores}
    )

