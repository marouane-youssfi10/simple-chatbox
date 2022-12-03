from django.urls import path
from core_apps.views.users.views import loginPage, logoutUser, registerPage

urlpatterns = [
    path("login/", loginPage, name="login"),
    path("logout/", logoutUser, name="logout"),
    path("register/", registerPage, name="register"),
]
