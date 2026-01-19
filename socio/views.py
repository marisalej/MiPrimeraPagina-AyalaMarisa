from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView
)
from .models import Socio
from .forms import SocioForm
from django.contrib.auth.mixins import LoginRequiredMixin


class SocioCreateView(LoginRequiredMixin, CreateView):
    model = Socio
    form_class = SocioForm
    template_name = "socio/socio_form.html"
    success_url = reverse_lazy("socio:lista")


class SocioSearchView(LoginRequiredMixin, ListView):
    model = Socio
    template_name = "socio/socio_search.html"
    context_object_name = "socios"

    def get_queryset(self):
        query = self.request.GET.get("q")
        qs = Socio.objects.all()

        if query:
            qs = qs.filter(
                Q(nombre__icontains=query) |
                Q(apellido__icontains=query) |
                Q(dni__icontains=query)
            )
        return qs


class SocioListView(LoginRequiredMixin, ListView):
    model = Socio
    template_name = "socio/socio_list.html"
    context_object_name = "socios"
    ordering = ["apellido", "nombre"]


class SocioDetailView(LoginRequiredMixin, DetailView):
    model = Socio
    template_name = "socio/socio_detail.html"
    context_object_name = "socio"


class SocioUpdateView(LoginRequiredMixin, UpdateView):
    model = Socio
    form_class = SocioForm
    template_name = "socio/socio_form.html"
    success_url = reverse_lazy("socio:lista")


class SocioDeleteView(LoginRequiredMixin, DeleteView):
    model = Socio
    template_name = "socio/socio_confirm_delete.html"
    success_url = reverse_lazy("socio:lista")

