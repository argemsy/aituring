# Third-party Libraries
from django.contrib import admin
from django.http.request import HttpRequest

# Own Libraries
from apps.core.models import Report, ReportHistory


class ReportHistoryInline(admin.TabularInline):
    model = ReportHistory
    fields = ["version", "is_last_version", "is_active", "is_deleted"]
    extra = 0

    def has_add_permission(self, request: HttpRequest, obj=None) -> bool:
        return False

    def has_change_permission(self, request: HttpRequest, obj=None) -> bool:
        return False

    def has_delete_permission(self, request: HttpRequest, obj=None) -> bool:
        return False


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    date_hierarchy = "created_at"
    list_display = (
        "id",
        "content_type",
        "object_id",
        "created_at",
        "is_active",
        "is_deleted",
    )
    raw_id_fields = [
        "created_by",
    ]
    inlines = [
        ReportHistoryInline,
    ]
