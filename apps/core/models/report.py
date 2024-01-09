# Third-party Libraries
from django.conf import settings
from django.db import models

# Own Libraries
from apps.utils.model import Auditable

CLIENT_REPORT = 1


REPORT_CONTENT_TYPE_CHOICES = ((CLIENT_REPORT, "CLIENT_REPORT"),)


class Report(Auditable):
    content_type = models.SmallIntegerField(
        choices=REPORT_CONTENT_TYPE_CHOICES,
        default=CLIENT_REPORT,
        db_index=True,
    )
    object_id = models.IntegerField(
        db_index=True,
        help_text="Model ID",
    )
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.DO_NOTHING,
        related_name="report_set",
    )
    url = models.URLField(
        max_length=255,
        db_index=True,
    )

    class Meta:
        db_table = "report"


class ReportHistory(Auditable):
    report = models.ForeignKey(
        "Report",
        on_delete=models.PROTECT,
        related_name="report_history_set",
    )
    version = models.SmallIntegerField(default=1)
    is_last_version = models.BooleanField(default=True)

    class Meta:
        db_table = "report_history"
