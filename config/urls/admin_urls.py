from django.contrib import admin
from django.urls import path


urlpatterns = [
    path(f"admin/", admin.site.urls),
]