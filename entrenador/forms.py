from django import forms
from .models import Entrenador

class EntrenadorForm(forms.ModelForm):
    class Meta:
        model = Entrenador
        fields = "__all__"
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "apellido": forms.TextInput(attrs={"class": "form-control"}),
            "especialidad": forms.TextInput(attrs={"class": "form-control"}),
            "telefono": forms.TextInput(attrs={"class": "form-control"}),
        }

