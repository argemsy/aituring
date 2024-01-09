# Third-party Libraries
from django.contrib import admin

# Own Libraries
from apps.core.models import City


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    date_hierarchy = "created_at"
    list_display = (
        "name",
        "created_at",
        "is_active",
        "is_deleted",
    )
