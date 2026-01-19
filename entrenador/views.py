from django.shortcuts import render, redirect, get_object_or_404
from .models import Entrenador
from .forms import EntrenadorForm
from django.contrib.auth.decorators import login_required


@login_required
def crear_entrenador(request):
    if request.method == "POST":
        form = EntrenadorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("entrenador:lista")
    else:
        form = EntrenadorForm()

    return render(request, "entrenador/entrenador_form.html", {"form": form})


@login_required
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


@login_required
def lista_entrenadores(request):
    #entrenadores = Entrenador.objects.all()
    entrenadores = Entrenador.objects.order_by("apellido", "nombre")
    return render(
        request,
        "entrenador/entrenador_list.html",
        {"entrenadores": entrenadores}
    )


@login_required
def detalle_entrenador(request, id):
    entrenador = get_object_or_404(Entrenador, id=id)
    return render(
        request,
        "entrenador/entrenador_detail.html",
        {"entrenador": entrenador}
    )


@login_required
def editar_entrenador(request, id):
    entrenador = get_object_or_404(Entrenador, id=id)

    if request.method == "POST":
        form = EntrenadorForm(request.POST, instance=entrenador)
        if form.is_valid():
            form.save()
            return redirect("entrenador:lista")
    else:
        form = EntrenadorForm(instance=entrenador)

    return render(
        request,
        "entrenador/entrenador_form.html",
        {"form": form, "editar": True}
    )


@login_required
def eliminar_entrenador(request, id):
    entrenador = get_object_or_404(Entrenador, id=id)

    if request.method == "POST":
        entrenador.delete()
        return redirect("entrenador:lista")

    return render(
        request,
        "entrenador/entrenador_confirm_delete.html",
        {"entrenador": entrenador}
    )
