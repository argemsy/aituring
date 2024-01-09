# Third-party Libraries
from django.db import models

# Own Libraries
from apps.utils.model import Auditable


class Category(Auditable):
    name = models.CharField(max_length=255)
    description = models.TextField(
        blank=True,
        null=True,
    )

    class Meta:
        db_table = "category"
