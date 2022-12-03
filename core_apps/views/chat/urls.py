from django.urls import path
from core_apps.views.chat.views import lobby

urlpatterns = [
    path("", lobby, name="home")
]
