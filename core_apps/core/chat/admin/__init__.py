from django.contrib import admin

from core_apps.core.chat.models import Message


class MessageAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "message"]


admin.site.register(Message, MessageAdmin)
