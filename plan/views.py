from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView
)
from .models import Plan
from .forms import PlanForm
from django.contrib.auth.mixins import LoginRequiredMixin


class PlanCreateView(LoginRequiredMixin, CreateView):
    model = Plan
    form_class = PlanForm
    template_name = "plan/plan_form.html"
    success_url = reverse_lazy("plan:lista")


class PlanSearchView(LoginRequiredMixin, ListView):
    model = Plan
    template_name = "plan/plan_search.html"
    context_object_name = "planes"

    def get_queryset(self):
        query = self.request.GET.get("q")
        qs = Plan.objects.all()

        if query:
            qs = qs.filter(
                Q(nombre__icontains=query) |
                Q(descripcion__icontains=query)
            )

        return qs


class PlanListView(LoginRequiredMixin, ListView):
    model = Plan
    template_name = "plan/plan_list.html"
    context_object_name = "planes"
    ordering = ["nombre"]


class PlanDetailView(LoginRequiredMixin, DetailView):
    model = Plan
    template_name = "plan/plan_detail.html"
    context_object_name = "plan"


class PlanUpdateView(LoginRequiredMixin, UpdateView):
    model = Plan
    form_class = PlanForm
    template_name = "plan/plan_form.html"
    success_url = reverse_lazy("plan:lista")


class PlanDeleteView(LoginRequiredMixin, DeleteView):
    model = Plan
    template_name = "plan/plan_confirm_delete.html"
    success_url = reverse_lazy("plan:lista")