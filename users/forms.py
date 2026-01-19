from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User


class BootstrapFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({
                "class": "form-control"
            })


class UserRegisterForm(BootstrapFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        )


class CustomUserChangeForm(BootstrapFormMixin, UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "email",
            "bio",
        )
