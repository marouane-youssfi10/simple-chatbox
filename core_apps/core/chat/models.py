from django.db import models
from django.utils.translation import gettext_lazy as _

from core_apps.core.chat.managers import MessageManager
from core_apps.core.users.admin import User


class Message(models.Model):
    user = models.ForeignKey(
        User, verbose_name=_("user"), related_name="message", on_delete=models.CASCADE
    )
    message = models.CharField(
        verbose_name=_("message"), max_length=1000, blank=False, null=False
    )
    created_at = models.DateTimeField(auto_now_add=True)

    objects = MessageManager()

    def __str__(self):
        return self.message
