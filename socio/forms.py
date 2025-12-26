from django import forms
from .models import Socio

class SocioForm(forms.ModelForm):
    class Meta:
        model = Socio
        fields = "__all__"
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "apellido": forms.TextInput(attrs={"class": "form-control"}),
            "dni": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "fecha_alta": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date"
                }
            ),
        }


