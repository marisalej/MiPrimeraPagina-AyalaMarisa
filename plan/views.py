from django.shortcuts import render, redirect
from .models import Plan
from .forms import PlanForm, PlanBusquedaForm

def crear_plan(request):
    if request.method == "POST":
        form = PlanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("plan:buscar")
    else:
        form = PlanForm()

    return render(request, "plan/plan_form.html", {"form": form})


def buscar_plan(request):
    form = PlanBusquedaForm(request.GET or None)
    planes = Plan.objects.all()

    if form.is_valid():
        nombre = form.cleaned_data.get("nombre")
        if nombre:
            planes = planes.filter(nombre__icontains=nombre)

    return render(
        request,
        "plan/plan_search.html",
        {"form": form, "planes": planes}
    )


def lista_planes(request):
    planes = Plan.objects.all()
    return render(request, "plan/plan_list.html", {"planes": planes})
