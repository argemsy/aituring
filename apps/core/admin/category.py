# Third-party Libraries
from django.contrib import admin

# Own Libraries
from apps.core.models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    date_hierarchy = "created_at"
    list_display = (
        "name",
        "created_at",
        "is_active",
        "is_deleted",
    )
