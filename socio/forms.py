from django import forms
from .models import Socio

class SocioForm(forms.ModelForm):
    class Meta:
        model = Socio
        fields = "__all__"
        widgets = {
            "fecha_alta": forms.DateInput(
                attrs={
                    "type": "date",
                    "class": "form-control"
                }
            ),
        }


class SocioBusquedaForm(forms.Form):
    q = forms.CharField(
        label="Buscar",
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Buscar por nombre o DNI'
        })
    )
