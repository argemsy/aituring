# Third-party Libraries
from django.contrib import admin

# Own Libraries
from apps.core.models import Country


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    date_hierarchy = "created_at"
    list_display = (
        "name",
        "code",
        "slug",
        "created_at",
        "is_active",
        "is_deleted",
    )
