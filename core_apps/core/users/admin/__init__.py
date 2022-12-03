from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils import timesince
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class UserAdmin(BaseUserAdmin):
    ordering = ["-id"]
    model = User
    list_display = [
        "id",
        "email",
        "first_name",
        "last_name",
        "_date_joined",
        "_last_login",
        "is_staff",
        "is_active",
    ]
    list_display_links = ["email"]
    list_filter = ("is_staff",)
    fieldsets = (
        (
            _("Login Credentials"),
            {"fields": ("email", "password")},
        ),
        (
            _("Personal Information"),
            {
                "fields": (
                    "username",
                    "first_name",
                    "last_name",
                )
            },
        ),
        (
            _("Permissions and Groups"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (_("Important Dates"), {"fields": ("last_login", "date_joined")}),
    )
    readonly_fields = ("date_joined", "last_login")
    search_fields = ["email", "username", "first_name", "last_name"]

    def _date_joined(self, obj):
        return timesince.timesince(obj.date_joined) + " ago"

    def _last_login(self, obj):
        return timesince.timesince(obj.last_login) + " ago" if obj.last_login else "-"


admin.site.register(User, UserAdmin)
