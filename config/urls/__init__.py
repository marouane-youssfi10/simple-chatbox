from django.urls import include, path


urlpatterns = [
    path(f"", include("config.urls.admin_urls")),
    path(f"", include("config.urls.views_urls")),
]
