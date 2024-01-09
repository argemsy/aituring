# Third-party Libraries
from django.contrib import admin
from django.http.request import HttpRequest

# Own Libraries
from apps.core.models import AuditLog


@admin.register(AuditLog)
class AuditLogAdmin(admin.ModelAdmin):
    date_hierarchy = "created_at"
    list_display = (
        "content_type",
        "action",
        "object_id",
        "created_by_id",
        "created_at",
    )

    # def has_add_permission(self, request: HttpRequest, obj=None) -> bool:
    #     return False

    def has_change_permission(self, request: HttpRequest, obj=None) -> bool:
        return False

    def has_delete_permission(self, request: HttpRequest, obj=None) -> bool:
        return False
