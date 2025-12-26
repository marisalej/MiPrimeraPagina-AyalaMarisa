from django.shortcuts import render, redirect
from .models import Plan
from .forms import PlanForm

def crear_plan(request):
    if request.method == "POST":
        form = PlanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("plan:lista")
    else:
        form = PlanForm()

    return render(request, "plan/plan_form.html", {"form": form})


def buscar_plan(request):
    query = request.GET.get("q", "")
    planes = Plan.objects.all()

    if query:
        planes = planes.filter(nombre__icontains=query)

    return render(
        request,
        "plan/plan_search.html",
        {
            "planes": planes,
            "query": query
        }
    )


def lista_planes(request):
    planes = Plan.objects.all()
    return render(request, "plan/plan_list.html", {"planes": planes})
