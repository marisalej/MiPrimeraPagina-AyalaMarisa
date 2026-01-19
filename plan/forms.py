from django import forms
from .models import Plan

class PlanForm(forms.ModelForm):
    class Meta:
        model = Plan
        fields = [
            "nombre",
            "descripcion",
            "precio",
            "duracion_meses",
        ]
        
        widgets = {
            "descripcion": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 5,
                }
            ),
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "precio": forms.NumberInput(attrs={"class": "form-control"}),
            "duracion_meses": forms.NumberInput(attrs={"class": "form-control"}),
        }

