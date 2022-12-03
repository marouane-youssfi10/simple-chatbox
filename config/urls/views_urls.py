from django.urls import path, include


urlpatterns = [

    path('', include('core_apps.views.chat.urls')),
    path('accounts/', include('core_apps.views.users.urls')),
]
