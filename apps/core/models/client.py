# Third-party Libraries
from django.conf import settings
from django.db import models

# Own Libraries
from apps.utils.model import Auditable


class Client(Auditable):
    name = models.CharField(max_length=255)
    city = models.ForeignKey(
        "City",
        on_delete=models.PROTECT,
        related_name="client_set",
    )
    category = models.ForeignKey(
        "Category",
        on_delete=models.PROTECT,
        related_name="client_set",
    )
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="client_set",
    )
    edited_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="editor_client_set",
    )

    class Meta:
        db_table = "client"
