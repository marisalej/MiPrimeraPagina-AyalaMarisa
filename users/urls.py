from django.urls import path
from . import views
from .views import edit_profile, CustomLoginView, CustomLogoutView, CustomPasswordChangeView

app_name = "users"

urlpatterns = [
    path("profile/", views.profile, name="profile"),
    path("register/", views.register, name="register"),
    path("profile/edit/", views.edit_profile, name="edit_profile"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", CustomLogoutView.as_view(), name="logout"),
    path("password/change/", CustomPasswordChangeView.as_view(), name="change_password"),
]

