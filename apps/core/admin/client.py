# Third-party Libraries
from django.contrib import admin

# Own Libraries
from apps.core.models import Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    date_hierarchy = "created_at"
    list_display = (
        "name",
        "city",
        "category",
        "created_by",
        "edited_by",
        "created_at",
        "is_active",
        "is_deleted",
    )
    raw_id_fields = [
        "city",
        "category",
        "created_by",
        "edited_by",
    ]
