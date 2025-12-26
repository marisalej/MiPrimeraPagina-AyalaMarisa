from django import forms
from .models import Plan

class PlanForm(forms.ModelForm):
    class Meta:
        model = Plan
        fields = "__all__"
        widgets = {
            "descripcion": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 5,   # cantidad de filas visibles
                    #"placeholder": "Descripción del plan"
                }
            ),
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "precio": forms.NumberInput(attrs={"class": "form-control"}),
            "duracion_meses": forms.NumberInput(attrs={"class": "form-control"}),
        }

