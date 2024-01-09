# Third-party Libraries
from django.db import models

MODEL_CATEGORY = 1
MODEL_CITY = 2
MODEL_CLIENT = 3
MODEL_COUNTRY = 4
MODEL_REPORT = 5


LOG_CONTENT_TYPE_CHOICES = (
    (MODEL_CATEGORY, "MODEL_CATEGORY"),
    (MODEL_CITY, "MODEL_CITY"),
    (MODEL_CLIENT, "MODEL_CLIENT"),
    (MODEL_COUNTRY, "MODEL_COUNTRY"),
    (MODEL_REPORT, "MODEL_REPORT"),
)

ADDITION = 1
EDITION = 2
DELETION = 3


LOG_ACTIONS_CHOICES = (
    (ADDITION, "ADDITION"),
    (EDITION, "EDITION"),
    (DELETION, "DELETION"),
)


class AuditLog(models.Model):
    content_type = models.SmallIntegerField(
        choices=LOG_CONTENT_TYPE_CHOICES,
        db_index=True,
    )
    action = models.SmallIntegerField(
        choices=LOG_ACTIONS_CHOICES,
        db_index=True,
    )
    object_id = models.TextField(
        db_index=True,
        help_text="Source Model ID",
    )
    created_by_id = models.IntegerField(
        db_index=True,
    )
    message = models.JSONField(
        default=dict,
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
    )

    class Meta:
        db_table = "audit_log"
