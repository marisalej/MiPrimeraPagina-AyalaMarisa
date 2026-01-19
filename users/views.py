from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from .forms import UserRegisterForm, CustomUserChangeForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


@login_required
def profile(request):
    return render(request, "users/profile.html", {"user": request.user})


@login_required
def edit_profile(request):
    if request.method == "POST":
        form = CustomUserChangeForm(
            request.POST,
            #request.FILES,
            instance=request.user
        )
        if form.is_valid():
            #form.save()
            user = form.save(commit=False)

            if request.FILES.get("avatar"):
                user.avatar = request.FILES["avatar"]
            
            user.save()
            return redirect("users:profile")
    else:
        form = CustomUserChangeForm(instance=request.user)

    return render(
        request,
        "users/edit_profile.html",
        {"form": form}
    )


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) 
            return redirect("home")
    else:
        form = UserRegisterForm()

    return render(request, "users/register.html", {"form": form})


class CustomLoginView(LoginView):
    template_name = "users/login.html"


class CustomLogoutView(LogoutView):
    next_page = "/"


class CustomPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    template_name = "users/change_password.html"
    success_url = reverse_lazy("users:profile")
